# This was designed for the AQA GCSE German Revision Guide
# Other PDFs on Pearson Revise Online may vary

import os
import requests
from pypdf import PdfWriter
from selenium import webdriver

# Configuration
OUTPUT_PDF = "full_revision_guide.pdf"
TEMP_DIR = "temp_pdfs"

def main():
    options = webdriver.ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    
    print("Launching browser...")
    driver = webdriver.Chrome(options=options)
    driver.get("https://reviseonline.pearson.com/")
    
    print("=" * 60)
    print("1. Log in to your account in the opened browser window.")
    print("2. Open your revision guide table of contents.")
    print("=" * 60)
    
    input("👉 Press **Enter** here once you are on the table of contents and ran the link grabber javascript...")

    print("Automating chapter navigation to capture all signed URLs...")
    
    # Automatically find and click all chapter elements (like 'Clothing and fashion') in the UI
    # This triggers the browser to fetch the signed PDF URLs without you clicking manually.
    pdf_urls = []
    
    while True:
        # Grab current performance logs
        logs = driver.get_log('performance')
        for entry in logs:
            try:
                log_data = json.loads(entry['message'])['message']
                if log_data['method'] == 'Network.requestWillBeSent':
                    url = log_data['params']['request']['url']
                    if 'resource-repository.pearson.com' in url and '.pdf' in url:
                        if url not in pdf_urls:
                            pdf_urls.append(url)
            except Exception:
                continue
                
        # Use JavaScript to click the next unvisited or available chapter/page element in the sidebar/toc
        clicked_new = driver.execute_script("""
            let items = Array.from(document.querySelectorAll('p[title], .tw-truncate, [class*="chapter"], [class*="item"]'));
            for (let item of items) {
                if (!item.getAttribute('data-clicked') && item.offsetParent !== null) {
                    item.setAttribute('data-clicked', 'true');
                    item.click();
                    return true;
                }
            }
            return false;
        """)
        
        if not clicked_new:
            break
        driver.implicitly_wait(1)

    print(f"Captured {len(pdf_urls)} signed URLs via automated navigation.")
    
    if not pdf_urls:
        print("[!] No URLs captured. Exiting.")
        driver.quit()
        return

    os.makedirs(TEMP_DIR, exist_ok=True)
    writer = PdfWriter()
    downloaded_files = []
    
    session = requests.Session()
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'])
        
    try:
        for i, url in enumerate(pdf_urls):
            filename = os.path.join(TEMP_DIR, f"part_{i:03d}.pdf")
            print(f"Downloading [{i+1}/{len(pdf_urls)}]: {url}")
            
            response = session.get(url, timeout=30)
            response.raise_for_status()
            
            with open(filename, 'wb') as pf:
                pf.write(response.content)
                
            downloaded_files.append(filename)
            writer.append(filename)
            
        print(f"Saving merged PDF to {OUTPUT_PDF}...")
        writer.write(OUTPUT_PDF)
        print("Successfully created the full PDF!")
        
    except Exception as e:
        print(f"Error during download/merge: {e}")
    finally:
        driver.quit()
        writer.close()
        for file in downloaded_files:
            if os.path.exists(file):
                os.remove(file)
        if os.path.exists(TEMP_DIR):
            os.rmdir(TEMP_DIR)

if __name__ == '__main__':
    import json
    main()


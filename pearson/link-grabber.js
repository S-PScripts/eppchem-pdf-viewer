// run revise-online-pro.py
// once you're on table of contents run this code below in console/inspect element and wait for it to finish
// if it does nothing make sure it's set as player, not top
// will be merged into revise-online-pro.py later

async function clickAllChapters() {
    // Expand all collapsible category headers
    const expanders = document.querySelectorAll('div[class*="tw-cursor-pointer"], .nav-wrapper-nav [class*="flex"]');
    expanders.forEach(el => { try { el.click(); } catch(e){} });
    
    await new Promise(r => setTimeout(r, 1000));
    
    // Find all topic/page items in the sidebar
    const items = document.querySelectorAll('.row li p, p[title], [class*="truncate"]');
    console.log(`Found ${items.length} items to click.`);
    
    for (let i = 0; i < items.length; i++) {
        try {
            items[i].scrollIntoView();
            items[i].click();
            await new Promise(r => setTimeout(r, 150)); // 150ms delay per page
        } catch(e) {}
    }
    console.log("Finished clicking all items!");
}
clickAllChapters();

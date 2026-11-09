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

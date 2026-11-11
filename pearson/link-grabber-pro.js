// make sure it's set to player, not top

async function clickAllPearsonPages() {
    console.log("🚀 Starting Pearson page clicker...");

    // All regular pages: numbered AND non-numbered
    const normalPages = Array.from(document.querySelectorAll('span[title]'))
        .filter(el => {
            const title = el.getAttribute('title');
            const text = el.innerText.trim().toLowerCase();

            if (!title || text.includes('sign out') ||
                text.includes('log out') || text.includes('account') ||
                text.includes('help')) {
                return false;
            }

            return el.offsetParent !== null;
        });

    // Special chapter pages
    const specialPages = Array.from(document.querySelectorAll('[title]'))
        .filter(el => {
            const title = el.getAttribute('title')?.trim().toLowerCase();

            if (!title || el.offsetParent === null) return false;

            return title.includes('topic overview') ||
                   title.includes('acknowledgement') ||
                   title.includes('acknowledgment');
        });

    // Combine without duplicates
    const items = [...new Set([...normalPages, ...specialPages])];

    console.log(`Regular pages: ${normalPages.length}`);
    console.log(`Special chapters: ${specialPages.length}`);
    console.log(`Total unique items: ${items.length}`);

    console.log("Selected items:", items.map(el => el.getAttribute('title')));

    if (!items.length) {
        console.warn("⚠️ No pages found.");
        return;
    }

    for (let i = 0; i < items.length; i++) {
        try {
            items[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
            items[i].click();

            console.log(`👉 Clicked [${i + 1}/${items.length}]:`,
                items[i].getAttribute('title'));

            await new Promise(resolve => setTimeout(resolve, 500));
        } catch (e) {
            console.warn("Failed:", items[i].getAttribute('title'), e);
        }
    }

    console.log("✅ Finished clicking all Pearson pages!");
}

clickAllPearsonPages();

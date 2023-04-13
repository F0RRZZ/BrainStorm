import {getPaginatorsArgs, getUrlWithNewArgument} from './functions.js';

let indicators = getPaginatorsArgs();

for (let indicator of indicators) {
    let pagesListId = `#pages-list-${indicator}`;
    if (window.location.hash == pagesListId) {
        let pagesList = document.querySelector(pagesListId);
        if (indicators.length > 1) {
            let pageTabId = pagesList.parentNode.parentNode.parentNode.id;
            console.log(`#${pageTabId}-tab`);
            const bsTab = new bootstrap.Tab(`#${pageTabId}-tab`);
            bsTab.show();
        }
        window.location.hash = "";
        window.scrollTo(0, document.body.scrollHeight);
        // let rect = pagesList.parentNode.parentNode.getBoundingClientRect();
        // window.scrollTo(0, rect.top);
    }
    let links = document.querySelectorAll(`${pagesListId} .page-link`);
    for (let link of links) {
        let value = Number(link.id.substring("page-link-".length));
        if (value) {
            link.onclick = function() {
                let newUrl = getUrlWithNewArgument(indicator, value);
                window.location.replace(newUrl + pagesListId);
            }
        }
    }
}

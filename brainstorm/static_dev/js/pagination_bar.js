import {getPaginatorsArgs, getUrlWithNewArgument} from './functions.js';

let indicators = getPaginatorsArgs();

for (let indicator of indicators) {
    let pagesListId = `#pages-list-${indicator}`;
    if (window.location.hash == pagesListId) {
        let pagesList = document.querySelector(pagesListId);
        let pageTabId = pagesList.parentNode.parentNode.parentNode.id;
        if (indicators.length > 1) {
            const bsTab = new bootstrap.Tab(`#${pageTabId}-tab`);
            bsTab.show();
            window.location.hash = `${pageTabId}-tab`;
        } else {
            window.location.hash = "";
            let rect = pagesList.parentNode.parentNode.getBoundingClientRect();
            window.scrollTo(0, rect.top);
        }
        // window.scrollTo(0, document.body.scrollHeight);
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

import {getPaginatorsArgs, getUrlWithNewArgument} from './functions.js';

let indicators = getPaginatorsArgs();

for (let indicator of indicators) {
    let pagesListId = `#pages-list-${indicator}`;
    if (window.location.hash == pagesListId) {
        window.location.hash = "";
        window.scrollTo(0, document.body.scrollHeight);
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

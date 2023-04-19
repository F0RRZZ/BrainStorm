import {getUrlWithNewArgument, getArgumentFromUrl, getSelectedValues, clearFromPaginators, filterSelectByValue} from './functions.js';

function redirect() {
    let selected = getSelectedValues(document.querySelector("#tags-selector > select"));
    let new_url = clearFromPaginators(getUrlWithNewArgument("tags", selected.join(",")));
    window.location.replace(new_url);
}

function reset() {
    let new_url = getUrlWithNewArgument("tags", "");
    window.location.replace(new_url);
}

function filterOptions() {
    let select = document.querySelector("#tags-selector > select");
    let value = document.querySelector("#tags-selector > input").value.toLowerCase();
    filterSelectByValue(select, value);
}

let select = document.querySelector("#tags-selector > select");
let tagsList = document.querySelector("#tags-selector .tags-list")
let selectedValues = getArgumentFromUrl("tags").split(",")

for (let i = 0; i < select.options.length; i++) {
    if (selectedValues.includes(select.options[i].value)) {
        select.options[i].selected = true;
        tagsList.innerHTML += `<div class="badge rounded-pill text-bg-dark mt-1">${select.options[i].text}</div>`;
    }
}
if (tagsList.innerHTML == "") {
    tagsList.innerHTML = "<div><i>---</i></div>"
}
select.allOptions = [].concat(select.options);

document.querySelector("#tags-selector > button").onclick = redirect;
document.querySelector("#tags-selector > div > button").onclick = reset;
document.querySelector("#tags-selector > input").addEventListener("input", filterOptions)

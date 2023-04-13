import {getUrlWithNewArgument, getArgumentFromUrl, clearFromPaginators} from './functions.js';

function redirect() {
    let input = document.querySelector("#search-string > input");
    let newUrl = clearFromPaginators(getUrlWithNewArgument("search", input.value));
    window.location.replace(newUrl);
}

document.querySelector("#search-string > button").onclick = redirect;
document.querySelector("#search-string > input").value = getArgumentFromUrl("search", "")

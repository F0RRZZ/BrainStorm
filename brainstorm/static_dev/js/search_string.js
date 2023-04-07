import {getUrlWithNewArgument, getArgumentFromUrl} from './functions.js';

function redirect() {
    let input = document.querySelector("#search-string > input");
    let new_url = getUrlWithNewArgument("search", input.value);
    window.location.replace(new_url);
}

document.querySelector("#search-string > button").onclick = redirect;
document.querySelector("#search-string > input").value = getArgumentFromUrl("search", "")

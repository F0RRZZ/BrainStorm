import {filterSelectByValue} from './functions.js';

function reset() {
    let select = document.querySelector("#tags-input > select");
    console.log("Reset");
    for (let option of select.options) {
        option.selected = false;
    }
}

function filterOptions() {
    let select = document.querySelector("#tags-input > select");
    let value = document.querySelector("#tags-input > input").value.toLowerCase();
    filterSelectByValue(select, value);
}

document.querySelector("#tags-input > button").onclick = reset;
document.querySelector("#tags-input > input").addEventListener("input", filterOptions)

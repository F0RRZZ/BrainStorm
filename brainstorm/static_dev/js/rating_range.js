import {getColorFromNumber, clearFromNonVisible} from './functions.js';

function handleRangeChange(addValue=true) {
    let range = document.getElementById('rating-range')
    let rangeValue = range ? range.value : 0;
    let displays = document.querySelectorAll('.bs-rating-show');
    for (let display of displays) {
        if (display.id == 'range-value-display' && addValue) {
            display.innerHTML = rangeValue;
        }
        let rating = Number(display.innerHTML.replace(",", "."));
        if (isNaN(rating)) {
            continue;
        }
        let color = getColorFromNumber(rating);
        display.style.borderColor = color;
        display.style.boxShadow = "0 0 3px 0.2rem " + color + "b5";
    }
}

let addValueElement = document.getElementById('set-range-value-in-start');
handleRangeChange(Boolean(clearFromNonVisible(addValueElement.innerHTML)));
addValueElement.innerHTML = ""

let range = document.getElementById('rating-range');
if (range) {
    range.addEventListener("input", handleRangeChange);
}

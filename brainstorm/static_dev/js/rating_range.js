import {getColorFromNumber} from './functions.js';

function handleRangeChange() {
    let rangeValue = document.getElementById('rating-range').value;
    let display = document.getElementById('range-value-display');
    display.innerHTML = rangeValue;

    let color = getColorFromNumber(rangeValue);
    display.style.borderColor = color;
    display.style.boxShadow = "0 0 3px 0.2rem " + color + "b5";
}

handleRangeChange();
document.getElementById('rating-range').addEventListener("input", handleRangeChange);

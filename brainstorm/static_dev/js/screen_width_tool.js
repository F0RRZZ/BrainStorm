/*
HTML:

<div id="screen-width-display"></div>

Tool for view screen width
*/
display = document.getElementById("screen-width-display");
display.style.position = "fixed";
display.style.left = "1vw";
display.style.bottom = "1vh";
display.style.border = "solid yellowgreen 0.2vw";
display.style.backgroundColor = "white";
display.style.width = '19vw';
display.style.height = '8vh';
display.style.fontSize = "4vh";
display.style.textAlign = "center";

function updateDisplay() {
    display = document.getElementById("screen-width-display");
    display.innerHTML = document.documentElement.scrollWidth + "px";
}

updateDisplay();
window.addEventListener('resize', updateDisplay, true);

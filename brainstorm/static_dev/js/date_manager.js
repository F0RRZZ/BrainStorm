let clientDate = new Date();
let [year, month, dat, hour, minute, second] = document.getElementById("liz-sh-currentServerDate").innerHTML.split("-")
let serverDate = new Date(year, month - 1, dat, hour, minute, second);

let date;
if (Math.abs(clientDate.getTime() - serverDate.getTime()) > 24 * 60 * 60 * 1000) {
    date = serverDate;
    console.log("Use server date");
} else {
    date = clientDate;
    console.log("Use client date");
}

let dateTag = document.getElementById("footerDateSpan");
dateTag.innerHTML = date.getFullYear();

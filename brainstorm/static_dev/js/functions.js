`use strict`

export function normalizeUrl(url) {
    while (url.includes("??")) {
        url = url.replace("??", "?");
    }
    if (!url.includes("?")) {
        url += "?";
    }
    return url;
}

export function getUrlWithNewArgument(arg, value, url=window.location.href) {
    let baseUrl, argsString;
    [baseUrl, argsString] = normalizeUrl(url).split("?");
    let newArgs = [];
    for (let argument of argsString.split("&")) {
        if (!argument.startsWith(`${arg}=`) && argument) {
            newArgs.push(argument);
        }
    }
    if (value) {
        newArgs.push(`${arg}=${encodeURIComponent(value)}`);
    }
    return `${baseUrl}?${newArgs.join("&")}`
}

export function getArgumentFromUrl(arg, default_="", url=window.location.href) {
    let baseUrl, argsString;
    [baseUrl, argsString] = normalizeUrl(url).split("?");
    for (let argument of argsString.split("&")) {
        let param, value;
        [param, value] = argument.split("=");
        if (param == arg) {
            return decodeURIComponent(value);
        }
    }
    return default_;
}

export function getSelectedValues(select) {
    return Array.from(select.options).filter(option => option.selected).map(option => option.value);
}

export function getColorFromNumber(number) {
    let color;
    if (number <= 3) {
        color = "#de1212";
    } else if (number <= 6) {
        color = "#debc12";
    } else if (number <= 9) {
        color = "#5ebf13";
    } else if (number <= 10) {
        color = "#00d0ff";
    }
    return color;
}

export function clearFromNonVisible(string) {
    return string.replace(/( )/gm, '').replace(/(\r\n|\n|\r)/gm, '');
}

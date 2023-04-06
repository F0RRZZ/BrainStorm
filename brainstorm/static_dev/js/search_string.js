function redirect() {
    let input = document.querySelector("#search-string > input");
    let current_url = window.location.href;
    let new_url;
    if (!current_url.includes("?")) {
        new_url = current_url + "?search=" + input.value;
    } else {
        let args_string;
        while (current_url.includes("??")) {
            current_url = current_url.replace("??", "?");
        }
        [new_url, args_string] = current_url.split("?");
        let new_args = [];
        for (let arg_string of args_string.split("&")) {
            let param, value;
            [param, value] = arg_string.split("=")
            if (param != "search") {
                new_args.push(arg_string);
            }
        }
        if (input.value) {
            new_args.push("search=" + input.value);
        }
        new_url += "?" + new_args.join("&");
    }
    console.log(input.value, new_url);
    window.location.replace(new_url);
}

document.querySelector("#search-string > button").onclick = redirect;

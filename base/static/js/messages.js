$.jGrowl.defaults.position = 'center'
function show_message(tag, message) {
    var class_name = "alert alert-"
    if (tag == "error")
        class_name = class_name + "danger"
    else
        class_name = class_name + tag
    $.jGrowl(message, {
            openDuration: 700,
            closeDuration: 1000,
            life: 3000,
            group: class_name
        }
    );
}


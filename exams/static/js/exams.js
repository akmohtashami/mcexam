var choice_changed = false;
$(document).ready(function() {
    $('.choice').on("click", function (event) {
        choice_changed = true;
        var radio_str = "[data-identifier='" + $(this).data("correspond") + "']";
        var obj = $(document).find(radio_str);
        var currently_selected = $("input[name='" + $(obj).prop("name") + "']:checked");
        if (currently_selected.length && currently_selected != obj) {
            var selected_label = $(document).find("[data-correspond='" + $(currently_selected).data("identifier") + "']");
            selected_label.removeClass("marked");
        }
        var current = $(obj).prop("checked");
        $(obj).prop("checked", !current);
        if (!current)
            $(this).addClass("marked");
        else
            $(this).removeClass("marked");
    });
    $('.choice.locked').unbind("click");
    $("[data-delete=true]").click(function(e) {
        return confirm(gettext("Please confirm to continue"));
    });
});
$(window).on('beforeunload', function(e) {
    if (choice_changed) {
        return ' ';
    }
});
$(document).on("submit", "form", function(event){
    // disable unload warning
    $(window).off('beforeunload');
});


/*
$("[data-delete=true]").click(function(e){
    e.preventDefault();
    var elem = $(this);
    var buttons = {};
    buttons[gettext("Yes")] = function(){
        $(this).dialog("close");
        window.location = $(elem).prop("href");
    };
    buttons[gettext("No")] = function(){
        $(this).dialog("close");
    };
    $("<div></div>").appendTo("body")
        .html("<div>" + gettext("Are you sure about deleting this participant?") + "</div>")
        .dialog({
            resizable: false,
            height:200,
            modal: true,
            buttons: buttons
        });
});
*/

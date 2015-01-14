$('.choice').on("click", function(event){
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
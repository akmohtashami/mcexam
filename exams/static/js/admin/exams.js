function renumerate(objs){
    for (i = 0; i < objs.length; i++){
        $("#id_" + objs[i] + "-order").prop("value", i + 1);
    }
}

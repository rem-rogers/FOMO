$(function(context){
    return function() {
        // $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pnum + "/")
        $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pnum + "/")
        console.log(context.category);
        console.log(context.pnum);
        // $('#next_page').load()
        //
        // $('#previous_page').load()
    }
}(DMP_CONTEXT.get()));

$(function(context){
    return function() {
        // $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pnum + "/")
        $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pNum)
        console.log(context.category);
        console.log(context.pNum);

        $('#next_page').click(function(){
            if (context.pNum < context.pMax) {
                context.pNum++;
                $("#currentPage").text(context.pNum);
                $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pNum)
            }
            });

        $('#previous_page').click(function() {
            if (context.pNum >1) {
            context.pNum--;
            $("#currentPage").text(context.pNum);
            $("#catalog").load("/catalog/index.products/" + context.category + "/" + context.pNum)
             }
            });




        // $('#previous_page').load()
    }
}(DMP_CONTEXT.get()));

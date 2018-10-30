$(function () {
    $("#inputGroupFile02").onAddItem = function () {
        console.log("choose")
    };
    $("#upload_file").bind("click", function () {
        $("#upload_form").submit();
    })
});
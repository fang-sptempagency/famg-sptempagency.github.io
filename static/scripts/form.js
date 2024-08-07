$(function() {
    $('.next-photo-btn').on('click', () => {
        //http通信開始
        $.ajax({
            url: "http://localhost:8080/",
            dataType: "json",
            type: "POST"
        }).done(function(res) {
            console.log(res)
        }).fail(function(res) {
            console.log(res)
        });
    });
});
$(document).ready(function () {
    eng_vie = new eng_vie();
});

class eng_vie {
    constructor() {
        var x = 0;
        $('.youranswer').keyup(function (e) {
            if (e.keyCode == 13) {
                var youranswer = $(this)[0].value;
                var correct = $(this).attr('id');
                $(this).attr('disabled','disabled');
                if (youranswer === correct)
                    x = x + 1;
                    $('.score')[0].innerHTML = "Score: " + x;
            }
        });
    }
}
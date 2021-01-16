$(document).ready(function () {
    admin = new admin();
});

class admin {
    constructor() {
         $(document).on("click", ".btn.edit", this.openDialogedit);
         $(document).on("click", ".dialog .btn.btn-success", this.editWord);
    }
    openDialogedit(){
        if($('.btn.edit').hasClass('fixing')){
            $('.btn.edit').removeClass('fixing');
        }
        $(this).addClass('fixing');
        var word_origin = $(this).parent().parent().children();
        var dialog_input = $('.dialog input.form-control')
        dialog_input[0].value = word_origin[0].innerText;
        dialog_input[1].value = word_origin[1].innerText;
        $(".dialog").dialog({
            width: 400,
            height: 250,
        })
    }
    editWord(){
        var edit = $('.btn.edit.fixing').attr('id');
        var dialog_input = $('.dialog input.form-control')
        $.ajax({
			url: '/update/' + edit,
            type: 'POST',
			data: {
			    en : dialog_input[0].value,
                vn : dialog_input[1].value
            }})
            .done( function (data){
                if(data.error){
                    alert("lỗi")
                }
                else {
                    $(".dialog").dialog('close')
                    $.ajax({
                        url: '/updatetabledata/' + edit,
                        type: 'GET',
                        async: false,
                        success: function (res) {
                            var word_origin = $('.btn.edit.fixing').parent().parent().children();
                            word_origin[0].innerText = res.en
                            word_origin[1].innerText = res.vn
                        }
                    })
                }
                }
            )
    }
}
$(document).ready(function(){
//  Check Radio-box
    $('.rating input:radio').attr('checked', false);
    $('.rating input').click(function () {
        $('.rating span').removeClass('checked');
        $(this).parent().addClass('checked');
        var userRating = this.value;
        var sendt = ('You have given this quiz a' + userRating + 'out of 5. &#10; Takk for din rating.');
        $('#takk').innerHTML = sendt;
        $('#takk').show();
    });

    $('input:radio').change(
    function(){

        $('.rating span').removeClass('checked');


    });
});

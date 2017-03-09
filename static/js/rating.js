$(document).ready(function(){
//  Check Radio-box
    $('.rating input:radio').attr('checked', false);
    $('.rating input').click(function () {
        $('.rating span').removeClass('checked');
        $(this).parent().addClass('checked');
    });

    $('input:radio').change(
    function(){
        var userRating = this.value;
        var sendt = ('You have given this quiz a' + userRating + 'out of 5. &#10; Takk for din rating.');
        $('.rating span').removeClass('checked');
        $('#takk').innerHTML = sendt;
        $('#takk').show();

    });
});

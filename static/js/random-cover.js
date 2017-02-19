/**
 * Created by Eier on 19.02.2017.
 */
$(document).ready(function(){
var images=['../img/cover.png',
            '../img/cover2.jpeg',
            '../img/cover3.png',
            '../img/cover4.png',];

var randomNumber = Math.floor(Math.random() * images.length);
var bgImg = 'url(' + images[randomNumber] + ')';

$('body').css({'background':bgImg, 'background-size':'cover', });

});
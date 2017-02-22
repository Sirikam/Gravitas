/**
 * Created by Eier on 19.02.2017.
 */
function randomcover(){
    var images = ['cover.png', 'cover2.jpeg', 'cover3.png', 'cover4.png'];
    document.getElementsByTagName("body")[0].style.backgroundImage = 'url(../img/' + images[Math.floor(Math.random() *  images.length)] + ');';
}
randomcover();
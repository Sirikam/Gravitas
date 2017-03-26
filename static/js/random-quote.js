/**
 * Created by Eier on 19.02.2017.
 */
document.addEventListener("DOMContentLoaded", function quotes() {
	var liste = ["Keep up the good work, {{ user.username }} !", "'Learning is not a spectator sport.'</br> -D. Blocher", "'It is wiser to find out than to suppose.'</br> -Mark Twain", "'Education is what survives when what has been learned has been forgotten.'</br> –B. F. Skinner", "'Experience: that most brutal of teachers. But you learn, my God do you learn.'</br> –C.S. Lewis", "'The purpose of learning is growth, and our minds, unlike our bodies, can continue growing as long as we live.'</br> –Mortimer Adler", "'Learning is like rowing upstream, not to advance is to drop back.'</br> -Chinese Proverb"];
	var random = liste[Math.floor(Math.random()*liste.length)];
	document.getElementById("quote").innerHTML = random;
});
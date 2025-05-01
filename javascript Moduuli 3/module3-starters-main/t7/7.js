const img = document.querySelector('#target');
const pic = document.querySelector('#trigger');
function on() {
    img.src = "img/picB.jpg";}
function off() {
    img.src = "img/picA.jpg";}

pic.addEventListener('mouseenter', on);
pic.addEventListener('mouseleave', off);
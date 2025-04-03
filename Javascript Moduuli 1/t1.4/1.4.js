name = prompt("Tell me your name: ")
number = Math.random() * 4
document.querySelector('#target').innerHTML=(number)
if (0<number, number< 1){
    document.querySelector('#target').innerHTML=(name + ", you're an Gryffindor")
} else if (1<number,number<2){
    document.querySelector('#target').innerHTML=(name + ", you're an Slytherin")
} else if (2<number,number<3){
    document.querySelector('#target').innerHTML=(name +", youre an Hufflepuff")
} else {
    document.querySelector('#target').innerHTML=(name+", you're an Ravenclaw")
}
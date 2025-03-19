name = prompt("Tell me your name: ")
number = Math.random() * 4
console.log(number)
if (0<number, number< 1){
    console.log(name + ", you're an Gryffindor")
} else if (1<number,number<2){
    console.log(name + ", you're an Slytherin")
} else if (2<number,number<3){
    console.log(name +", youre an Hufflepuff")
} else {
    console.log(name+", you're an Ravenclaw")
}
let numerot = []
for(;;){
    let numero = +prompt("kerro minulle numero: ")
    if (numero === 0){break}
    numerot.push(numero)


}
numerot.sort((a,b) => b-a);
console.log(numerot)
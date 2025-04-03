let numerot = [2,3,4,5,6,7,9,100,1000]
quickfix = true
numero = 8
for(;;) {
    if (quickfix === false) {
        break
    }

    console.log("test1")
    for (let i = 0; i < numerot.length; i++) {

        if (numero == numerot[i]) {
            quickfix = false
            break

        }
    }
numerot.push(numero)
}
console.log("Hei, laitoit saman numeron 2 kertaa, tässä numerosi pienimmästä suurimpaan")
console.log(numerot)
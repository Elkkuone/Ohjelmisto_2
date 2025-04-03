let numerot = []
quickfix = true

for(;;) {
    numero = +prompt("hei, kerro uusi numero")
    for (let i = 0; i < numerot.length; i++) {

        if (numero == numerot[i]) {
            quickfix = false
            break
        }
    }
if (quickfix === false) {break}
else{numerot.push(numero)}
}
document.querySelector('#target').innerHTML=("Hei, laitoit saman numeron 2 kertaa, tässä numerosi pienimmästä suurimpaan")
numerot.sort((a,b)=> a-b)
document.querySelector('#target').innerHTML=(numerot)
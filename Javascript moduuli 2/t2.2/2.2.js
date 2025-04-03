numero = +prompt("kerro osallistujien määrä")
nimet = []
for (let i=1;i-1<numero;i++){
    nimi = prompt("kerro "+i+" osallistujan nimi: ")
    nimet = nimet +('<ol>'+"Nimi: "+nimi+" Numero: " +i+'</ol>')
}
document.querySelector('#target').innerHTML=nimet
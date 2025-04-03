let koirat = []

for (let i = 0; i < 6; i++) {
    let nimi = prompt("kerro " + (i + 1) + " koiran nimi: ")
    koirat.push(" "+nimi)
}
koirat.reverse()
document.querySelector('#target').innerHTML=koirat
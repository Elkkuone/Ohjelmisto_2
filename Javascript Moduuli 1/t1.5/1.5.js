vuosi = prompt("hei hei, kerro minulle vuosi ja lasken onko se karkausvuosi: ")
testi = 0

if (vuosi % 4 === testi) {
    if (vuosi % 100 === testi) {
        if (vuosi % 400 === testi) {
            document.querySelector('#target').innerHTML=("tämä vuosi on karkausvuosi")
        } else
            document.querySelector('#target').innerHTML=("tämä vuosi ei ole karkausvuosi")
    } else
        document.querySelector('#target').innerHTML=("tämä vuosi on karkausvuosi")
} else
    document.querySelector('#target').innerHTML=("tämä vuosi ei ole karkausvuosi")



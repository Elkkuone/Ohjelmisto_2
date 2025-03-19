vuosi = prompt("hei hei, kerro minulle vuosi ja lasken onko se karkausvuosi: ")
testi = 0

if (vuosi % 4 === testi) {
    if (vuosi % 100 === testi) {
        if (vuosi % 400 === testi) {
            console.log("tämä vuosi on karkausvuosi")
        } else
            console.log("tämä vuosi ei ole karkausvuosi")
    } else
        console.log("tämä vuosi on karkausvuosi")
} else
    console.log("tämä vuosi ei ole karkausvuosi")



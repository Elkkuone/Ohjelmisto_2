'use strict';
const names = ['John', 'Paul', 'Jones'];
for (let i=0;i<names.length;i++){
    names[i] = ("<li>"+names[i]+"</li>")
    console.log(names[i])
}


 const para = document.createElement("ul");
para.innerHTML =names.join("");
document.getElementById("target").appendChild(para);

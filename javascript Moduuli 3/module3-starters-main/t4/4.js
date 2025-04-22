'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const target = document.getElementById("target");

for (let i=0;i<students.length;i++){
  const para = document.createElement('option')
  para.value = students[i].id
  para.innerHTML = students[i].name
  target.appendChild(para)
}


let body=document.getElementsByTagName("body")
console.log(body)
let space = " "
let i=0

for (let i=0;i<7; i++){
    let span = document.createElement('span')
    span.id= i
    document.body.appendChild(span)
    let br=document.createElement('br')
    document.body.appendChild(br)
}

let first_row=document.getElementById("0")
first_row.textContent=" *** ";
first_row.insertAdjacentHTML('beforebegin', "&nbsp;")
first_row.insertAdjacentHTML('afterend', "&nbsp;")

let second_row= document.getElementById("1")
let third_row=document.getElementById("2")

second_row.textContent=" * "
second_row.insertAdjacentHTML('afterend', "&emsp; *")

third_row.textContent=second_row.textContent
third_row.insertAdjacentHTML('afterend', "&emsp; *")

let fourth_row=document.getElementById("3")
fourth_row.textContent=" ***** "

let fifth_row=document.getElementById("4")
let sixth_row=document.getElementById("5")
let seventh_row= document.getElementById("6")

fifth_row.textContent=sixth_row.textContent=seventh_row.textContent=second_row.textContent

fifth_row.insertAdjacentHTML('afterend', "&emsp; *")
sixth_row.insertAdjacentHTML('afterend', "&emsp; *")
seventh_row.insertAdjacentHTML('afterend', "&emsp; *")

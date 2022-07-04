//1
let form = document.querySelector('form');
console.log(form);
//2

let first_name=document.getElementById("fname");
let last_name=document.getElementById("lname");
let submit=document.getElementById("submit");

console.log(first_name, last_name, submit);
//3
let f_name=document.getElementsByName("fname");
let l_name=document.getElementsByName("lname");
console.log(f_name, l_name);

//4
let button=document.getElementById("submit");
button.addEventListener('click', prevent);

function prevent() {
    event.preventDefault(); // this is good so the link is not connected before checking that all relevant fields are filled in
    
    let input_val_1=document.querySelector('input').value;
    let input_val_2=document.querySelector('#lname').value;
    console.log(input_val_1);
    console.log(input_val_2);

    while (input_val_1.length==0 || input_val_2.length==0){
        alert("Fill out form");
    }

    if (input_val_1.length!=0 && input_val_2.length!=0){
        let li_1= document.createElement("LI");
        li_1.append(input_val_1);

        let li_2=document.createElement("LI");
        li_2.append(input_val_2);

        console.log(li_1, li_2);

        let root = document.getElementsByClassName('usersAnswer')[0];
        root.appendChild(li_1);
        root.appendChild(li_2);
    }

}


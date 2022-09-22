
let exercise_3=document.getElementsByTagName("div");
//2
let new_id=exercise_3[0].setAttribute("id","socialNetworkNavigation");
console.log(new_id);
//3

let ul_1=document.getElementsByTagName('ul');
let new_li=document.createElement('li');
new_li.textContent="Logout";
ul_1[0].appendChild(new_li);
console.log(new_li);


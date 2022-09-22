let exercise_1= document.getElementsByTagName("div");
console.log(exercise_1);
//2
let new_name=exercise_1[0].nextElementSibling.children[1].textContent="Richard";
console.log(new_name);

//3
let new_name_3=exercise_1[0].nextElementSibling.children[0].textContent="David";
let new_name_3a=exercise_1[0].nextElementSibling.nextElementSibling.children[0].textContent="David";

//4
let Sarah=exercise_1[0].nextElementSibling.nextElementSibling.children[1];
let remove_Sarah=Sarah.remove();
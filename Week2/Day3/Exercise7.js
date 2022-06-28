let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let unordered_array=[];
let ordered_list="";

for (i in names){
    let first_letter=names[i][0];
    unordered_array.push(first_letter);
}

let ordered_array=unordered_array.sort();

let secrect_society=ordered_array.join(""); 

console.log(secrect_society);

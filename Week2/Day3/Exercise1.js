
let people = ["Greg", "Mary", "Devon", "James"];
// 1
people.shift();

console.log(people);
// 2 & 3
people[2]="Jason";
people[3]="David";

// 4
console.log(people.indexOf("Mary"));
console.log(people)
// 5
let sliced_array = people.slice(1,3);
console.log(sliced_array);
//6
console.log(sliced_array.indexOf("Foo"));
// 7
let last=sliced_array.length-1;
console.log(last);

// Part 2
// 1.

for (i in people){
    console.log(people[i]);
}
for (i in people){
    console.log(people[i]);
    if(people[i]=="Jason"){
        break;
    }
}
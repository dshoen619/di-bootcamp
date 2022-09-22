let input= prompt("enter words seperated by commas");

let input_array=input.split(',');

var max_str = input_array[0].length;
var ans = input_array[0];
for (var i = 1; i < input_array.length; i++) {
    var maxi = input_array[i].length;
    if (maxi > max_str) {
        ans = input_array[i];
        max_str = maxi;
    }
}
console.log(max_str);

let horizontal_stars="";
while (i<max_str){
    i++;
    horizontal_stars+="*";
}

console.log(horizontal_stars)
for (i in input_array){
    console.log("* "+input_array[i]+" *");
}
console.log(horizontal_stars);


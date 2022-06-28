// 1

let number= prompt("Please enter a number");

let prompt_type = typeof(number);

//2
number_conv=parseInt(number);
console.log(number_conv);

while (isNaN(number_conv)){
    alert("Enter a number!");
    let number=prompt("Please enter a number");
    number_conv=parseInt(number);
}
while(number_conv<10){
    let new_number=prompt("Please enter a new number");
    number_conv=parseInt(new_number);
}

alert("congrats!")
        




let bottles_start= prompt("How many bottles");

let prompt_type = typeof(bottles_start);

//2
number_conv=parseInt(bottles_start);
console.log(bottles_start);

while (isNaN(number_conv)){
    alert("Enter a number!");
    let bottles_start=prompt("How many bottles to start with? Must be a number.");
    number_conv=parseInt(bottles_start);
}

let bottles_taken_down=0;

while(number_conv>bottles_taken_down){
    bottles_taken_down+=1;
    console.log(number_conv+" bottles of beer on the wall");
    console.log(number_conv+" bottles of beer");
    console.log("Take "+bottles_taken_down+ " down, pass it around");
    number_conv=number_conv-bottles_taken_down;
    console.log(number_conv+" bottles of beer on the wall");

}

console.log(number_conv+" bottles of beer on the wall");
console.log(number_conv+" bottles of beer");
console.log("Take "+number_conv+ " down, pass it around");
console.log("0 bottles of beer on the Wall!");

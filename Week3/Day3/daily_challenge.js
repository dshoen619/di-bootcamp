let counter=0
let letter_array=[]
function lettercheck(){
    event.preventDefault();
    let letter=document.getElementById("input").value;
    let one_letter= Array.from(letter)[counter];
    // if (one_letter.toUpperCase()!=one_letter.toLowerCase()){
    if (one_letter='a'){
        letter.slice(counter);
    }
    counter+=1;
    console.log(one_letter)
    console.log(letter);


}







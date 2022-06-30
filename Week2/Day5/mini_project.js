function playTheGame(){
   let play_q=confirm("Would you like to play?");
   if (play_q==false){
       alert("No Problem, Goodbye");
   }
   else if (play_q==true){
       let number_q=prompt("Please enter a number between 0 and 10");
       let number_conv=parseInt(number_q);
       if (isNaN(number_conv)==true){
           alert("Sorry its not a number, Goodbye");}
       else if(number_conv<0 || number_conv>10){
           alert("Sorry its not a good number, Goodbye");}
       else {let computerNumber=Math.floor(Math.random() * 11);
            compareNumbers(number_conv,computerNumber);}
   }

}

function compareNumbers(userNumber,computerNumber){
    console.log(computerNumber);
    let guess_1=0;
    let guess_2=0;
    // if(userNumber==computerNumber){
    //     console.log("Winner");
    //     alert("Winner");
    //    return;
    
    while(userNumber!=computerNumber && guess_1+guess_2<3){
        console.log("guess_1 ", guess_1);
        console.log("guess_2 ", guess_2);

        if (userNumber>computerNumber){
            userNumber=parseInt(prompt("Your number is bigger than computer, guess again"));
            guess_1+=1;
        }
        else if (userNumber<computerNumber){
            userNumber=parseInt(prompt("Your number is smaller than computer, guess again"));
            guess_2+=1;
        }
        }
    if(userNumber==computerNumber){
        alert("Winner");}
    else{
        alert("out of chances");
}

}


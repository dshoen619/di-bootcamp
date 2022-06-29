// 1
var tip;

function calculateTip(){
    let bill_string = prompt("John, how much was the bill?");
    let bill = Number(bill_string);
    if (bill<50){
         tip=0.2*bill;}
    else if (bill>=50 && bill<=200){
         tip=0.15*bill;}
    else if (bill>200){
         tip=0.1*bill;}
    let total = bill+tip;
    console.log(bill,tip,total);
}

calculateTip();


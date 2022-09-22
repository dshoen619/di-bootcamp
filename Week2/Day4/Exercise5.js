function changeEnough(itemPrice, amountOfChange){
        let quarters= amountOfChange[0]*0.25;
        let dimes= amountOfChange[1]*0.1;
        let nickels=amountOfChange[2]*0.05;
        let pennies=amountOfChange[3]*0.01;
        let sum= quarters+dimes+nickels+pennies;
        if (sum>=itemPrice){
            return true;
        }
        else if (sum<itemPrice){
            return false;
        }

}

console.log(changeEnough(0.75, [0,0,20,5]));
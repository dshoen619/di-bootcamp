let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList=["banana", "orange", "apple"];

function mybill(){
    for (item in shoppingList){
        let fruit= shoppingList[item];
        if (stock[fruit]!=0){
            let price= prices[fruit];
            console.log(fruit, price);
            //bonus
            stock[fruit]=stock[fruit]-1;
            console.log(stock);}
        else if (stock[fruit]==0){
            console.log("Out of stock");
        }

    }
}

mybill();
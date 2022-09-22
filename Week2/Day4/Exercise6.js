function hotelcost(){
    let number_nights=prompt("How many nights would you like to stay?")
    number_conv=parseInt(number_nights);
    while (isNaN(number_conv)){
        number_nights=prompt("How many nights would you like to stay?");
        number_conv=parseInt(number_nights);}
    let hotel_price=140*number_conv;
    return hotel_price;
}

function planeRideCost(){
    let destination=prompt("Where are you going?");
    let destination_number_check=parseInt(destination);
    while (isNaN(destination_number_check)==false){
        destination=prompt("Where are you going?");
        destination_number_check=parseInt(destination);}
    if (destination.toLowerCase()=="london"){
        airfare=183;}
    else if(destination.toLowerCase()=="paris"){
        airfare=220;}
    else { airfare=300;}
    return airfare;  
}

function rentalCarcost(){
    let car_days=prompt("How many days would you like to rent a car?");
    number_conv_car=parseInt(car_days);
    while (isNaN(number_conv_car)){
        car_days=prompt("How many days would you like to rent a car?");
        number_conv_car=parseInt(car_days);}
    if (number_conv_car<=10){
        car_cost=40*number_conv_car;}
    else if(number_conv_car>10){
        car_cost=0.9*40*number_conv_car;
    }
    return car_cost

}


function totalVacationcost(){
    console.log("The hotel costs $"+hotelcost()+", The plane costs $"+planeRideCost()+", The car costs $"+rentalCarcost());
}   
totalVacationcost();
// 1


function isDivisible(){
    let i=0;
    let count_23=0;
    while (i<500){
        i++;
        if (i%23==0){
            console.log(i);
            count_23+=i;
        }

    }
    console.log(count_23);
}

isDivisible();

//Bonus
function isDivisible(divisor){
    let i=0;
    let count_divisor=0;
    while (i<500){
        i++;
        if (i%divisor==0){
            console.log(i);
            count_divisor+=i;
        }

    }
    console.log(count_divisor);
}

isDivisible(23);

array=['*','*','*'];

let pattern_string="";
for (i in array){
    if (i==2){
        break;}
    for (j in array){
        pattern_string+=array[j];
        console.log(pattern_string);

    }
}


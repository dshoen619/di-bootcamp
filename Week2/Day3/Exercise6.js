let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
let string="";
new_string="";
for (i in details){
    let string=(i+" "+details[i]+" ");
    new_string+=string;
}

console.log(new_string);



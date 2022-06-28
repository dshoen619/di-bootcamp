// 1
let colors = ["blue", "green", "red", "white", "orange"];
// 2
for (i in colors){
    let index_number= Number(i)+1;
    console.log("My #"+index_number+" choice is "+colors[i]);
}
//2 bonus
let suffix_array=["st","nd","rd","th","th"]

for (i in colors,suffix_array){
    let number_index=Number(i)+1;
    console.log("My "+number_index+suffix_array[i]+" choice is "+colors[i]);
}
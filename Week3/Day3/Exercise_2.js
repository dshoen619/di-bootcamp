let move_counter=0;
let move_counter_2=0;
function moveright(){
    move_counter+=1;
    document.getElementById('animate').style.left=move_counter+"px";
    // console.log(move_counter)

}
function myMove(){
    move_counter_2+=1
    let move=setInterval(moveright,1);
    console.log(document.getElementById('animate').style.left.textContent)
    if (document.getElementById('animate').style.left=="400px"){
        clearInterval(move);
    }

}

// function stop(){
//     if (document.getElementById('animate').style.left=="400px"){
//         clearInterval
//     }
// }

let button=document.querySelector("p");
button.addEventListener('click', myMove);







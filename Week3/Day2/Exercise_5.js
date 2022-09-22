let button = document.querySelector('button');

function clickon(){
    document.body.style.backgroundColor="black";
}
function change_size(){
    button.style.width="800px";
}
function hidden(){
    button.style.visibility="hidden";
}
function visible(){
    button.style.color="blue";
}

button.addEventListener('click',clickon);
button.addEventListener('dblclick',change_size);
button.addEventListener('mouseout',hidden);
button.addEventListener('mouseover',visible);


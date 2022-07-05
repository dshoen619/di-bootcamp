//1
function helloworld(){
    alert("Hello, World");
}

setTimeout(helloworld,2000);
//2
let new_para_count=0;
function newParagraph(){
    let hello_p=document.createElement('p');
    hello_p.innerHTML='Hello, World';
    let root = document.querySelector('#container');
    root.appendChild(hello_p);
    new_para_count+=1;
    console.log(new_para_count);
    if (new_para_count>=5){
        clearInterval(new_para);
    }


}

setTimeout(newParagraph,2000);

let new_para=setInterval(newParagraph,2000);
//3
function stopinterval(){
    clearInterval(new_para);
}

let button=document.getElementById("clear");
button.addEventListener('click', stopinterval);


//4
// clear interval solution added to newParagraph function





//1
let header_1=document.querySelector('h1');
console.log(header_1);

// 2
let last_elem = document.querySelector('article').lastElementChild;
console.log(last_elem);
last_elem.remove();

//3
h2=document.querySelector('h2');
h2.addEventListener('click',RespondClick);

function RespondClick(){
    document.querySelector("h2").style.backgroundColor = "red"; 
}
//4
h3=document.querySelector('h3');
h3.addEventListener('click', RespondClick_hide);

function RespondClick_hide(){
    document.querySelector('h3').style.display="none";
}
//5

let bold_button =document.createElement("button");
bold_button.innerHTML="Click to make paragraph text bold";
document.querySelector("article").appendChild(bold_button);

bold_button.addEventListener('click',MakeBold);

function MakeBold(){
    //document.querySelectorAll('p').style.fontWeight="900";
    //document.querySelector("p").style.fontWeight = "bold";

    let all_ps = document.querySelectorAll('p');
    for (let i=0; i<all_ps.length;i++){
        all_ps[i].style.fontWeight="bold";
    }

}





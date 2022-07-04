var allBoldItems="";

function getBold_items(){
    for (let i=0; i<6;i++){
        let all_strong=document.getElementsByTagName('strong')[i].innerHTML;
        //console.log(all_strong);
        allBoldItems+=" "+(all_strong);  
    }
    console.log(allBoldItems);
}

getBold_items()

function highlight(){
    for (let i=0; i<6;i++){
        let all_strong=document.getElementsByTagName('strong')[i];
        all_strong.style.color="blue";
    }
}

function return_normal(){
    for (let i=0; i<6;i++){
        let all_strong=document.getElementsByTagName('strong')[i];
        all_strong.style.color="black";

}
}
let x = document.querySelector('p');


x.addEventListener('mouseover', highlight);
x.addEventListener('mouseout', return_normal);
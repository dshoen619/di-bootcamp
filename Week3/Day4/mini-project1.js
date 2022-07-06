let counter=0;
let sidebar=document.getElementsByClassName('color-palette')[0];
let root = document.getElementsByClassName("grid-container")[0];
let button=document.getElementById("button");
let boxes=[]
let color;
let mouse_count=0;
let mouse_down=false;

document.body.addEventListener('mousedown',function(){
    mouse_down=true;
})
document.body.addEventListener('mouseup',function(){
    mouse_down=false;
})

while (counter<3000){
    let box = document.createElement('div');
    box.className='grid-item';
    box.id='box'
    boxes.push(box)
    root.appendChild(box);
    box.addEventListener('mousedown', function(){
        if(mouse_down){
            box.style.backgroundColor=color
        }
    })

    box.addEventListener('mouseover', function(){
        if (mouse_down){
            box.style.backgroundColor=color    
        }
    })


    counter+=1
}
 
button.addEventListener('click',function(){
    for (x in boxes){
        boxes[x].style.backgroundColor=""
    }
})

    

function clear(){

}

function generateColors(){
    let letters='0123456789ABCDEF';
    let color='#';
    for (let i=0; i<6;i++){
        color +=letters[Math.floor(Math.random()*16)];
    }
    return color;
}

let color_col=3;
let color_rows=8;
let color_count=color_rows*color_col;

for (let i =0; i<color_count; i++){
    let div = document.createElement('div');
    div.className='Color';
    div.id='Color-ID'+(i+1);
    div.addEventListener('click',function(){
        color=div.style.backgroundColor;
        console.log(color)
    })
    div.style.backgroundColor=generateColors();
    sidebar.appendChild(div)
} 
// for (let i =0; i<color_count; i++){
//     id='Color-ID'+(i+1)
//     element_color=document.getElementById(id).style.backgroundColor;
//     console.log(element_color)  
// }


function takeColor(){

}
//takeColor()








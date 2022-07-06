let listTasks=[];
let button= document.getElementById('button');
let div = document.getElementsByClassName("listTasks")[0]
let input=document.getElementById("input")

button.addEventListener('click', addTask)


function addTask(){
    event.preventDefault();
    let text=input.value;
    if (text.length==0){
        alert("Enter Something")
    }
    else{
        listTasks.push(text);
        let i_element = document.createElement('i')
        i_element.classList.add("fa-solid")
        i_element.classList.add("fa-xmark")
        let para = document.createElement('p')
        let checkbox=document.createElement("INPUT")
        checkbox.setAttribute('type','checkbox')
        para.append(checkbox," ", i_element ," ",text);
        div.appendChild(para)
        i_element.addEventListener('click',function(){
            para.remove()
        })
        input.value=""

    }
}








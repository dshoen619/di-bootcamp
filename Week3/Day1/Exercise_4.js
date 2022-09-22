

let arr = [ {
    title: 'Harry Potter 1',
    author:'JK Rowling',
    image: src="https://ae01.alicdn.com/kf/HTB1PW1eIVXXXXaxXFXXq6xXFXXXO/Harry-Potter-and-the-Sorcerer-s-Stone-Book-1-English-Children-s-Books-Science-Fiction-Fantasy.jpg_Q90.jpg_.webp",
    alreadyRead:false,
},
{
    title: 'The Great Gatsby',
    author:'F Scott Fitzgerald',
    image: src="https://m.media-amazon.com/images/I/41XMaCHkrgL.jpg",
    alreadyRead:true,
}]


let div = document.getElementsByClassName("listBooks");

let table = document.createElement('table');
div[0].appendChild(table);

for (i in arr){
    let tr = document.createElement('TR');
    table.appendChild(tr);

    let title=document.createElement('td');
    tr.appendChild(title);
    title.textContent=arr[i].title;

    let author=document.createElement('td');
    tr.appendChild(author);
    author.textContent=arr[i].author;

    let image=document.createElement('td');
    tr.appendChild(image);
    image.textContent=arr[i].image;

    let read_status=document.createElement('td');
    tr.appendChild(read_status);
    read_status.textContent=arr[i].alreadyRead;

}





// let row1=book_table.insertRow(0);
// let cell1=row1.insertCell(0);
// let cell2=row1.insertCell(1);
// let cell3=row1.insertCell(2);
// let cell4=row1.insertCell(3);

// cell1.innerHTML=arr[0];
// cell2.innerHTML=arr[1];
// cell3.innerHTML=arr[2];
// cell4.innerHTML=arr[3];
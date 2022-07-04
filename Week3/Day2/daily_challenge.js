var libButton = document.getElementById('lib-button');
        var libIt = function() {
            event.preventDefault();
            var storyDiv = document.getElementById("story");
            let noun_value=document.querySelector('#noun').value;
            let adj_value=document.querySelector('#adjective').value;
            let name_value =document.querySelector('#person').value;
            let verb_value=document.querySelector('#verb').value;
            let place_value=document.querySelector('#place').value;

            if (noun_value.length!=0 && adj_value.length!=0 && name_value.length!=0 && verb_value.length!=0 && place_value.length!=0){
                storyDiv.innerHTML = "The "+adj_value+" "+noun_value+" "+verb_value+" all over "+name_value+" in the middle of "+place_value;
            }
            else{alert("Fill in all spaces!")}
            };
        libButton.addEventListener('click', libIt);

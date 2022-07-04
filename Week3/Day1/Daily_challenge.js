let planets_array = ['Mercury','Venus','Earth','Mars','Jupiter', 'Saturn', 'Uranus', 'Neptune'];
let color_array=["grey", "orange", "green","red", "purple", "yellow", "white", "lightblue" ];

for (i in planets_array){
    let planets=document.createElement("div");
    planets.className="planet";
    document.body.appendChild(planets);
    let list =planets.classList;
    list.add(planets_array[i]);
    let root = document.getElementsByClassName("listPlanets")[0];
    root.appendChild(planets);
}



    
document.getElementsByClassName("Mercury")[0].style.backgroundColor="grey";
document.getElementsByClassName("Venus")[0].style.backgroundColor="orange";
document.getElementsByClassName("Earth")[0].style.backgroundColor="green";
document.getElementsByClassName("Mars")[0].style.backgroundColor="red";
document.getElementsByClassName("Jupiter")[0].style.backgroundColor="Purple";
document.getElementsByClassName("Saturn")[0].style.backgroundColor="Yellow";
document.getElementsByClassName("Uranus")[0].style.backgroundColor="white";
document.getElementsByClassName("Neptune")[0].style.backgroundColor="lightblue";


console.log("hey");




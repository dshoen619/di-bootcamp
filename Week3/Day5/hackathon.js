//event.preventDefault()
let input=document.getElementById("input_2")
// let input=document.getElementById("text_box")
let button= document.getElementById('button'); 
// let navbar=document.getElementById("navbar")
// navbar.style.display="none"
let second_input=document.getElementById("input")

let loc_array=[]


button.addEventListener('click', search)
document.getElementById("things_to_do").style.display="none"
document.getElementById("input").style.display="none"
document.getElementById("nav_button").style.display="none"

//console.log(document.getElementById("activities"))

function search(){
    event.preventDefault()

    console.log("1", input.value)

    // let add_search_bar=document.getElementById("home_bar")
    // add_search_bar.type="text"
    // add_search_bar.className="form-control input-group-lg"
 


    document.getElementById("background").className="next_page row justify-content-around"   
    document.getElementById("header").style.display="none" 
    document.querySelector(".input-group-lg").style.display="none"
    document.getElementById("button").style.display="none" 
    document.getElementById("things_to_do").style.display="block"
    document.getElementById("input").style.display="block"
    document.getElementById("nav_button").style.display="block"

    let loc=input.value
 
    loc_array.push(loc)
    console.log("2", loc_array)
    // console.log(loc)
    all_my_functions()
}

    // let myTimeout=setTimeout(all_my_functions, 0);

function all_my_functions(){
    

    things_to_do()
    where_to_eat()
    Bars()
    kids_activities()
    places_to_stay()
}
    // let nav_bar_search= document.getElementById("input_nav")
    // let new_button=document.getElementById("nav_button")
    // new_button.addEventListener('click',function(){
    //     loc_array=[]
    //     console.log("4",nav_bar_search.value)
    //     loc_array.push(nav_bar_search.value);
    //     console.log("8",loc_array)
    //     search(loc_array[0])

    //})
    
let nav_bar_search= document.getElementById("input_nav")
let new_button=document.getElementById("nav_button")
new_button.addEventListener('click',function(){
    document.getElementById("things_to_do").remove()
    document.getElementById("food").remove()
    document.getElementById("bars").remove()
    document.getElementById("kids_activities").remove()
    document.getElementById("hotels").remove()

    let background= document.getElementById("background")
    let activities_para = document.createElement('p')
    activities_para.id="things_to_do"
    background.append(activities_para)

    let food_para = document.createElement('p')
    food_para.id="food"
    background.append(food_para)

    let bars_para = document.createElement('p')
    bars_para.id="bars"
    background.append(bars_para)

    let kids_para = document.createElement('p')
    kids_para.id="kids_activities"
    background.append(kids_para)

    let hotels_para = document.createElement('p')
    hotels_para.id="hotels"
    background.append(hotels_para)
    
    loc_array=[]

    console.log("4",nav_bar_search.value)
    loc_array.push(nav_bar_search.value);
    console.log("8",loc_array)

    all_my_functions()
})



function things_to_do(){
    console.log("3",loc_array)
    let insert_location=""
    for (i in loc_array){
        insert_location+=loc_array[i]
    }
    let link = "http://www.google.com/search?client=firefox-b-e&q="+insert_location+" things+to+do"
    //let things_to_do = "Things To Do".link(link);
    let things=document.getElementById("things_to_do")
    //document.getElementById("things_to_do").innerHTML= things_to_do;
    document.getElementById("things_to_do").className+= "card mb-3 border border-3 border-primary col-4";
    let img= document.createElement('img')
    img.src="https://www.choicehotels.com/cms/images/choice-hotels/pace/hero-explore-what-to-do-in-a-new-city-charlotte/hero-explore-what-to-do-in-a-new-city-charlotte.jpg" 
    img.style.height="571"
    img.style.width="856"
    img.className="card-img-top"
    things.append(img)
    let div = document.createElement('div')
    div.className="card-body"
    div.style.color="black"
    let header_5=document.createElement('h5')
    header_5.className="card-title"
    header_5.textContent="A day in "+loc_array[0]
    div.append(header_5)
    let p1=document.createElement('p')
    p1.className="card-text"
    p1.textContent="Check out the cool things to do in "+loc_array[0]+"!"
    let new_para=document.createElement('p');
    let button=document.createElement('button')
    button.type="button"
    button.className="btn btn-primary"
    button.textContent="Learn More"
    button.addEventListener('click',function(){
        location=link
    })
    new_para.append(button)
    p1.append(new_para)
    div.append(p1)
    things.append(div)




    let p=document.createElement('p')
    p.className="card-text"
    div.append(p)
    things.append(div)

}

function where_to_eat(){
    let insert_location=""
    for (i in loc_array){
        insert_location+=loc_array[i]
    }
    let link = "https://www.yelp.com/search?find_desc=food&find_loc="+insert_location;
    //let where_to_eat = "Where to Eat".link(link_to_eat);
    let where_to_eat=document.getElementById("food")
    //document.getElementById("food").innerHTML = where_to_eat;

    document.getElementById("food").className+= "card mb-3 border border-3 border-primary col-3";
    let img= document.createElement('img')
    img.src="https://st2.depositphotos.com/3591429/10531/i/950/depositphotos_105319422-stock-photo-people-enjoying-food.jpg" 
    img.style.height="571"
    img.style.width="856"
    img.className="card-img-top"
    where_to_eat.append(img)
    let div = document.createElement('div')
    div.className="card-body"
    div.style.color="black"
    let header_5=document.createElement('h5')
    header_5.className="card-title"
    header_5.textContent="Where to eat in "+loc_array[0]
    div.append(header_5)
    let p1=document.createElement('p')
    p1.className="card-text"
    p1.textContent="Check out the most popular places to eat in "+loc_array[0]+"!"
    let new_para=document.createElement('p');
    let button=document.createElement('button')
    button.type="button"
    button.className="btn btn-primary"
    button.textContent="Learn More"
    button.addEventListener('click',function(){
        location=link
    })
    new_para.append(button)
    p1.append(new_para)
    div.append(p1)
    where_to_eat.append(div)

}

function Bars(){
    let insert_location=""
    for (i in loc_array){
        insert_location+=loc_array[i]
    }
    let link= "https://www.yelp.com/search?find_desc=Bars&find_loc="+insert_location;
    //let where_to_drink = "Bars".link(link_to_bars);
    //document.getElementById("bars").innerHTML = where_to_drink;

    let bars=document.getElementById("bars")
    document.getElementById("bars").className+= "card mb-3 border border-3 border-primary col-3";
    let img= document.createElement('img')
    img.src="http://prod-upp-image-read.ft.com/d56cf392-8575-11ea-b6e9-a94cffd1d9bf" 
    img.style.height="571"
    img.style.width="856"
    img.className="card-img-top"
    bars.append(img)
    let div = document.createElement('div')
    div.className="card-body"
    div.style.color="black"
    let header_5=document.createElement('h5')
    header_5.className="card-title"
    header_5.textContent="Best Bars in "+loc_array[0]
    div.append(header_5)
    let p1=document.createElement('p')
    p1.className="card-text"
    p1.textContent="Check out the best places to grab a drink in "+loc_array[0]+"!"
    let new_para=document.createElement('p');
    let button=document.createElement('button')
    button.type="button"
    button.className="btn btn-primary"
    button.textContent="Learn More"
    button.addEventListener('click',function(){
        location=link
    })
    new_para.append(button)
    p1.append(new_para)
    div.append(p1)
    bars.append(div)

    let p=document.createElement('p')
    p.className="card-text"
    div.append(p)
    bars.append(div)


}


function kids_activities(){
    let insert_location=""
    for (i in loc_array){
        insert_location+=loc_array[i]
    }
    let link = "https://www.yelp.com/search?cflt=kids_activities&find_loc="+insert_location;
    //let kids_activies = "Activities for Kids".link(link_to_kids_activities);
    //document.getElementById("kids_activities").innerHTML = kids_activies;
    let kids=document.getElementById("kids_activities")
    document.getElementById("kids_activities").className+= "card mb-3 border border-3 border-primary col-3";
    let img= document.createElement('img')
    img.src="https://media.timeout.com/images/103146299/750/562/image.jpg" 
    img.style.height="571"
    img.style.width="856"
    img.className="card-img-top"
    kids.append(img)
    let div = document.createElement('div')
    div.className="card-body"
    div.style.color="black"
    let header_5=document.createElement('h5')
    header_5.className="card-title"
    header_5.textContent="Family Friendly Activities in "+loc_array[0]
    div.append(header_5)
    let p1=document.createElement('p')
    p1.className="card-text"
    p1.textContent="Check out activities in "+loc_array[0]+" that the kids will love!"
    let new_para=document.createElement('p');
    let button=document.createElement('button')
    button.type="button"
    button.className="btn btn-primary"
    button.textContent="Learn More"
    button.addEventListener('click',function(){
        location=link
    })
    new_para.append(button)
    p1.append(new_para)
    div.append(p1)
    kids.append(div)

    let p=document.createElement('p')
    p.className="card-text"
    div.append(p)
    kids.append(div)
   
}

function places_to_stay(){
    let insert_location=""
    for (i in loc_array){
        insert_location+=loc_array[i]
    }
    let link = "https://www.google.com/travel/hotels/"+insert_location;
    //let hotels = "Places to Stay".link(link_to_hotels);
    //document.getElementById("hotels").innerHTML = hotels;
    let hotels=document.getElementById("hotels")
    document.getElementById("hotels").className+= "card mb-3 border border-3 border-primary col-3";
    let img= document.createElement('img')
    img.src="https://imageio.forbes.com/specials-images/imageserve/5cdb058a5218470008b0b00f/Nobu-Ryokan-Malibu/0x0.jpg?format=jpg&amp;height=1009&amp;width=2000" 
    img.style.height="571"
    img.style.width="856"
    img.className="card-img-top"
    hotels.append(img)
    let div = document.createElement('div')
    div.className="card-body"
    div.style.color="black"
    let header_5=document.createElement('h5')
    header_5.className="card-title"
    header_5.textContent="Where to stay in "+loc_array[0]
    div.append(header_5)
    let p1=document.createElement('p')
    p1.className="card-text"
    p1.textContent="Check out the best hotels in "+loc_array[0]+"!"
    let new_para=document.createElement('p');
    let button=document.createElement('button')
    button.type="button"
    button.className="btn btn-primary"
    button.textContent="Learn More"
    button.addEventListener('click',function(){
        location=link
    })
    new_para.append(button)
    p1.append(new_para)
    div.append(p1)
    hotels.append(div)




    let p=document.createElement('p')
    p.className="card-text"
    div.append(p)
    hotels.append(div)

    loc_array=[]

}


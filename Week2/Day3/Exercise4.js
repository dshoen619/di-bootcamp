// 1
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 290],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
//2
console.log(building.numberOfFloors);
//3
console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);
//4
let rooms_and_rent = building.numberOfRoomsAndRent;

console.log(Object.keys(rooms_and_rent)[1], Object.values(rooms_and_rent)[1][0]);

//5
let sarahs_rent= Object.values(rooms_and_rent)[0][1];
let davids_rent= Object.values(rooms_and_rent)[2][1];
let dans_rent=Object.values(rooms_and_rent)[1][1];

if (sarahs_rent+davids_rent>dans_rent){
    Object.values(rooms_and_rent)[1][1]=1200;
}

//console.log(sarahs_rent, davids_rent, dans_rent);

console.log(building);


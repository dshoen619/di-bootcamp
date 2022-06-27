let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];



let amt_users=users.length;

if (amt_users==0){
    console.log("no one is online");}
else if (amt_users==1){
    console.log(users[0]+" "+"is online");}
else if (amt_users==2){
    console.log(users[0]+" and "+users[1]+" "+"are online");}
else if (amt_users>2){
    console.log(users[0]+" "+users[1]+" and "+(amt_users-2) +" additional users are online");}





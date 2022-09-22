// 1.
let sentence="The dinner is bad";

// 2.
let wordNot=sentence.indexOf("not");
console.log(wordNot);

// 3.
let wordBad=sentence.indexOf("bad");
console.log(wordBad);

// 4.
if(wordBad>wordNot){
    new_sentence= sentence.replace(/not.*bad/,'good');
    console.log(new_sentence);
}
else {
    console.log(sentence);
}



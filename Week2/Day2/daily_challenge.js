// 1.
let sentence="The movie is not sooooo bad , I like it";

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



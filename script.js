//document.writeln("hello"); 

//console.log("javascript Tutorial");

//var fristnsme="grestdtsck";

// let x =10;

// if(x>5){
//     let y=20;
//     console.log(y);
// }
 
// const a =4;
// console.log(a);

//#Golbal scope

var x = "hello, GreatStack Golbal";
function example(){
    
console.log(x);
}
example(); 

// console.log(x);

//##Function scope

// function example2(){
//     var fs="hello, GreatStack Function";
// }
// example2
//  console.log(fs);  //fs is not defined


 //##Block scope

 function example3(){
    if(true){
        let bv ="GreatStack";
        console.log(bv);
    }
 }
 example3(); 


 //## string data types

 let fristnsme="vaidik";  //double quotes
 let lastname='patel'; //single quotes

 //## number data types

let num = 96.0;
console.log(num);


let x1 ="10"; //string
let x2= 10; //number
console.log(typeof x2);

//## Bolean data types

let learning= true;
let completed =false;

console.log(typeof completed);
console.log(completed);


let a =20>10;
console.log(a);
console.log(typeof a);

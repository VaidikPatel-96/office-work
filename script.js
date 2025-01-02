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

//## undefined data types

let age ;

console.log(age); //age=23

console.log(typeof age);

// ##null data types

let number1= null;
console.log(number1);
console.log(typeof number1);
console.log(null == undefined);


//## Referemce data types

// object

let person = {
    fristnsme : 'vaidik',
    lastname : 'patel',
    age : 36
};
console.log(person);
console.log(typeof person);

// Array data types

let number=[1,2,3,4,5];
console.log(number);
console.log(typeof number);

// function 

function msg(){
    console.log("hello ,vaidik");
    
}
console.log(typeof msg);


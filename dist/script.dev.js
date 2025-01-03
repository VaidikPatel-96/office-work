"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

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

function example() {
  console.log(x);
}

example(); // console.log(x);
//##Function scope
// function example2(){
//     var fs="hello, GreatStack Function";
// }
// example2
//  console.log(fs);  //fs is not defined
//##Block scope

function example3() {
  if (true) {
    var bv = "GreatStack";
    console.log(bv);
  }
}

example3(); //## string data types

var fristnsme = "vaidik"; //double quotes

var lastname = 'patel'; //single quotes
//## number data types

var num = 96.0;
console.log(num);
var x1 = "10"; //string

var x2 = 10; //number

console.log(_typeof(x2)); //## Bolean data types

var learning = true;
var completed = false;
console.log(_typeof(completed));
console.log(completed);
var a = 20 > 10;
console.log(a);
console.log(_typeof(a)); //## undefined data types

var age;
console.log(age); //age=23

console.log(_typeof(age)); // ##null data types

var number1 = null;
console.log(number1);
console.log(_typeof(number1));
console.log(null == undefined); //## Referemce data types
// object

var person = {
  fristnsme: 'vaidik',
  lastname: 'patel',
  age: 36
};
console.log(person);
console.log(_typeof(person)); // Array data types

var number = [1, 2, 3, 4, 5];
console.log(number);
console.log(_typeof(number)); // function 

function msg() {
  console.log("hello ,vaidik");
}

console.log(_typeof(msg)); //## Opreators In JavaScript ##
//Arithmetic Operators
// Addition

var sum = 5 + 3;
console.log(sum); //Subtraction

var s = 5 - 3;
console.log(s); //multiplication

var m = 5 * 3;
console.log(m); //division

var d = 5 / 3;
console.log(d); //Modulus

var m1 = 15 % 31;
console.log(m1); //Exponentiation

var e = Math.pow(2, 4); //2x2x2x2

console.log(e);
//# sourceMappingURL=script.dev.js.map

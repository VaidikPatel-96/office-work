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
console.log(_typeof(person));
//# sourceMappingURL=script.dev.js.map

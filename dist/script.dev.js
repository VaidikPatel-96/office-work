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

console.log(_typeof(x2)); //##
//# sourceMappingURL=script.dev.js.map

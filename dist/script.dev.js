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

console.log(e); //## Assignment Operators

var A = 5; // A +=3;
// A -=3;
// A *=3;
// A /=3;
// A %=3;

A = Math.pow(A, 3);
console.log(A); //## Increment ++/ Decrement-- Operators
//prefix and postfix:
// let i = 10;
// console.log(++i);
// console.log(i);
// let i = 10;
// console.log(--i);
// console.log(i);
// let i = 10;
// console.log(i++);
// console.log(i);

var i = 10;
console.log(i--);
console.log(i); // Comarison Operators

var c = 10;
var c1 = 20;
console.log(c < c1);
console.log(c > c1);
console.log(c <= c1);
console.log(c >= c1);
console.log(c == c1);
console.log(c != c1);
console.log(c === c1);
console.log(c !== c1); // Logical Operator
// AND (&&)

var a2 = 5;
var a3 = 10;
console.log(a2 > 0 && a3 > 0);
console.log(a2 > 0 && a3 < 0);
console.log(a2 < 0 && a3 > 0);
console.log(a2 < 0 && a3 < 0); // OR || 

var b2 = 5;
var b3 = 10;
console.log(b2 < 0 || b3 > 0);
console.log(b2 > 0 || b3 < 0);
console.log(b2 > 0 || b3 > 0);
console.log(b2 < 0 || b3 < 0); // NOT (!)

var yes = true;
var no = false;
console.log(!yes);
console.log(!no); //## Operator Precedence

var result = 2 + 3 * 4;
console.log(result); // 2+3= 5 * 4 =20
//## Conditional Statements
//if

var contry = "India";
var age1 = 20;

if (age1 >= 18 && contry == "India") {
  console.log("You can get a driver's license. ");
} //If else


var age5 = 19;

if (age5 > 18) {
  console.log("YOu are an adult.");
} else {
  console.log("You are a minor.");
} // else if


var age6 = 17;

if (age6 >= 18) {
  console.log("you are an adult");
} else if (age6 >= 16) {
  console.log("you are  teenager");
} else {
  console.log("you are a minor");
} //Switch


var value = true;

switch (_typeof(value)) {
  case "number":
    console.log("number");
    break;

  case "string":
    console.log("string");
    break;

  case "boolean":
    console.log("boolean");
    break;

  default:
    console.log("other");
    break;
}

var dayName = 4;

switch (dayName) {
  case 1:
    dayName = "Sunday";
    break;

  case 2:
    dayName = "Monday";
    break;

  case 3:
    dayName = "tuesday";
    break;

  case 4:
    dayName = "wednesday";
    break;

  case 5:
    dayName = "thrusday";
    break;

  case 6:
    dayName = "friday";
    break;

  case 1:
  case 7:
    dayName = "saturday";
    break;

  default:
    dayName = "Invalid day number";
    break;
}

console.log("The day is:" + dayName); // Ternary operator
// condition ? value_if_true : value_if_false

var age7 = 16;
var msg1 = age7 >= 18 ? "You are an adult" : "you are a minor";
console.log(msg1); //## loop
// for loop
//  for (let ii =1; ii <=10; ii++){
//     console.log(ii);
//  }

for (var ii = 1; ii <= 5; ii++) {
  console.log(ii);

  for (var j = 1; j <= 3; j++) {
    console.log("inner loop" + j);
  }
} //wile loop


var iii = 0;

while (iii <= 10) {}
//# sourceMappingURL=script.dev.js.map

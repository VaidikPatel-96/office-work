var para = document.getElementById("p");
para.innerText = "Hello World";
para.style.color = "blue";
para.style.fontSize = "20px";
para.style.fontWeight = "bold";


var para2 = document.querySelector(".para2");
if (para2) {
    para2.innerText = "Hello World";
    para2.style.color = "green";
    para2.style.fontSize = "18px";
    para2.style.fontWeight = "normal";
}

var data1 = document.getElementById("p");
document.write(data1.innerText);
document.write(data1.style);

const paras = document.getElementById("p");
paras.addEventListener("click", function () {
    alert("Hello World");
});
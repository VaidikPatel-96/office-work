const notesConstainer = document.querySelector(".notes-container");
const creatBtn = document.querySelector(".btn");
let notes= document.querySelectorAll(".input-box");


function updateStorage(){
    localStorage.setItem("notes",notesConstainer.innerHTML);
}

creatBtn.addEventListener("click", ()=>{
    let inputBox = document.createElement("p");
    let img = document.createElement("img");
    inputBox.className= "input-box";
    inputBox.setAttribute("contenteditable","true");
    img.src = "images/delete.png";
    notesConstainer.appendChild(inputBox).appendChild(img);
});

notesConstainer.addEventListener("click", function(e){
    if(e.target.tagName ==="IMG"){
        e.target.parentElement.remove();
        updateStorage()
         
    }
})
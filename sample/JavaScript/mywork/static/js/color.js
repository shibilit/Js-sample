const btnEl = document.querySelector(".btn");
const bodyEl = document.querySelector("body");

var colors = ["green", "blue", "orange", "yellow", "violet"];

bodyEl.style.background = "pink";

btnEl.addEventListener("click", addColor);

function addColor() {
    console.log("clicked");
    var color = parseInt(Math.random() * colors.length);
    bodyEl.style.background = colors[color];
    count++;
}
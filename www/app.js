//Write the javascript code here

//scummy websites use this to create popups
//alert("Hello from App.js!");

var pics = [
    "imgs/picture1.jpg",
    "imgs/picture2.gif",
    "imgs/picture4.jpg",
    "imgs/picture5.jpg",
    "imgs/picture6.jpg",
    "imgs/picture7.jpg",
    "imgs/picture8.jpg",
    "imgs/picture9.jpg",
    "imgs/picture10.png"
]

//targets the first instance of button
var btn = document.querySelector("button"); //(semicolon ;) is important but sometimes optional in JS
var img = document.querySelector("img");
var counter = 1;
btn.addEventListener("click", function() {
    //alert("Clicked!"); //works! 6/27/20 8:04pm
    //img.src = "imgs/picture2.jpg";

    if (counter === 9) {
        counter = 0;
    } else {
        img.src = pics[counter];
        counter++; //counter = counter + 1
    }
});



let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");


ctx.imageSmoothingEnabled = false;

var imgWidth = 55;
var imgHeight = 82;
var imgMouse = "./assets/mouse.png";
var imgMouseRight = "./assets/mouse_right-click.png";
var imgMouseLeft = "./assets/mouse_left-click.png";


var img = new Image();
img.src = "./assets/mouse.png";
var posXStart = (cnv.width / 2) - (imgWidth / 2);
var posYStart = (cnv.height / 2) - (imgHeight / 2);
img.onload = function() {
    ctx.drawImage(img, posXStart, posYStart, imgWidth, imgHeight);
};


function updateImage(newImg) {
    img.src = newImg;
};


let gui = new dat.gui.GUI();
let mouseFolder = gui.addFolder("Mouse");
mouseFolder.open()


let param = {
    mouse : {
        x: posXStart,
        y: posYStart,
        // mouseDefault: updateImage(imgMouse),
        // mouseRight: updateImage(imgMouseRight),
        // mouseLeft: updateImage(imgMouseLeft),
    },
};

mouseFolder.add(param.mouse, "x", 0, 600, 1);
mouseFolder.add(param.mouse, "y", 0, 400, 1);
// mouseFolder.add(param.mouse, "mouseDefault");
// mouseFolder.add(param.mouse, "rigmouseRightht");
// mouseFolder.add(param.mouse, "mouseLeft");


// HOM TO UPDATE imgWidth AND imgHeight WITH dat.GUI ???


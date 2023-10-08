

let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");


ctx.imageSmoothingEnabled = false;




class myImg {
    constructor(imgSrc = null, w = 25, h = 25) {
    this.defaultW = w;
    this.defaultH = h
    this.w = w;
    this.h = h;
    this.imgSrc = imgSrc;

    this.x = (cnv.width / 2) - (this.w / 2);
    this.y = (cnv.height / 2) - (this.h / 2);

    this.img = new Image();
    this.img.src = this.imgSrc;
    }

    reset() {
        this.w = this.defaultW;
        this.h = this.defaultH;
        this.x = (cnv.width / 2) - (this.w / 2);
        this.y = (cnv.height / 2) - (this.h / 2);
        this.img.src = this.img;
    }

    draw(ctx) {
        ctx.drawImage(this.img, this.x, this.y, this.w, this.h);
    }
}

class myAnimatedImg extends myImg {
    constructor(/*spritesW = null, spritesH = null,*/ sprites = [], w = 25, h = 25) {
        // myImg.call(this, sprites[0], w, h);
        super(sprites[0], w, h);
        this.sprites = sprites;
        // this.spritesW = spritesW;
        // this.spritesH = spritesH;
    }

    next_frame(cnv) {
        size = this.sprites.length
        next = this.sprites.slice(0, 1)
        this.sprites = this.sprites.slice(1, -1)
        this.sprites.push(next)
        this.img.src = next
    }

}


// let img = new myImg();
let imgName = "pp-a_pp_walking_";
let ext = ".png";
let sprites = [];
for (let i = 0; i < 8; i++) {
    sprites.push(imgName + (i+1) + ext);
}


let img = new myAnimatedImg(sprites)
let gui = new dat.gui.GUI();

let imgFolder = gui.addFolder("Perso");
imgFolder.open()


imgFolder.add(img, "x", 0, cnv.width - img.w, 1);
imgFolder.add(img, "y", 0, cnv.height - img.h, 1);
imgFolder.add(img, "w", 10, cnv.width, 1);
imgFolder.add(img, "h", 10, cnv.height, 1);
imgFolder.add(img, "reset");


function updateDisplay() {
    imgFolder.updateDisplay();
}


function draw() {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    img.draw(ctx);
    updateDisplay();
}


function update() {
    draw();
    requestAnimationFrame(update);
}

requestAnimationFrame(update);

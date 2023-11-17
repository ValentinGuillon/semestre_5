
let cnv = document.getElementById("myCanvas");
let ctx = cnv.getContext("2d");

ctx.imageSmoothingEnabled = false;

let gui = new dat.gui.GUI();





function dist(x0, y0, x1, y1) {
    let dx = x1-x0;
    let dy = y1-y0;
    return Math.sqrt( dx*dx + dy*dy );
}

class Arc {
    constructor(x, y, r) {
    this.x = x; this.y = y; this.r = r;
    }
    collide(otherArc) {
        let r = this.r + otherArc.r;
        return dist(this.x, this.y, otherArc.x, otherArc.y) < r;
    }
    move(dx, dy) {
        this.x += dx; this.y += dy;
    }
    moveTo(nx, ny) {
        this.x = nx; this.y = ny;
    }
}




let velocity = 2;
let moving_A = [];
let static_A = [];
function collide_with(new_a, T) {
    for (let i = 0; i < T.length; i++)
        if(new_a.collide(T[i])) return true;
    return false;
}
while (static_A.length < 10) {
    let new_x = Math.floor(Math.random() * cnv.width);
    let new_y = Math.floor(Math.random() * cnv.height);
    let new_a = new Arc(new_x, new_y, 30);
    if(collide_with(new_a, static_A) == false)
        static_A.push(new_a);
}

while (moving_A.length < 40) {
    let new_x = Math.floor(Math.random() * cnv.width);
    let new_y = Math.floor(Math.random() * (cnv.height-50));
    let new_r = 10+Math.floor(Math.random() * 40);
    let new_a = new Arc(new_x, new_y, new_r);
        if(collide_with(new_a, moving_A) == false)
    moving_A.push(new_a);
}








function draw() {
    ctx.clearRect(0, 0, cnv.width, cnv.height);
    for (let i = 0; i < static_A.length; i++) {
        ctx.beginPath();
        ctx.arc(static_A[i].x, static_A[i].y, static_A[i].r, 0, 2*Math.PI);
        ctx.fillStyle = "gray";
        ctx.fill();
        ctx.closePath();
    }
    for (let i = 0; i < moving_A.length; i++) {
        if(collide_with(moving_A[i], static_A) == false) {
            ctx.beginPath();
            ctx.arc(moving_A[i].x, moving_A[i].y, moving_A[i].r, 0, 2*Math.PI);
            ctx.fillStyle = "red";
            ctx.fill();
            ctx.closePath();
        }
        ctx.beginPath();
        ctx.arc(moving_A[i].x, moving_A[i].y, moving_A[i].r, 0, 2*Math.PI);
        ctx.strokeStyle = "dark";
        ctx.stroke();
        ctx.closePath();
    }
}

function update_pos() {
    console.log(moving_A.length)
    for (let i = 0; i < moving_A.length; i++) {
        moving_A[i].move(0,velocity);
        if(moving_A[i].y >= cnv.height) {
            moving_A[i].moveTo(moving_A[i].x, 0);
        }
    }
}

function update(timestamp) {
    update_pos();
    draw();
    requestAnimationFrame(update);
}
requestAnimationFrame(update);

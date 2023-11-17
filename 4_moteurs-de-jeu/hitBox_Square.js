
// À TESTER
class HitBox_Square {
    constructor(x, y, w, h) {
        this.x = x; this.y = y;
        this.w = w; this.h = h;

        this.collision = true;
        this.contours = false;
    }

    //retourn true if at least one border of "obj" is inside "this"
    is_collides(obj) {
        if (!this.collision) { return false}
        let left = false;
        let right = false;
        let top = false;
        let bot = false;

        let my_left = this.x
        let my_right = this.x + this.w
        let my_top = this.y;
        let my_bot = this.y + this.h;

        let obj_left = obj.x
        let obj_right = obj.x + obj.w
        let obj_top = obj.y;
        let obj_bot = obj.y + obj.h;

        //by left
        if (obj_left >= my_left && obj_left <= my_right) {
            left = true;
        }
        //by right
        if (obj_right >= my_left && obj_right <= my_right) {
            right = true;
        }
        //by top
        if (obj_top >= my_top && obj_top <= my_bot) {
            top = true;
        }
        //by bottom
        if (obj_bot >= my_top && obj_bot <= my_bot) {
            bot = true;
        }

        //maybe add conditions for the case, "obj" completely inside "this" (or vice versa)


        //verif
        if ((!left && !right) || (!left && !right)) {
            return false;
        }
        
        //se chevauve
        if (top && (right || left)) {
            return true;
        }
        if (bot && (right || left)) {
            return true;
        }

        if (top && bot) {
            return true;
        }
        if (left && right) {
            return true;
        }

        //no collision
        return false
    }

    draw_contours(cnv) {

    }

}

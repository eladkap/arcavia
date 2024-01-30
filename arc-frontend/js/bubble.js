class Bubble {
    constructor(x, y, radius, velocity, color) {
        this.pos = new Vector(x, y);
        this.radius = radius;
        this.velocity = velocity;
        this.color = color;
    }

    display() {
        ctx.beginPath();
        ctx.arc(this.pos.x, this.pos.y, this.radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = this.color;
        ctx.stroke();
    }

    update() {
        this.pos.add(this.velocity);
        this.checkBounds();
    }

    checkBounds() {
        if (this.pos.x - this.radius < 0 || this.pos.x + this.radius > window.innerWidth) {
            this.velocity.x *= -1;
        }
        if (this.pos.y - this.radius < 0 || this.pos.y + this.radius > window.innerHeight) {
            this.velocity.y *= -1;
        }
    }

    isClicked(mx, my) {
        let dSquared =  Math.pow(this.pos.x - mx, 2) + Math.pow(this.pos.y - my, 2);
        return dSquared < Math.pow(this.radius, 2);
    }
}
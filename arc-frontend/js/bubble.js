class Bubble {
    constructor(x, y, radius, velocity, color, symbol, srcImage) {
        this.pos = new Vector(x, y);
        this.radius = radius;
        this.velocity = velocity;
        this.color = color;
        this.symbol = symbol;
        this.srcImage = srcImage;
    }

    display() {
        ctx.beginPath();
        ctx.arc(this.pos.x, this.pos.y, this.radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = this.color;
        ctx.stroke();

        ctx.font = `${this.radius}px ${SYMBOL_FONT_FAMILY}`
        ctx.fillStyle = 'black';
        ctx.fillText(this.symbol, this.pos.x - this.radius * 0.6, this.pos.y + this.radius / 4);

        ctx.fillStyle = 'white';
        ctx.fillRect(this.pos.x, this.pos.y, 3, 3);
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
 
    isClicked(mousePos) {
        let d =  Utils.dist(mousePos, this.pos);
        console.log(`${mousePos.toString()} - ${this.pos.toString()} = ${d}   ${this.radius}   ${this.symbol}`);
        return d < this.radius;
    }
}
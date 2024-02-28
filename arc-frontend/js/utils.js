class Utils {
    static getRandomFromRange(a, b) {
        return Math.random() * (b - a) + a;
    }

    static dist(p1, p2) {
        let a = p1.x - p2.x;
        let b = p1.y - p2.y;
        return Math.sqrt(a ** 2 + b ** 2);
    }

    static squaredDist(p1, p2) {
        let a = p1.x - p2.x;
        let b = p1.y - p2.y;
        return a ** 2 + b ** 2;
    }

    static checkCorrectAnswer(query, bubble) {
        let correctAnswer = query.answers[query.correctAnswerInd];
        return bubble.symbol == correctAnswer;
    }

    static translateMouseToCanvasPosition(mouseX, mouseY, canvasRect) {
        let mx = mouseX - canvasRect.left - scrollX;
        let my = mouseY - canvasRect.top - scrollY;
        mx /= canvasRect.width;
        my /= canvasRect.height;
        mx *= canvas.width;
        my *= canvas.height;
        return new Vector(mx, my);
    }
}
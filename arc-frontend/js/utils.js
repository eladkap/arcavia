class Utils {
    static getRandomFromRange(a, b) {
        return Math.random() * (b - a) + a;
    }

    static dist(p1, p2) {
        let a = p1.x - p2.x;
        let b = p1.y - p2.y;
        return Math.sqrt(a * a + b * b);
    }

    static squaredDist(p1, p2) {
        let a = p1.x - p2.x;
        let b = p1.y - p2.y;
        return a * a + b * b;
    }

    static checkCorrectAnswer(query, bubble) {
        let correctAnswer = query.answers[query.correctAnswerInd];
        return bubble.symbol == correctAnswer;
    }
}
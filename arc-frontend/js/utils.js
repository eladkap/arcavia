class Utils {
    static getRandomFromRange(a, b) {
        return Math.random() * (b - a) + a;
    }

    static dist(p1, p2) {
        return Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2);
    }

    static checkCorrectAnswer(query, bubble) {
        let correctAnswer = query.answers[query.correctAnswerInd];
        return bubble.symbol == correctAnswer;
    }
}
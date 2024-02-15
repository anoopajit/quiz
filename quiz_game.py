from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        answers = {
            "karnataka": ["bangalore", "bengaluru"],
            "india": ["delhi", "new delhi"],
            "currency": ["dollar", "us dollar"],
            "sydney": ["sydney"]
        }

        # Check answers
        for question, correct_answers in answers.items():
            user_answer = request.form.get(question)
            if user_answer and user_answer.lower() in correct_answers:
                score += 1

        return render_template('result.html', score=score)
    else:
        return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)

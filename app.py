from flask import Flask, render_template, request
from generator import Generator

app = Flask(__name__)

LENGTH = 100

def generate(length):
    gen = Generator()
    results = []
    for i in range(length):
        results.append(gen.generate())
    return results

@app.route('/')
def index():
    results = generate(LENGTH)
    return render_template('index.html', results=results)

@app.route('/submit', methods=['POST'])
def submit():
    selected_fruits = request.form.getlist('fruit')
    return f'選択されたフルーツ: {", ".join(selected_fruits)}'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    selected_fruits = request.form.getlist('fruit')
    return f'選択されたフルーツ: {", ".join(selected_fruits)}'

if __name__ == '__main__':
    app.run(debug=True)

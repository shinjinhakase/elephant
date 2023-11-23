from flask import Flask, render_template, request, Response
from generator import Generator
import csv
from io import StringIO

app = Flask(__name__)

LENGTH = 100
category = ["male","female","land","horse","monster","none"]

def generate(length):
    gen = Generator()
    results = []
    for i in range(length):
        results.append(gen.generate())
    return results

def one_hot_vector(set_category):
    vector = []
    for c in category:
        if set_category == c:
            vector.append(1)
        else:
            vector.append(0)
    return vector

def form_to_csv(form):
    data = []
    for c in category:
        clist = form.getlist(c)
        vector = one_hot_vector(c)
        for name in clist:
            row = [name]
            row.extend(vector)
            data.append(row)
    return data

@app.route('/')
def index():
    results = generate(LENGTH)
    return render_template('index.html', results=results)

@app.route('/submit', methods=['POST'])
def submit():
    data = [["name"]]
    data[0].extend(category)
    data.extend(form_to_csv(request.form))
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerows(data)

    # レスポンスを作成し、CSVファイルとしてダウンロード
    response = Response(
        csv_data.getvalue(),
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=data.csv'}
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)

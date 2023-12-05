from flask import Flask, render_template, request, Response
from generator import Generator
from classifier import Classifier
import csv
from io import StringIO

app = Flask(__name__)
AMOUNT = 100
LENGTH = 2
category = ["male","female","land","horse","monster","none"]

def generate(length):
    gen = Generator()
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

def form_to_csv_gb(form):
    data = []
    for g in form.getlist("good"):
        data.append([g,1,0])
    for b in form.getlist("bad"):
        data.append([b,0,1])
    return data

@app.route('/')
def index():
    # gen = Generator()
    # results = gen.generate_list(LENGTH, AMOUNT)
    # return render_template('index.html', results=results)
    return "ROUTE"

@app.route('/elim_none')
def elim_none():
    cla = Classifier()
    results = cla.generate(AMOUNT)
    return render_template('index.html', results=results)

@app.route('/hunt')
def hunt():
    cla = Classifier()
    results = cla.treasure(AMOUNT)
    return render_template('index.html', results=results)

@app.route('/gb')
def good_bad():
    cla = Classifier(str(LENGTH) + 'let_gb_model')
    results = cla.generate_for_more_learn()
    return render_template('gb_page.html', results=results)

@app.route('/gb_sub', methods=['POST'])
def gb_sub():
    data = [["name","good","bad"]]
    data.extend(form_to_csv_gb(request.form))
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerows(data)
    response = Response(
        csv_data.getvalue(),
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=2let_gb_data.csv'}
    )
    return response

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

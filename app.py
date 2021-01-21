from flask import Flask, render_template, request

app = Flask(__name__)

rows = []

@app.route('/')
def index():
    return '<h1> Hello World</h1>'
#    return render_template('index.html', names=rows)

# @app.route('/process_name', methods = ['POST'])
# def process_name():
#     name =request.form['name']
#     age=request.form['age']
#     rows.append([name,age])
#     print("Recieved request to add " + request.form["name"])
#
#     return '<h1>' + request.form["name"] + '</h1>'
# #    return render_template('index.html', names=rows)


if __name__ == "__main__":
    app.run()

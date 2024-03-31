from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    AuthorName = "Smit PATEL"
    if request.method == 'POST':
        return render_template('anon.html', name=request.form['name'])
    return render_template('anon.html', user = AuthorName)


if __name__ == '__main__':
    app.run(debug=True)
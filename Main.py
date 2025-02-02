from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/category/')
def category():
    return render_template('category.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run(debug=True)


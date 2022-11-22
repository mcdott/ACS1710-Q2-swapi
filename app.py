from flask import Flask

app = Flask(__name__)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('character-search-form.html')




if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('character-search-form.html')

@app.route('/results')
def results():
    swapi_url = 'https://swapi.py4e.com/api/'
    character_id = request.args.get('character_id')
    character_response = requests.get(swapi_url + 'people/' + character_id)
    character_result = json.loads(character_response.content)
    # >>>>>>>
    print(character_id)
    print(character_result)


    context = {
        'character': character_result
        }
    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
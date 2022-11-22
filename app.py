from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def search():
    context = {
    'valid_id': True
    }
    return render_template('character-search-form.html', **context)

@app.route('/results')
def results():
    swapi_url = 'https://swapi.py4e.com/api/'
    character_id = request.args.get('character_id')
    character_response = requests.get(swapi_url + 'people/' + character_id)
    character_result = json.loads(character_response.content)

    context = {
            'character': character_result
            }
    try: 
        check_for_key = character_result['name']
        return render_template('results.html', **context)
    except KeyError:
        context = {
            'valid_id': False
        }
        return render_template('character-search-form.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
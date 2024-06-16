import time
from flask import Flask, render_template, request, jsonify
from ollama_module import OllamaClient

oc = OllamaClient()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/zeugnisse')
def zeugnisse():
    return render_template('zeugnisse.html')


@app.route('/zeugnis', methods=['GET'])
def zeugnis():
    data = request.args
    id = data.get('id')

    name = 'Vorname'
    surname = 'Nachname'
    birthday = 'mm.dd.YYYY'

    if not id:
        return render_template('zeugnis.html')
    else:
        if id == '1':
            name = 'Max'
            surname = 'Mustermann'
            birthday = '09. 07. 2006'
        elif id == '2':
            name = 'Karen'
            surname = 'Bens'
            birthday = '23. 07. 2005'
        elif id == '3':
            name = 'Beeke'
            surname = 'Prehn'
            birthday = '14. 02. 2006'
        return render_template('zeugnis.html', id=id, name=name, surname=surname, birthday=birthday)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    content = data.get('content')
    fach = data.get('fach')
    name = data.get('name')
    if not fach:
        response = oc.get_response(content=content, subject='', name=name)
    else:
        response = oc.get_response(content=content, subject=fach, name=name)

    response_data = {'message': f'{response}'}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)

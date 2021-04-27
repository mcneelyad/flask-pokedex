from flask import Flask, url_for, request, render_template, session

import api

app = Flask(__name__)
app.config['SECRET_KEY'] = "/lYx#&!v@?)U+#YHU&SrTUsfK$sOa;"

pokemon = api.getPokemonByName('pikachu')

@app.route('/')
def home():
    return render_template('index.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)
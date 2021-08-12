from flask import Flask, request, render_template
import os
import api

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Home page
@app.route('/', methods=['POST', 'GET'])
def home():
   # search for a specific pokemon
   if request.method == 'POST':
      
      # if the form value is not empty
      if request.form['pokemon'] != '':
         try:
            # get the pokemon data from the form
            pokemon = api.getPokemonByName(request.form['pokemon'])

            # get the image url from pokemon data
            image = api.getPokemonImage(pokemon).front['default']

            return render_template('search.html', pokemon=pokemon, image=image)
         except:
            # if the pokemon is not found, return an error message
            message = "Pokemon Not Found"
            return render_template('search.html', message=message)

      # if the form value is empty
      else:
         message = "Please enter a pokemon name"
         return render_template('search.html', message=message)

   # if the request is a GET request
   else:
      return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request,redirect
app = Flask(__name__)


@app.route("/")
def index():
      return render_template('index.html')
    
    
@app.route('/results', methods=['POST'])
def results():
    favpets = request.form.getlist('favorite_pet')
    fav = ",".join(favpets)
    userDict = {
      'name':request.form['name'],
      'location': request.form['location'],
      'favLang':request.form['favLang'],
      'gender':request.form['gender'],
      'favorite_pet':fav,
      'comments':request.form['comments'],
    }
    print(userDict["favorite_pet"])
    print(userDict)
    return render_template('results.html',userDict=userDict)

if __name__ == '__main__':
  app.run(debug=True)
 
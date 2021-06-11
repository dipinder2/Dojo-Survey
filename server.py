from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key = "asdjgfljadsl;fgjadsl;kjfl;aksdjfl;kasjl;fkasdjl;kfjasl;kjflkasdjf;kilasjhipouwehjiopuhjnsadk;jhnfk;asdhfkasdhjfkj;ashjkfashdkjl;fjasdkljaskfjaskl;dfjk;alsdjfkl;sadjfkl;asdjflk;adsjkldfsajlkasdjfsadj"


@app.route("/")
def index():
      return render_template('index.html')
    
    
@app.route("/success")
def success():
    return render_template('results.html',userDict=session)
    
    
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
    for keys,value in userDict.items():
          session[keys] = value
    return redirect('/success')


if __name__ == '__main__':
  app.run(debug=True)
 
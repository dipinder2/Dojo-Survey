from flask import Flask, render_template, request,redirect
app = Flask(__name__)


@app.route("/")
def index():
      return render_template('index.html')
    
    
@app.route('/results', methods=['POST'])
def results():
    userDict = {
      'name':request.form['name'],
      'location': request.form['location'],
      'favLang':request.form['favLang'],
      'comments':request.form['comments']
    }
    print(userDict)
    return render_template('results.html',userDict=userDict)

if __name__ == '__main__':
  app.run(debug=True)
 
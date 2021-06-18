from flask import redirect,render_template,request
from flask_app import app
from ..models.user import User

@app.route("/")
@app.route("/user")
def index():
      return render_template('index.html')
    
    
@app.route("/user/<int:id>")
def user(id):
      return render_template('results.html',user = User.get_one({'id':id}))
    
    
@app.route('/results', methods=['POST'])
def results():
      if not User.validate_user(request.form):
            return redirect('/user')
      id = User.insert_user(request.form)
      return redirect(f'/user/{id}')


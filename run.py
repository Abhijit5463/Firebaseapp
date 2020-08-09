import pyrebase
  
config = {
  "apiKey": "AIzaSyA5KdMWmCpGN9pFmwYie8AWOz_J20D-nS0",
  "authDomain": "test-b98ea.firebaseapp.com",
  "databaseURL": "https://test-b98ea.firebaseio.com",
  "projectId": "test-b98ea",
  "storageBucket": "test-b98ea.appspot.com",
  "messagingSenderId": "824919329134",
  "appId": "1:824919329134:web:0c75ccb564240eb7f5197f",
  "measurementId": "G-T26690LTL6"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

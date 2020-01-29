from flask import Flask, url_for, render_template, request 
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def opening():
	return render_template("opening.html")

@app.route('/opening/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		name = request.form['name']
		password = request.form['password']
		username = request.form['username']
		year = request.form['year']
		add_user(username, name, year, password)
        return render_template('homepage.html',
            name = name,
            year = year)

@app.route('/opening/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		return render_template("signin.html")
	else:
		username = request.form['username']
		password = request.form['password']
		requested= verify_user(username, password)
		print(requested)
		if requested:
			session['using'] = username
			return render_template(url_for(homepage), username=username
			)
		else:
			return render_template("signin.html", 
				error="username or password is incurrect, try again")

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
	info = profile(session['using'])
	return render_template("homepage.html", name=info[0], year=info[1], challanges=info[2])
	



if __name__ == '__main__':
	app.run(debug=True)
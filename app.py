from flask import Flask, url_for, render_template, request, redirect
from databases import *
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def opening():
    print(querry_all_u())
    print(querry_all_c())

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
            login_session['using'] = username
            logged=profile(username)
            name=logged[0]
            year=logged[1]
            challanges=logged[2]
            return render_template("homepage.html", username=username, name=name, year=year)  
        else:
            return render_template("signin.html", 
                error="username or password is incurrect, try again")

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    info = profile(login_session['using'])
    uploaded=querry_all_c()
    return render_template("homepage.html", name=info[0], year=info[1], challanges=info[2], uploaded=uploaded)

@app.route('/homepage/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("upload.html")
    else:
        cn = request.form['cn']
        description = request.form['description']
        newc = upload_challange("", cn, description)
        return redirect("/homepage")




if __name__ == '__main__':
    app.run(debug=True, threaded=False)
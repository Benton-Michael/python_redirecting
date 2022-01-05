from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# write a function that will show a page with a form on it
# the index route will handle rendering the HTML form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got the POST info")
    print(request.form)
    # Never render a template on a POST request.
    # To avoid this, redirect to the index route.
    name = request.form['name']
    email = request.form['email']
    return redirect('/show')

# adding the method below -Redirecting- in order to present the HTML form data
# to the user, in browser
@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)

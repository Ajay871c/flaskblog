from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator

'''
safe
capitalize
lower
upper
title
trim
striptags
'''

@app.route('/')
def index():
	stuff = "This is <strong>BOLD</strong> text."
	favorites = [
		'cheese',
		'pepperoni',
		981,
		142432
	]
	return render_template('index.html',
		stuff=stuff,
		favorites = favorites
		)

#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404


@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'),500
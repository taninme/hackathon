from app import app, db
from flask import request, redirect, request, flash, session, url_for
from flask import render_template, jsonify
from forms import SignupForm, SigninForm
from flask import send_file
from models import db, User
from app.main import generator

from lolhelp import *

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/generate')
def generate():
	g= generator()
	LNG, LAT = g.gene()
	print LNG
	return render_template("about.html", LAT = LAT, LNG = LNG)
	

@app.route('/list_all')
def list_cost():
	g = generator()
	list_all = g.parser()
	list_c = dict()
	i = 0
	for i in range(len(list_all)):
		list_c[i] = str(list_all[i])
	return jsonify(list_c)
	

# https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/G0Devil?api_key=DEV_KEY
@app.route('/', methods=['POST'])
def index_post():
	input_name = request.form['username']
	summoner_data = get_summoner_data(input_name.replace(' ', ''))

	if summoner_data == None:	
		return render_template("summoner_not_found.html", input_name = input_name)
	else:
		# Map Map Map!!!!!
		roman = ['', 'I', 'II', 'III', 'VI', 'V']
		number = {'I':1, 'II':2, 'III':3, 'VI':4, 'V':5}
		tier_number = {'BRONZE':1, 'SILVER':2, 'GOLD':3, 'PLATINUM':4, 'DIAMOND':5, 'MASTER':6,
						'CHALLENGER':7}		
		summoner_stat = get_summoner_stat(summoner_data)
		# -------------------------
		# I will do refactoring later
		# ------------------------- 
		rank = "Unranked"
		wins = 0
		losses = 0
		leaguePoints = 0
		
		division = 0
		tier = 0
		
		rank_name = ""

		if not summoner_stat == None:
			rank = summoner_stat['tier'] + ' ' + summoner_stat['entries'][0]['division']
			
			wins = summoner_stat['entries'][0]['wins']
			losses = summoner_stat['entries'][0]['losses']
			leaguePoints = summoner_stat['entries'][0]['leaguePoints']
			
			rank_name = summoner_stat['name']

			division = number[summoner_stat['entries'][0]['division']]
			tier = tier_number[summoner_stat['tier']]
		src_img = '/img/lol_img/tiers/' + str(tier) + '-' + str(division)+'.png'

		summoner_hisory =  get_summoner_hisory(summoner_data)

		return render_template("summoner_page.html", 
			summoner_data = summoner_data, 
			rank = rank,
			wins = wins,
			losses = losses,
			leaguePoints = leaguePoints,
			rank_name = rank_name,
			src_img = src_img,
			summoner_hisory = summoner_hisory
			)


@app.route('/champ')
def base():
	champions = get_champs()
	return render_template('champs.html', champions  = champions)

@app.route('/test')
def testpage():
    return "hello world! -- this is from local"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/riot.txt')
def verification_by_riot():
	return app.send_static_file('riot.txt')

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return 'Something is broken.'
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:   
			newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()
			session['email'] = newuser.email
			return redirect(url_for('profile'))

	elif request.method == 'GET':
		return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	form = SigninForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signin.html', form=form)
		else:
			session['email'] = form.email.data
			return redirect(url_for('profile'))

	elif request.method == 'GET':
		return render_template('signin.html', form=form)


@app.route('/profile')
def profile():

	if 'email' not in session:
		return redirect(url_for('signin'))

	user = User.query.filter_by(email = session['email']).first()

	if user is None:
		return redirect(url_for('signin'))
	else:
		return render_template('profile.html')

@app.route('/signout')
def signout():
	if 'email' not in session:
		return redirect(url_for('signin'))
	 
	session.pop('email', None)
	return redirect(url_for('index'))
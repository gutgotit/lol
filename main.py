from flask import Flask,render_template,Response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///final.db"
app.config['SECRET_KEY']='fds,lfhsjdfhjmndfsm,gfg'
db=SQLAlchemy(app)
class Framework(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Integer, nullable=False)
class Library(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Integer, nullable=False)
class Module(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False)
    licence=db.Column(db.String(80), nullable=False)
    status = db.Column(db.Integer, nullable=False)
@app.route('/')
def home():
	item=Library.query.filter_by().all()
	l=0
	lf=0
	for i in item:
		if i.status==1:
			l+=1
		else:
			lf+=1
	item=Framework.query.filter_by().all()
	f=0
	ff=0
	for i in item:
		if i.status==1:
			f+=1
		else:
			ff+=1
	item=Module.query.filter_by().all()
	m=0
	mf=6
	for i in item:
		if i.status==1:
			m+=1
		else:
			mf+=1
	return render_template('all.html',l=l,m=m,f=f,lf=lf,mf=mf,ff=ff)
@app.route('/library')
def library():
	title="Library"
	item=Library.query.filter_by().all()
	return render_template('home.html',item=item,title=title)
@app.route('/module')
def mod():
	title="Modules"
	item= Module.query.filter_by().all()
	return render_template('home.html',item=item,title=title)
@app.route('/framework')
def fram():
	title="Framework"
	item=Framework.query.filter_by().all()
	return render_template('home.html',item=item,title=title)
app.run()












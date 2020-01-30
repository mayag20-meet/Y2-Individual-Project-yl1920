from model import Base, User, Challange
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, name, year, password):
	user_object = User(
		username = username,
		name = name,
		password = password,
		year = year,
		challanges = "no challanges yet")
	session.add(user_object)
	session.commit()

def verify_user(u, p):
	user = session.query(
		User).filter_by(
		username=u,
		password=p).all()
	if len(user)==1:
		return True
	else:
		return False

def profile(uname): 
	loggedin = session.query(
		User).filter_by(
		username=uname).first()
	name=loggedin.name
	year=loggedin.year
	challanges=loggedin.challanges
	return [name, year, challanges]
   
def upload_challange(category, name, description):
	challange_object = Challange(
		category = category,
		name = name, 
		description = description)
	session.add(challange_object)
	session.commit()

def querry_all_u():
	users=session.query(User).all()
	return users

def querry_all_c():
	challanges=session.query(Challange).all()
	return challanges

# def get_user():	

# def edit_user():


# def join_challange():

# def leave_challange():

# def edit_challange():

# add_user("mayag", "maya", 2003, "1234mtlg")
# add_user("inihohs", "shohini", 1998, "hello")
# print(verify_user("mayag", "1234mtlg"))
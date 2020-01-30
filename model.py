from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	username = Column(String, primary_key=True)
	name = Column(String)
	password = Column(String)
	year = Column(Integer)
	challanges = Column(String)

	def __repr__(self):
		listu = [self.username, self.name, self.password, self.year, self.challanges]
		return str(listu)


class Challange(Base):
	__tablename__ = 'challanges'
	id = Column(Integer, primary_key=True)
	category = Column(String)
	name = Column(String)
	description = Column(String)
	# location = Column(String)

	def __repr__(self):
		listc = [self.category, self.name, self.description]
		return str(listc)
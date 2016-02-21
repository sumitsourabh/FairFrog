from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


Base = declarative_base()

#pic_name,Product_name,Brand_name,price,Discount,description,color,size
#You will use this secret key to create and verify your tokens
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    #Add a method to generate auth tokens here
    
    #Add a method to verify auth tokens here

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    pictureLink = Column(String(250))
    name = Column(String(50))
    brandName = Column(String(100))
    availColors = Column(String)
    availSizes = Column(String(20))
    category = Column(String(30))
    price = Column(String(5))
    discount = Column(String(5))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'pictureLink' : self.pictureLink,
            'name' : self.name,
            'brandName' : self.brandName,
            'availColors' : self.availColors,
            'AvailSizes' : self.availSizes,
            'category' : self.category,
            'price' : self.price,
            'discount' : self.discount
        }

engine = create_engine('mysql:///demoDB.db')
 

Base.metadata.create_all(engine)

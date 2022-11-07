import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    LastName = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'Followers'
    id = Column(Integer, primary_key=True)
    User_from_Id = Column(Integer, ForeignKey('User.id'))
    User_to_Id = Column(Integer, ForeignKey('User.id'))
    Followers = relationship(User)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    User_Id = Column(Integer, ForeignKey('User.id'))
    Post = relationship(User)

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    Comments = relationship(Post)

class Like(Base):
    __tablename__ = 'Like'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    Like = relationship(Post)

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.id'))
    Media = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
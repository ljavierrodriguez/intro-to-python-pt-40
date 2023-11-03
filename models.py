from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)
    created_at = Column(DateTime(), default=datetime.now())
    
    
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    content = Column(Text(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    
""" 
-- users

CREATE TABLE users (
    id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(120) NOT NULL,
    password VARCHAR(120) NOT NULL,
    active Boolean default true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE (username)
);

CREATE TABLE notes (
    id INTEGER NOT NULL AUTO_INCREMENT,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


"""
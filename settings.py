from flask import Flask
app = Flask(__name__)

#Path to store database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Development\Python\Interviews\WeOrgPlatformChallenge\puppies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

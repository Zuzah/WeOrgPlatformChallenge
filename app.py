from flask import Flask, render_template, url_for
from flask import jsonify, request, Response
from datetime import datetime
#The Flask application object with __main__ entry
#app = Flask(__name__) #app object  now resides in settings.py

from settings import *

#import jwt

#TODO: use BluePrints, don't just house all the routes like below

print(__name__)

#Test data

#Hard-Coded User data
puppy_data =  [
    {
        'user_token': 1,
        'post_id': 1,
        'date_created': 'Fri, 8 Feb 2019 20:07:04 GMT',
        'likes': 0,
        'img_src': 'puppy1.png',
        'message': 'Picture of my first ever puppy'

    },

    {
        'user_token': 1,
        'post_id': 2,
        'date_created': 'Sat, 9 Feb 2019 20:07:04 GMT',
        'likes': 0,
        'img_src': 'puppy2.png',
        'message': 'Picture of my 2nd ever puppy'


    },

    {
        'user_token': 2,
        'post_id': 1,
        'date_created': 'Sun, 10 Feb 2019 20:07:04 GMT',
        'likes': 5,
        'img_src': 'puppy_cute.jpg',
        'message': 'A picture of a puppy I saw yesterday'


    }
]

#Mock POST json request for User (Test via POSTMAN app to http://localhost:5000/puppies)
#{
#    "user_token": 1,
#    "post_id": 4,
#    "likes": 1,
#    "img_src": "newPup.gif",
#    "message": "Really nice picture",

#}


user_data =  [
    {
        'first_name':'Lauren',
        'last_name': 'Carmichael',
        'email': 'larmichael@WePuppies.org',
        'user_id': 'lcarmichael',
        'user_token': 1
    },
    {
        'first_name':'Murtaza',
        'last_name': 'Hasni',
        'email': 'mhasni@WePuppies.org',
        'user_id': 'mhasni',
        'user_token': 2

    }
]

#Mock POST json request for User (Test via POSTMAN app to http://localhost:5000/users)
#{
#        "first_name":"Dan",
#        "last_name": "kuzmicki",
#        "email": "dkuzmicki@WePuppies.org",
#        "user_id": "dkuzmicki",
#        "user_token": 3
#}

#Login routes
#============================
@app.route('/login')
#def get_jwt_token():
    #Var for expiry date of the token
    #token = jwt.encode({'exp':}, app.config['SECRET_KEY'], algorithm='HS256')
    #return token

#Default Routes
#=============================

#route decorator for index
@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
   #Jinja2 Template for /Index
   return render_template('index.html', title="Options", text="Select one of the following options to perform")
   #return render_template('index.html')

#'Puppies' Content Routes
#==============================

#GET request for /puppies (will list all posts)
@app.route('/puppies')
@app.route('/puppies/')
def get_users():
    return jsonify({'puppy_data':puppy_data})

#GET request to retrieve Puppy Posts by User: /users/{value} "Fetch a users feed" TODO: ordered by date
@app.route('/puppies/<int:user_token>')
def get_user_by_token(user_token):
    #List var to hold any dictionary data containing the user's posts
    return_data = []

    #For data in the user_data dictionary
    for post in puppy_data:
        #IF the user_data.user_token value matches the token passed via POST
        if post["user_token"] == user_token:

            #TODO: Assign all dictionary content where user_toke is found
            #Then assign that users's data to dictionary
            return_data.append( {
                'user_token': post["user_token"],
                'post_id': post["post_id"],
                'img_src': post["img_src"],
                'message': post["message"],
                'likes': post["likes"],
                'date_created': post["date_created"],
            })
    #IF data exists for specified user
    if bool(return_data):
        #Then return the user data + http response 201 as json
        return jsonify(return_data)


        #TODO: Swap this back before PROD in to return just 201 response
        #response = Response("",201,mimetype='application/json')
        #return response

    else:
        #Else return no such user data
        return "UserID does not exsist"


#POST request to ADD a new user
@app.route('/puppies', methods = ['POST'])
def add_puppies_post():

    request_data = request.get_json() #Grab the json data that is sent via POST

    #Test to confirm data is read
    #return jsonify(request_data)

    #filtered data related to user_token from request_data

    #TODO: create a seperate class 'Post' that defines this
    #      THEN do a = Post()


    #TODO: I assume user_token or data is provided via post method

    #for the data currently in puppy pata
    #for data in puppy_data:
        #for the key/values in the data
        #for k, v in data.items():

            #if(k=='post_id'):
                #print(k,v)

    #If there is request data to process:
    if bool(request_data):

        new_post = {

            "user_token": request_data["user_token"],
            "post_id": request_data["post_id"],
            "img_src": request_data["img_src"],
            "message": request_data["message"],
            "date_created": datetime.now(),
            "likes": 0

        }

        #Update or Insert the dictionary
        puppy_data.insert(0,new_post)

        #Return with http 201 response "able to create"
        response = Response("",201,mimetype='application/json')
        return response

        #test of return value that is to be created
    #return jsonify(puppy_data) #test to ensure data is accepted

    else:
        #Return a 409 error: unable to create
        response = Response("",409,mimetype='application/json')
        return response

#PUT method to LIKE a post (a type of Update)
app.route('/puppies/<int:user_token>/<int:likes>', methods = ['PUT'])
def likePuppyPost(user_token, likes):
    pass

#Route decorator for Error Handling
@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404


#Depoyment settings for app (port, prod/dev)
if __name__ == "__main__":
    #Debug Mode
    app.run(host='127.0.0.1', debug = True, port = 5000)
    #Prod Mode
    #app.run()

from flask import Flask, render_template, url_for
from flask import jsonify, request
from datetime import datetime

#Test data

#Hard-Coded User data
puppy_data =  [
    {
        'user_token': 1,
        'post_id': 1,
        'date_created': '2012-04-23T18:25:43.511Z',
        'date_edited': '2012-04-23T18:25:43.511Z',
        'likes': 0,
        'img_src': 'puppy1.png',
        'message': 'Picture of my first ever puppy'

    },

    {
        'user_token': 1,
        'post_id': 2,
        'date_created': '2013-04-23T18:25:43.511Z',
        'date_edited': '2013-04-23T18:25:43.511Z',
        'likes': 0,
        'img_src': 'puppy2.png',
        'message': 'Picture of my 2nd ever puppy'


    },

    {
        'user_token': 2,
        'post_id': 1,
        'date_created': '2012-04-23T18:25:43.511Z',
        'date_edited': '2012-04-23T18:25:43.511Z',
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


#The Flask application object with __main__ entry
app = Flask(__name__)
print(__name__)

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

#User Routes
#==============================

#GET request for /users
@app.route('/puppies')
@app.route('/puppies/')
def get_users():
    return jsonify({'puppy_data':puppy_data})

#GET request to retrieve Puppy Posts by User: /users/{value}
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
                'likes': post["likes"]
            })
    #IF data exists for specified user
    if bool(return_data):
        #Then return the user data
        return jsonify(return_data)

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

    new_post = {

        "user_token": request_data["user_token"],
        "post_id": request_data["post_id"],
        "img_src": request_data["img_src"],
        "message": request_data["message"],
        "date_created": datetime.now(),
        "date_edited": datetime.now(),

    }

    puppy_data.append(new_post)

    #Return the entire data
    return jsonify(puppy_data)

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

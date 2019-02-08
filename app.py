from flask import Flask, render_template, url_for
from flask import jsonify, request

#Test data

#User data

user_data =  [
    {
        'first_name':'Dan',
        'last_name': 'kuzmicki',
        'email': 'dkuzmicki@WePuppies.org',
        'user_id': 'dkuzmicki',
        'user_token': 1
    },
    {
        'first_name':'Murtaza',
        'last_name': 'Hasni',
        'email': 'dhasni@WePuppies.org',
        'user_id': 'mhasni',
        'user_token': 2

    }
]

#1. The Flask application object with __main__ entry
app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('/index')
def index():
   #Jinja2 Template for /Index
   return render_template('index.html', title="Options", text="Select one of the following options to perform")
   #return render_template('index.html')

#GET request for /users
@app.route('/users')
def get_users():
    return jsonify({'user_data':user_data})


#GET request /users/{value}
@app.route('/users/<int:user_token>')
def get_user_by_token(user_token):
    return_user = {} #Empty dict object
    for user in user_data:
        if user["user_token"] == user_token:
            return_user = {
                'first_name': user["first_name"],
                'email': user["email"]
            }
    return jsonify(return_user)

#Error Handling
@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404


#Depoyment settings for app (port, prod/dev)
if __name__ == "__main__":
    #Debug Mode
    app.run(debug = True, port = 5000)
    #Prod Mode
    #app.run()

from flask import Flask, render_template, url_for

#1. The Flask application object with __main__ entry
app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('/index')
def index():
   #Jinja2 Template for /Index
   return render_template('index.html', title="Options", text="Select one of the following options to perform")
   #return render_template('index.html')

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

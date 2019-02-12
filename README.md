
# WE Movement Take-home Exercise

## Puppies API


The purpose of this exercise is to give us an understanding of your capabilities around API and
data modelling, and to have a project that we can collaborate on during the on-site portion of
the interview. We do this so we have a chance to work together with you on something you’re
already familiar with.

Use whatever programming language and framework you’re the most comfortable with.
There’s no time limit, but we’d prefer you don’t spend more than **4-5 hours** on it; we’re happy
to discuss anything you didn’t get to doing in the on-site portion.

## The Project
WE is considering building an app called Puppies. The purpose of this app is for people to be
able to share pictures of their dogs, in a style similar to Instagram.
To get this app going, we will need an API to power it; the Puppies API. It’s up to you to build it.
These are the capabilities we’re hoping the full API will eventually have, we’d like to see 4-5
built for this task. Your API might have the ability to:

 - Create a user: They should have a name and an email
 -  Authenticate a user (sign in)
 - Create a post: They should have an image, some text content, and a date
 -  Like a post
 - Fetch a user’s feed: A list of all posts, ordered by date (newest first)
 - Fetch details of an individual post
 - Fetch a user’s profile
 - Fetch a list of the user’s liked posts
 - Fetch a list of posts the user made

To prove that the API is working, please include some tests to verify critical functionality.
Please provide in the project README:
-  Instructions for project setup:
	- all steps needed to get it running
	- steps for how to run the tests
- Any highlights or portions you’re particularly happy or proud of
- Any caveats or limitations of the implementation or design of the API

Feel free to email your recruiter if you have any questions

## Requirements

- Python 3.4+
- Flask 1.0 (pip install flask)
- SQLAlchemy (pip install flask_sqlalchemy)
- Postman: https://www.getpostman.com/downloads/

# Development Tools
- HTML5 and Static Content via http://www.initializr.com/
- Atom IDE

# Solutions

i. Run the db_create script to create sqlite database tables:
```bash
python db_create.py
```

ii. "Create a Post": Done by making an api to handle POST request containing new content:
- use url: http://localhost:5000/Puppies
- Using Postman send a request with json data for a new post:
```json
{
    "user_token": 1,
    "post_id": 5,
    "img_src": "newPupV4.gif",
    "message": "Puppy that I found"
}
```

# TODO:

- Fix date format to be consistant style
- Order content feed by date
- Implement PUT method for user + like

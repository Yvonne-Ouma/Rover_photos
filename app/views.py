from flask import render_template
from app import app
from .request import get_photos

#views 
@app.route('/')
def index():

    '''

    # view root page that returns the index page and its data
    '''

    '''
    get all photos

    '''
    photos = get_photos()
    print(photos)
    return render_template('index.html', all_photo = photos)


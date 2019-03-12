from app import app
import urllib.request,json
from .models import photo

Photo = photo.Photo

#getting api key
api_key = app.config['NASA_API_KEY']

#getting the photo base url
nasa_url = app.config["NASA_API_URL"]

def get_photos():
    '''
    Function that gets the json response to our url request
    '''
    get_photos_url = nasa_url.format(api_key)

    with urllib.request.urlopen(get_photos_url) as url:
        get_photos_data =url.read()
        get_photos_response = json.loads(get_photos_data)

        photos_results = None

        if get_photos_response['photos']:
            photo_results_list = get_photos_response['photos']
            photo_results = process_results(photo_results_list)

    return photo_results

def process_results(photo_list):
    '''
    Function  that processes the photo result and transform them to a list of Objects

    Args:
        photo_list: A list of dictionaries that contain photo details

    Returns :
        photo_results: A list of photo objects
    '''
    photo_results = []
    for photo_item in photo_list:
        id = photo_item.get('id')
        camera = photo_item.get('camera')
        img_src = photo_item.get('img_src')
        earth_date = photo_item.get('earth_date')
        rover = photo_item.get('rover')

        
        
        
        if earth_date:
            photo_object = Photo(id,img_src,camera,earth_date,rover)
            photo_results.append(photo_object)

    return photo_results


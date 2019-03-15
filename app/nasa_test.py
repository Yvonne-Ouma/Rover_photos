import unittest
from models import photo
Photo = photo.Photo

class PhotoTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Photo class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_photo = Movie(1234,'https://image.tmdb.org/t/p/w500/khsjha27hbs','yvonne','2012-08-08','ouma')

# we the isinstance() function that checks if the object self.new_photo is an instance of the Photo class.

    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo,Photo))


if __name__ == '__main__':
    unittest.main()
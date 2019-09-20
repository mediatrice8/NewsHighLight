import unittest
from app.models import Source

class TestNews(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_source = Source('abc','liz','https://abc.com/','abc news is the best source', 'usa', 'general', 'abc-news')
    
    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_source,Source))
    
    def test_to_check_instance_variables(self):
        '''
        '''
        self.assertEquals(self.new_source.name,'abc')
        self.assertEquals(self.new_source.url,'https://abc.com/')
        self.assertEquals(self.new_source.description,'abc news is the best source')
        self.assertEquals(self.new_source.country,'usa')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.id,'abc-news')
        
        
        


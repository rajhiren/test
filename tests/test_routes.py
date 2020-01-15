from app import app
import unittest

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'

    def test_results(self):
        rv = self.app.get('/results')
        assert rv.status == '200 OK'

    def test_result_id(self):
        rv = self.app.get('/result/1')
        assert rv.status == '200 OK'

    def test_survey(self):
        rv = self.app.get('/survey')
        assert rv.status == '200 OK'


    def test_stat(self):
        rv = self.app.get('/stat/1')
        assert rv.status == '404 NOT FOUND'

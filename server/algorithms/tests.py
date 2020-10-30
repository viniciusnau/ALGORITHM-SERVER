from django.test import TestCase
from rest_framework import routers
from django.urls import resolve
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.utils.encoding import force_text
from django.utils import translation

from algorithms.views import algorithm_view


class AlgorithmsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_positive_algorithms(self):
        url = "http://0.0.0.0:8000/1/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'extenso': 'um'}
        )
        self.assertJSONEqual(force_text(response.content), {'extenso': 'um'})
    
    def test_negative_algorithms(self):
        url = "http://0.0.0.0:8000/-1/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'extenso': 'menos um'}
        )
        self.assertJSONEqual(force_text(response.content), {'extenso': 'menos um'})

    def test_algorithms_func(self):
        url = "http://0.0.0.0:8000/99999/"
        response = self.client.get(url)
        self.assertEqual(response.resolver_match.func, algorithm_view)
        self.assertEqual(response.resolver_match.func.__name__, algorithm_view.__name__)

    def test_invalid_request(self):
        response = self.client.get('http://0.0.0.0:8000/invalid-request/', HTTP_ACCEPT_LANGUAGE='en')
        self.assertEqual(response.content, b'\n<!doctype html>\n<html lang="en">\n<head>\n  <title>Not Found</title>'
                                           b'\n</head>\n<body>\n  <h1>Not Found</h1><p>The requested resource was not'
                                           b' found on this server.</p>\n</body>\n</html>\n')

    def test_language_using_override(self):
        with translation.override('en'):
            response = self.client.get('http://0.0.0.0:8000/0/')
        self.assertEqual(response.content, b'{"extenso": "zero"}')

    def test_language_using_header(self):
        response = self.client.get('http://0.0.0.0:8000/-99999/', HTTP_ACCEPT_LANGUAGE='en')
        self.assertEqual(response.content, b'{"extenso": "menos noventa e nove mil e novecentos e noventa e nove"}')

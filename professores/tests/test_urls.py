from typing import Text
from django.http import response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from professores.views import index

class ProfessoresURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """teste se a home da aplicacao utiliza a funcao index da view"""
        request = self.factory.get("/")
        with self.assertTemplateUsed("index.html"):        
            #root = reverse('/')
            response = index(request)
            #self.assertEqual(root.func, index)
            self.assertEqual(response.status_code,200)
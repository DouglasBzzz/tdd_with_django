from professores.models import Professor
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from professores.models import models


class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.professor = Professor.objects.create(
            nome_professor = "Douglas",
            formacao = "Pós-Graduado",
            tempo_de_experiencia_em_anos = "2",
            area_de_atuacao = "G. Projetos e Dados"
        )


    def test_index_view_retorna_dados_professor(self):
        """teste que verifica se a index retorna os dados do professor pesquisado"""
        response = self.client.get("/", 
            {
                "buscar":"Douglas"
            }
        )
        dados_professor_pesquisado = response.content["caracteristicas"] 
        self.assertIs(type(response.context["caracteristicas"]), QuerySet)
        self.assertEqual(dados_professor_pesquisado[0].nome_professor, "Douglas")

    #def 

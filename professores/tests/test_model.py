from django.test import TestCase, RequestFactory
from professores.models import Professor

class ProfessorModelTestCase(TestCase):
    def setUp(self):
        self.professor = Professor.objects.create(
            nome_professor = "Géri",
            formacao = "Mestre",
            tempo_de_experiencia_em_anos = "25",
            area_de_atuacao = "Desenvolvimento"
        )
    
    def test_professor_cadastrado_com_caracteristicas(self):
        """verifica se o professor cadastrado possui caracteristicas no banco de dados"""
        self.assertEqual(self.professor.nome_professor, "Géri")
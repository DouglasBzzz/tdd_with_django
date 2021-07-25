from django.test import LiveServerTestCase
from selenium import webdriver
from professores.models import Professor
#import time

#antes de executar o teste, tem algumas acoes...
class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/doug/OneDrive/Mater Dei/2021/segundo_semestre/inovacao_desafios/TDD/pratica/django/tdd_busca_animal/setup/chromedriver")
        self.professor = Professor.objects.create(
            nome_professor = "Maicon",
            formacao = "Pós-Graduado",
            tempo_de_experiencia_em_anos = "2",
            area_de_atuacao = "Desenvolvedor"
        )

    def tearDown(self):
        """subimos o webdriver, fazemos os testes, e depois a gente mata o navegador"""
        self.browser.quit()

    """
    def test_verifica_se_janela_do_browser_esta_ok(self):
        self.browser.get("http://www.materdei.edu.br/pt")
        # quando rodamos um teste, ele cria um database para executar os testes, ele checa os erros, e se nada for encontrado, ele vira um (.) 
    """
    def test_abre_janela_do_chrome(self):
        """aqui executamos os testes na instancia do servidor."""
        self.browser.get(self.live_server_url)
    
    """
    def test_que_falha(self):
        #este teste foi concebido para ser executado com falha
        self.fail("este teste deu ruim fera")
    """

    def test_buscando_novo_professor(self):
        """
        Testa se um usuário consegue encontrar um professor na pesquisa. 
        """
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector(".navbar")
        self.assertEqual("Busca Professor", brand_element.text)

        buscar_professor_input = self.browser.find_element_by_css_selector("input#busca-professor")
        self.assertEqual(buscar_professor_input.get_attribute("placeholder"),"Exemplo: Géri")

        buscar_professor_input.send_keys("Cleyton")
        #time.sleep(2)
        self.browser.find_element_by_css_selector("form button").click()

        dados_professor = self.browser.find_elements_by_css_selector(".result-description")
        self.assertGreater(len(dados_professor), 3)


        pass


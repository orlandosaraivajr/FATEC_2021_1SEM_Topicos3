from django.test import TestCase
from feriado.models import FeriadoModel
from datetime import datetime

class TestView_SemFeriado_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Feriado')
        self.assertContains(self.resp, 'Não é feriado')

    def test_template_mostra_feriado(self):
        self.assertTemplateUsed(self.resp, 'mostra_feriado.html')

from datetime import date
class TestView_ComFeriado_Test(TestCase):
    def setUp(self):
        hoje = date.today()
        self.cadastro = FeriadoModel(
            nome='Dia do Saci Pererê',
            dia=hoje.day,
            mes=hoje.month,
        )
        self.cadastro.save()
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Feriado')
        self.assertContains(self.resp, 'Dia do Saci Pererê')

    def test_template_mostra_feriado(self):
        self.assertTemplateUsed(self.resp, 'mostra_feriado.html')



class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado,
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)
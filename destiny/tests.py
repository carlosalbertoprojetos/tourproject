from unicodedata import name
from django.test import TestCase

from .models import Destiny


class TesteCreateDestiny(TestCase):
    
    def setUp(self):
        Destiny.objects.create(
        name = 'Minas',
        state = 'MG',
        city = 'Ibié'
        )
        
    def test_novo_destino_criado(self):
        destiny = Destiny.objects.get(name='Minas')
        self.assertEquals(destiny.__str__(), 'Minas: Ibié/MG')
        self.assertEquals(destiny.city_state(), 'Ibié/MG')

        print(
            'Nome:', destiny.name,'\n'
            'Estado:', destiny.state,'\n'
            'Cidade:', destiny.city,'\n'
        )
from unittest import TestCase
from unittest.mock import Mock, patch, call
from app.Navio import Navio

class TestNavio(TestCase):

    @patch('app.Navio.Navio.verificar_posicao')
    def test_navio(self, mock_verificar_posicao):
        navio = Navio()
        retorno_verificar = Mock()
        mock_verificar_posicao.return_value = retorno_verificar

        condicao1 = navio.verificar_posicao('PortaAvioes', 'A1', 'A5')
        mock_verificar_posicao.assert_called_with('PortaAvioes', 'A1', 'A5')

        condicao2 = navio.verificar_posicao('PortaAvioes', 'A1', 'A6')
        condicao3 = navio.verificar_posicao('PortaAvioes', 'A1', 'E1')
        condicao4 = navio.verificar_posicao('PortaAvioes', 'A1', 'E5')
        condicao5 = navio.verificar_posicao('Submarino', 'A1', 'A1')
        mock_verificar_posicao.assert_has_calls([call('PortaAvioes', 'A1', 'A6'),
                                                 call('PortaAvioes', 'A1', 'E1'),
                                                 call('PortaAvioes', 'A1', 'E5'),
                                                 call('Submarino', 'A1', 'A1')])

        self.assertIsInstance(navio, Navio)
        self.assertEqual(condicao1, retorno_verificar)
        self.assertEqual(condicao2, retorno_verificar)
        self.assertEqual(condicao3, retorno_verificar)
        self.assertEqual(condicao4, retorno_verificar)
        self.assertEqual(condicao5, retorno_verificar)

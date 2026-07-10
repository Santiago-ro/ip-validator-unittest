import unittest
from validar_ip import es_ip_valida

class TestValidarIP(unittest.TestCase):
    
    def test_ip_valida_estandar(self):
        self.assertTrue(es_ip_valida("192.168.1.1"))
        self.assertTrue(es_ip_valida("8.8.8.8"))

    def test_ip_con_octeto_mayor_a_255(self):
        self.assertFalse(es_ip_valida("256.1.1.1"))
        self.assertFalse(es_ip_valida("192.168.300.1"))

    def test_ip_con_letras(self):
        self.assertFalse(es_ip_valida("192.168.1a.1"))
        self.assertFalse(es_ip_valida("abc.def.ghi.jkl"))

    def test_ip_con_diferente_numero_de_partes(self):
        self.assertFalse(es_ip_valida("192.168.1"))
        self.assertFalse(es_ip_valida("192.168.1.1.1"))

    def test_ip_con_ceros_a_la_izquierda(self):
        self.assertFalse(es_ip_valida("192.168.01.1"))
        self.assertTrue(es_ip_valida("192.168.0.1"))

if __name__ == '__main__':
    unittest.main()
import unittest
import myIMC

class RoteiroTesteFuncional(unittest.TestCase):

    def test_ct01(self):
        res = myIMC.imc(50, 1.82)
        self.assertEqual(res,"Abaixo do peso")
    
    def test_ct02(self):
        res = myIMC.imc(50, 1.60)
        self.assertEqual(res,"Peso normal")

    def test_ct03(self):
        res = myIMC.imc(60, 1.43)
        self.assertEqual(res,"Acima do peso")
    
    def test_ct04(self):
        res = myIMC.imc(100, 1.81)
        self.assertEqual(res,"Acima do Peso(Obesidade)")

    def test_ct05(self):
        res = myIMC.imc(110, 1.64)
        self.assertEqual(res,"Acima do peso(Obesiidade grave)")
    
    def test_ct06(self):
        res = myIMC.imc(600.1, 1.72)
        self.assertEqual(res,"Entrada Inválida. Verifique os valores inseridos")

    def test_ct07(self):
        res = myIMC.imc(600.1, 1.72)
        self.assertEqual(res,"Entrada Inválida. Verifique os valores inseridos")

    def test_ct08(self):
        res = myIMC.imc(0.5, 1.80)
        self.assertEqual(res,"Entrada Inválida. Verifique os valores inseridos")
    
    def test_ct09(self):
        res = myIMC.imc(68, 1.69)
        self.assertEqual(res,"Peso normal")

    def test_ct010(self):
        res = myIMC.imc(78, 1.77)
        self.assertEqual(res,"Peso normal")

    def test_ct011(self):
        res = myIMC.imc(55, 1.80)
        self.assertEqual(res,"Abaixo do peso")

    def test_ct012(self):
        res = myIMC.imc(90, 3.1)
        self.assertEqual(res,"Entrada Inválida. Verifique os valores inseridos")
    
    def test_ct013(self):
        res = myIMC.imc(1, 0.40)
        self.assertEqual(res,"Abaixo do peso")

    def test_ct014(self):
        res = myIMC.imc(600, 3)
        self.assertEqual(res,"Acima do peso(Obesiidade grave)")
    def test_ct15(self):
        res = myIMC.imc("adffd", "abcd")
        self.assertEqual(res, "Entrada inválida. As entradas devem ser numéricas")
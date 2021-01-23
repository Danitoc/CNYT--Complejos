import unittest
import ComplexL as cl
import math


class TestStringMethods(unittest.TestCase):

    def test_sum(self):
        c1 = (7, -8)
        c2 = (5, 15)
        self.assertEqual(cl.SumaComplejos(c1, c2), (12, 7))

    def test_mul(self):
        c1 = (3, -2)
        c2 = (1, 2)
        self.assertEqual(cl.MultiplicacionComplejos(c1, c2), (7, 4))

    def test_res(self):
        c1 = (7, -2)
        c2 = (5, 15)
        self.assertEqual(cl.RestaComplejos(c1, c2), (2, -17))

    def test_mod(self):
        c = (3, 4)
        self.assertEqual(cl.ModuloComplejos(c), 25 ** 1/2)

    def test_conj(self):
        c = (3, 4)
        self.assertEqual(cl.ConjugadoComplejos(c), (3, -4))
        c1 = (3, -4)
        self.assertEqual(cl.ConjugadoComplejos(c1), (3, 4))

    def test_cp(self):
        c = (1, 1)
        self.assertEqual(cl.CartesianaPolar(c), (math.sqrt(2), math.pi/4))
        c1 = (1, math.sqrt(3))
        self.assertEqual(cl.CartesianaPolar(c1), ((4 ** 1/2), math.pi/3)) # PRESENTA ERROR

    def test_pc(self):
        p = (math.sqrt(2), math.pi/4)
        self.assertEqual(cl.PolaCartesiano(p), (1, 1)) # PRESENTA ERROR


if __name__ == '__main__':
    unittest.main()

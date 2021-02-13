import unittest
import ComplexL as cl


class TestStringMethods(unittest.TestCase):

    def test_SumaCompeljos(self):
        c1 = (7, -8)
        c2 = (5, 15)
        self.assertEqual(cl.SumaComplejos(c1, c2), (12, 7))

    def test_MultiplicacionComplejos(self):
        c1 = (3, -2)
        c2 = (1, 2)
        self.assertEqual(cl.MultiplicacionComplejos(c1, c2), (7, 4))

    def test_RestaComplejos(self):
        c1 = (7, -2)
        c2 = (5, 15)
        self.assertEqual(cl.RestaComplejos(c1, c2), (2, -17))

    def test_DivisionComplejos(self):
        c1 = (-2, 1)
        c2 = (1, 2)
        c3 = (0, 3)
        c4 = (-1, -1)
        self.assertEqual(cl.DivisionComplejos(c1, c2), (0.0, 1.0))
        self.assertEqual(cl.DivisionComplejos(c3, c4), (-1.5, -1.5))

    def test_ModuloComplejo(self):
        c = (3, 4)
        self.assertEqual(cl.ModuloComplejos(c), 25 ** 1 / 2)

    def test_ConjugadoComplejo(self):
        c = (3, 4)
        c1 = (3, -4)
        self.assertEqual(cl.ConjugadoComplejos(c), (3, -4))
        self.assertEqual(cl.ConjugadoComplejos(c1), (3, 4))

    def test_CartesianoPolar(self):
        self.assertEqual(cl.CartesianaPolar((1, 2)), (2.23606797749979, 63.43494882292201))
        self.assertEqual(cl.CartesianaPolar((-3, 1)), (3.1622776601683795, 18.43494882292201))
        self.assertEqual(cl.CartesianaPolar((2, 2)), (2.8284271247461903, 45.0))

    def test_PolarCartesiano(self):
        self.assertEqual(cl.PolaCartesiano((13, 23)), (11.966563094881725, 5.079504670360558))
        self.assertEqual(cl.PolaCartesiano((2, 120)), (-0.9999999999999996, 1.7320508075688774))
        self.assertEqual(cl.PolaCartesiano((1, 0)), (1, 0))

    def test_SumaVectores(self):
        self.assertEqual(cl.SumaVectores([(1, 2), (1, 2), (3, 5)], [(-2, 2), (2, 2), (4, 10)]), [(-1, 4), (3, 4), (7, 15)])
        self.assertEqual(cl.SumaVectores([(1, 0), (1, -2), (3, 2)], [(2, 2), (3, 2), (4, 5)]), [(3, 2), (4, 0), (7, 7)])

    def test_InversoAditivoVector(self):
        self.assertEqual(cl.InversoAditivoVec([(1, -1), (2, 3), (-1, 3)]), [(-1, 1), (-2, -3), (1, -3)])
        self.assertEqual(cl.InversoAditivoVec([(1, 2), (-3, 3), (-1, 3)]), [(-1, -2), (3, -3), (1, -3)])

    def test_VectorEscalar(self):
        self.assertEqual(cl.VecEscalar((-2, 1), [(4, 0), (-3, 0)]), [(-8, 4), (6, -3)])

    def test_SumaMatrices(self):
        mat1 = [[(1, -2), (3, 4)], [(1, 9), (6, 5)]]
        mat2 = [[(1, 1), (1, 2)], [(1, 3), [1, 5]]]
        mat3 = [[(1, 1), (2, -3)], [(4, 2), (2, 4)]]
        mat4 = [[(1, 0), (1, 0)], [(1, 0), (1, 0)]]
        self.assertEqual(cl.SumaMatrices(mat1, mat2), [[(2, -1), (4, 6)], [(2, 12), (7, 10)]])
        self.assertEqual(cl.SumaMatrices(mat3, mat4), [[(2, 1), (3, -3)], [(5, 2), (3, 4)]])

    def test_InversoAditivoMatriz(self):
        mat1 = [[(1, -2), (3, 4)], [(1, 9), (6, 5)]]
        self.assertEqual(cl.InversaAditMat(mat1), [[(-1, 2), (-3, -4)], [(-1, -9), (-6, -5)]])

    def test_EscalarPorMatriz(self):
        res1 = cl.EscalarPorMatriz((1, 1), [[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
        res2 = cl.EscalarPorMatriz((2, 3), [[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
        self.assertEqual(res1, [[(0, 2), (5, -1)], [(2, 6), (-2, 6)]])
        self.assertEqual(res2, [[(-1, 5), (13, 0)], [(2, 16), (-8, 14)]])

    def test_TraspuestaMatriz(self):
        res1 = cl.TraspuestaMat([[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
        res2 = cl.TraspuestaMat([[(1, 1), (2, -3), (5, 4)], [(4, 2), (2, 4), (4, 5)]])
        self.assertEqual(res1, [[(1, 1), (4, 2)], [(2, -3), (2, 4)]])
        self.assertEqual(res2, [[(1, 1), (4, 2)], [(2, -3), (2, 4)], [(5, 4), (4, 5)]])

    def test_ConjugadaVector(self):
        self.assertEqual(cl.ConjugadaVector([(1, -3), (2, 1)]), [(1, 3), (2, -1)])

    def test_ConjugadaMatriz(self):
        res1 = cl.ConjugadaMatriz([[(1, 2), (2, 1)], [(1, -2), (2, -3)], [(3, 4), (3, -1)]])
        res2 = cl.ConjugadaMatriz([[(1, 1), (2, 2), (1, 1)], [(2, 2), (3, -3), (2, 3)]])
        self.assertEqual(res1, [[(1, -2), (2, -1)], [(1, 2), (2, 3)], [(3, -4), (3, 1)]])
        self.assertEqual(res2, [[(1, -1), (2, -2), (1, -1)], [(2, -2), (3, 3), (2, -3)]])

    def test_AdjuntaMatriz(self):
        res1 = cl.AdjuntaMatTransConj([[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
        res2 = cl.AdjuntaMatConjTrans([[(1, 1), (2, 3)], [(4, 2), (1, 4)], [(1, 0), (3, -4)]])
        self.assertEqual(res1, [[(1, -1), (4, -2)], [(2, 3), (2, -4)]])
        self.assertEqual(res2, [[(1, -1), (4, -2), (1, 0)], [(2, -3), (1, -4), (3, 4)]])

    def test_MultiplicacionMatrices(self):
        mat1 = [[(3, 2), (1, 0), (4, -1)], [(0, 0), (4, 2), (0, 0)], [(5, -6), (0, 1), (4, 0)]]
        mat2 = [[(5, 0), (0, 0), (7, -4)], [(2, -1), (4, 5), (2, 7)], [(6, -4), (2, 0), (0, 0)]]
        self.assertEqual(cl.MultiplicacionMatrices(mat1, mat2), [[(26, -52), (9, 7), (48, -21)], [(60, 24), (1, 29), (15, 22)], [(26, 0), (14, 0), (20, -22)]])

    def test_ProductoInternoVectores(self):
        self.assertEqual(cl.ProductoInternoVectores([(1, 0), (0, 1), (1, -3)], [(2, 1), (0, 1), (2, 0)]), (5, 7))
        self.assertEqual(cl.ProductoInternoVectores([(1, -2), (-2, 1), (4, 3)], [(2, 1), (1, -3), (3, 0)]), (7, 1))

    def test_NormaMatriz(self):
        self.assertEqual(cl.NormaVector([(3, 0), (-6, 0), (-2, 0)]), 7.0)
        self.assertEqual(cl.NormaVector([(2, 0), (4, 0)]), 4.47213595499958)
        self.assertEqual(cl.NormaVector([(4, 0), (3, 0)]), 5.0)

    def test_DisstanciaVectores(self):
        res1 = cl.DistanciaVectores([(0, 0), (0, 0)], [(1, 1), (2, 4)])
        res2 = cl.DistanciaVectores([(1, 2), (2, 5)], [(2, 6), (5, 3)])
        self.assertEqual(res1, 4.69041575982343)
        self.assertEqual(res2, 5.477225575051661)

    def test_PruebaSiUnitaria(self):
        self.assertTrue(cl.PruebaSiUnitaria([[(1, 0), (0, 0)], [(0, 0), (1, 0)]]))

    def test_PruebaSiHermitiana(self):
        self.assertFalse(cl.PruebaSiHermitiana([[(1, 1), (0, 0)], [(0, 0), (1, -1)]]))
        self.assertTrue(cl.PruebaSiHermitiana([[(-1, 0), (0, -1)], [(0, 1), (1, 0)]]))
        self.assertTrue(cl.PruebaSiHermitiana([[(0, 0), (1, 0)], [(1, 0), (0, 0)]]))

    def test_ProductoTensorVectores(self):
        res1 = cl.ProductoTensorVectores([(-1, 0), (2, 0), (5, 0)], [(4, 0), (-3, 0)])
        res2 = cl.ProductoTensorVectores([(-1, 1), (2, -1), (5, 1)], [(4, 1), (3, 0)])
        self.assertEqual(res1, [(-4, 0), (3, 0), (8, 0), (-6, 0), (20, 0), (-15, 0)])
        self.assertEqual(res2, [(-5, 3), (-3, 3), (9, -2), (6, -3), (19, 9), (15, 3)])

    def test_ProductoTensorMatrices(self):
        mat1 = [[(3, 2), (0, 0), (2, 0)], [(5, -1), (12, 0), (4, 4)], [(0, 2), (6, -3), (9, 3)]]
        mat2 = [[(1, 0), (10, 2), (0, 0)], [(3, 4), (6, 0), (1, 0)], [(5, -7), (2, 5), (2, 9)]]
        self.assertEqual(cl.ProductoTensorMatrices(mat1, mat2), [[(3, 2), (26, 26), (0, 0), (0, 0), (0, 0), (0, 0), (2, 0), (20, 4), (0, 0)], [(1, 18), (18, 12), (3, 2), (0, 0), (0, 0), (0, 0), (6, 8), (12, 0), (2, 0)], [(29, -11), (-4, 19), (-12, 31), (0, 0), (0, 0), (0, 0), (10, -14), (4, 10), (4, 18)], [(5, -1), (52, 0), (0, 0), (12, 0), (120, 24), (0, 0), (4, 4), (32, 48), (0, 0)], [(19, 17), (30, -6), (5, -1), (36, 48), (72, 0), (12, 0), (-4, 28), (24, 24), (4, 4)], [(18, -40), (15, 23), (19, 43), (60, -84), (24, 60), (24, 108), (48, -8), (-12, 28), (-28, 44)], [(0, 2), (-4, 20), (0, 0), (6, -3), (66, -18), (0, 0), (9, 3), (84, 48), (0, 0)], [(-8, 6), (0, 12), (0, 2), (30, 15), (36, -18), (6, -3), (15, 45), (54, 18), (9, 3)], [(14, 10), (-10, 4), (-18, 4), (9, -57), (27, 24), (39, 48), (66, -48), (3, 51), (-9, 87)]])


if __name__ == '__main__':
    unittest.main()

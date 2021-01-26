import math as m

'''Para el uso de las sigueintes funciones se tiene en cuenta
que los parametros c1 y c2 hacen referencia a tuplas de numeros 
complejos.
'''


#                               Operaciones con numeros complejos


def SumaComplejos(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def MultiplicacionComplejos(c1, c2):
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1]


def RestaComplejos(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def DivisionComplejos(c1, c2):
    r1 = c1[0] * c2[0] + c1[1] * c2[1]
    r2 = c2[0] * c1[1] - c1[0] * c2[1]
    div = c2[0] ** 2 + c2[1] ** 2
    return r1 / div, r2 / div


def ModuloComplejos(c):
    return (c[0] ** 2 + c[1] ** 2) ** 1 / 2


def ConjugadoComplejos(c):
    return c[0], -c[1]


#                               Transformaciones entre Grados y Radianes


def GradosRad(dat):
    return (dat * m.pi) / 180


def RadGrados(dat):
    return (dat * 180) / m.pi


#                               Transformaciones entre Cartesianas y Polares


def CartesianaPolar(c):
    return m.sqrt(c[0] ** 2 + c[1] ** 2), RadGrados(m.atan2(c[1], abs(c[0])))


def PolaCartesiano(p):
    return p[0] * m.cos(GradosRad(p[1])), p[0] * m.sin(GradosRad(p[1]))


def fase(c):
    return m.atan2(c[1], c[0])


#                               Operaciones adicionales


def InvesoComplejo(c):
    return c[0] * -1, c[1] * -1


#                               Operaciones para vectores y matrices complejas


def SumaVectores(v1, v2):
    vec = list()
    for i in range(0, len(v1)):
        vec.append(SumaComplejos(v1[i], v2[i]))
    return vec


def InversoAditivoVec(v):
    vec = list()
    for i in range(0, len(v)):
        vec.append(InvesoComplejo(v[i]))
    return vec


def VecEscalar(e, v):
    vec = list()
    for i in range(0, len(v)):
        vec.append(MultiplicacionComplejos(e, v[i]))
    return vec


'''def SumaMatrices(m1, m2):'''



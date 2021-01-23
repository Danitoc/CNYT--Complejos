import math


def SumaComplejos(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def MultiplicacionComplejos(c1, c2):
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1]


def RestaComplejos(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def ModuloComplejos(c):
    return (c[0] ** 2 + c[1] ** 2) ** 1/2


def ConjugadoComplejos(c):
    return c[0], -c[1]


def CartesianaPolar(c):
    return math.sqrt(c[0] ** 2 + c[1] ** 2), math.atan2(c[1], c[0])


def PolaCartesiano(p):
    return p[0] * math.cos(p[1]), p[0] * math.sin(p[1])


"""Hace falta la funcion de division y la funcion de fase 
esperando respuesta del docente
"""
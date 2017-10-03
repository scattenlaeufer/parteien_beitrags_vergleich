#!/usr/bin/python3

import numpy
from matplotlib import pyplot

def die_linke(einkommen):
    beitrag = []
    for e in einkommen:
        if e == 0:
            b =+ 1.5
        elif e <= 500:
            b =+ 3
        elif e <= 600:
            b =+ 5
        elif e <= 700:
            b =+ 7
        elif e <= 800:
            b =+ 9
        elif e <= 900:
            b =+ 12
        elif e <= 1000:
            b =+ 15
        elif e <= 1100:
            b =+ 20
        elif e <= 1300:
            b =+ 25
        elif e <= 1500:
            b =+ 35
        elif e <= 1700:
            b =+ 45
        elif e <= 1900:
            b =+ 55
        elif e <= 2100:
            b =+ 65
        elif e <= 2300:
            b =+ 75
        elif e <= 2500:
            b =+ 85
        else:
            b =+ e * 0.04
        beitrag.append(b + 0.5)
    return beitrag

def make_graph():
    # einkommen = [e for e in range(2500)]
    einkommen = numpy.arange(0, 3000, 1)
    pyplot.figure()
    pyplot.plot(einkommen, die_linke(einkommen), 'r')
    # pyplot.show()
    pyplot.savefig('parteienbeitrag.png', bbox_inches='tight')

if __name__ == '__main__':
    make_graph()

#!/usr/bin/python3

import numpy
from matplotlib import pyplot, patches

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


def spd(einkommen):
    beitrag = []
    for e in einkommen:
        if e == 0:
            beitrag.append(2.5)
        elif e <= 1000:
            beitrag.append(5)
        elif e <= 2000:
            beitrag.append(7.5)
        elif e <= 3000:
            beitrag.append(25)
        elif e <= 4000:
            beitrag.append(45)
        else:
            beitrag.append(100)
    return beitrag


def spd_2(einkommen):
    beitrag = []
    for e in einkommen:
        if e == 0:
            beitrag.append(2.5)
        elif e <= 1000:
            beitrag.append(5)
        elif e <= 1000 + 1000 / 3:
            beitrag.append(7.5)
        elif e <= 1000 + 2000 / 3:
            beitrag.append(15)
        elif e <= 2000:
            beitrag.append(20)
        elif e <= 2000 + 1000 / 3:
            beitrag.append(25)
        elif e <= 2000 + 2000 / 3:
            beitrag.append(30)
        elif e <= 3000:
            beitrag.append(35)
        elif e <= 3000 + 1000 / 3:
            beitrag.append(45)
        elif e <= 3000 + 2000 / 3:
            beitrag.append(60)
        elif e <= 4000:
            beitrag.append(75)
        elif e <= 4000 + 1000 / 3:
            beitrag.append(100)
        elif e <= 4000 + 2000 / 3:
            beitrag.append(150)
        else:
            beitrag.append(250)
    return beitrag


def make_graph():
    # einkommen = [e for e in range(2500)]
    einkommen = numpy.arange(0, 5000, 1)
    color_die_linke = '#ff00ff'
    color_spd = '#ff0000'
    pyplot.figure()
    pyplot.plot(einkommen, die_linke(einkommen), color_die_linke, label='DIE LINKE')
    pyplot.plot(einkommen, spd_2(einkommen), color=color_spd, linestyle='dashed')
    pyplot.plot(einkommen, spd(einkommen), color_spd, label='SPD')
    pyplot.legend(handles=[patches.Patch(color=color_die_linke, label='DIE LINKE'),
                           patches.Patch(color=color_spd, label='SPD')])
    # pyplot.show()
    pyplot.savefig('parteienbeitrag.png', bbox_inches='tight')

if __name__ == '__main__':
    make_graph()

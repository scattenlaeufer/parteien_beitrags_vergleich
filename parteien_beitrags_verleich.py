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


def gruene(einkommen):
    beitrag = []
    for e in einkommen:
        beitrag.append(e * .01)
    return beitrag


def fdp(einkommen):
    beitrag = []
    for e in einkommen:
        b = e * 0.005
        if e <= 2600:
            if b < 8:
                b = 8
        elif e <= 3600:
            if b < 12:
                b = 12
        elif e <= 4600:
            if b < 18:
                b = 18
        else:
            if b < 24:
                b = 24
        beitrag.append(b)
    return beitrag


def make_graph():
    einkommen = [e for e in range(5000)]
    # einkommen = numpy.arange(0, 5000, 1)
    party_list = [[die_linke, '#ff00ff', None, 'DIE LINKE'],
                  [gruene, '#00ff00', None, 'GRÜNE'],
                  [spd, '#ff0000', None, 'SPD'],
                  [spd_2, '#ff0000', 'dashed', None],
                  [fdp, '#ffff00', None, 'FDP'],
                  ]
    pyplot.figure()
    label = []
    for party in party_list:
        if party[2]:
            pyplot.plot(einkommen, party[0](einkommen), party[1], linestyle=party[2])
        else:
            pyplot.plot(einkommen, party[0](einkommen), party[1], linestyle='solid')
        if party[3]:
            label.append(patches.Patch(color=party[1], label=party[3]))
    pyplot.legend(handles=label),
    # pyplot.show()
    pyplot.savefig('parteienbeitrag.png', bbox_inches='tight')

if __name__ == '__main__':
    make_graph()

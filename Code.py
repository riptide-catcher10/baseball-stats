import random

ab = int(input("how many ab's? "))
singles = int(input("how many singles? "))
doubles = int(input("how many doubles? "))
triples = int(input("how many triples? "))
homeruns = int(input("how many homeruns? "))
walks = int(input("how many walks? "))
hbp = int(input("how many hit by pitches? "))
sf = int(input("how many sarfice flys?"))
hits = singles + doubles + triples + homeruns
pa = ab + walks + sf
doubles_val = doubles * 2
triples_val = triples * 3
homeruns_val = homeruns * 4
tb = doubles_val + triples_val + homeruns_val + singles

def calc():
    avg = hits / ab
    obp = (hits + walks + hbp) / pa
    slg = tb / ab
    ops = obp + slg
    print(f'avg {float(round(avg, 3))}/onbase {float(round(obp,3))}/slg {float(round(slg, 3))}/ops {float(round(ops, 3))}')
calc()

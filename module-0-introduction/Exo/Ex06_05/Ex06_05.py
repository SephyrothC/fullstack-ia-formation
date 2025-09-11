str = 'X-DSPAM-Confidence: 0.8475'

Ipo = str.find(':')
print(Ipo)
piece = str[Ipo +1:]
print(piece)
valeur = float(piece)
print(valeur)
print(valeur+61)
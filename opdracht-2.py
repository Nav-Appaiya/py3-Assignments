import random
import numpy as np


def toppers(rapportcijfers, n = 3):
    dic = {"key 1": "value 1", "key b": "value b"}
    dici = {}

    dici = np.average(rapportcijfers)

    print dici




lijst = [];

leerlinglijst = [random.choice([3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10]) for _ in range(1000)]

for a in leerlinglijst:
    leerling1 = {
        'llnr': a,
        'nl': 7,
        'en': 8,
        'fr': 5,
        'wi': 6,
        'sk': 9,
        'na': 8,
        'ak': 4,
        'gs': 6,
        'bi': 10,
        'lo': 5
    }

    lijst.append(leerling1)


for l in lijst:
    print toppers(l)
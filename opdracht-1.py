import random
import numpy as np

def samenvatting(l):

    my_dict = {
        'N': len(l),        # Aantal waarnemingen
        'Min': min(l),      # kleinste waarde
        'Kw1': np.percentile(l, 25),      # eerste kwartiel
        'Mediaan': np.median(l),  # mediaan, ook wel tweede kwartiel  genoemd
        'Gem': np.average(l),      # gemiddelde
        'Sd': np.std(l),       # standaarddeviatie
        'Kw3': np.percentile(l, 75),      # derde kwartiel
        'Max': max(l),      # grootste waarde
    }

    return my_dict

# Lijst 10000 elementen gevuld met uniform(50,150)
intelligentie_data_1 = [random.uniform(50, 150) for _ in range (10000)]

# Lijst 10000 elementen gevuld met triangular(50,150,115)
intelligentie_data_2 = [random.triangular(50,150,115) for _ in range (10000)]

print samenvatting(intelligentie_data_1);
print samenvatting(intelligentie_data_2);
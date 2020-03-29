from datetime import datetime, date

CHAKRAS = dict(muladhara = 23.6884, 
               swadihshthana = 28.426125,
               manipura = 33.163812,
               anahatha = 37.901499,
               vishuddha = 42.6392,
               ajna = 47.3769,
               sahasrara = 52.1146)

#PHASE_DIFFERENCE = (200 / p) * Abs(Mod(d, p) - p / 2)

def bday_delta(bdate1, bdate2):
    date_user1 = datetime.strptime(bdate1, '%d.%m.%Y')
    date_user2 = datetime.strptime(bdate2, '%d.%m.%Y')
    days_user1 = datetime.now() - date_user1
    days_user2 = datetime.now() - date_user2
    delta = abs(days_user1 - days_user2).days
    return delta

def phase_diff (chakra, delta):
    compability = (200 / chakra) * abs(delta % chakra - chakra / 2)
    return round(compability)

def chakras_compability(delta):
    compability = dict()
    chakras_sum = 0
    for chakra, value in CHAKRAS.items():
        compability[chakra] = phase_diff(value, delta)
        chakras_sum += compability[chakra]
    compability['average'] = round(chakras_sum / 7)
    return compability

#delta = bday_delta('17.11.1998', '7.10.1998')
#print(chakras_compability(delta))
#{'muladhara': 46, 'swadihshthana': 12, 'manipura': 53, 'anahatha': 84, 'vishuddha': 92, 'ajna': 73, 'sahasrara': 57, 'average': 60}


from datetime import datetime, date

ARIES = [date(2000,3,21), date(2000,4,20)]
TAURUS = [date(2000,4,21), date(2000,5,21)]
GEMINI = [date(2000,5,22), date(2000,6,21)]
CANCER = [date(2000,6,22), date(2000,7,22)]
LEO = [date(2000,7,23), date(2000,8,22)]
VIRGO = [date(2000,8,23), date(2000,9,23)]
LIBRA = [date(2000,9,24), date(2000,10,23)]
SCORPIO = [date(2000,10,24), date(2000,11,22)]
SAGITTARIUS = [date(2000,11,23), date(2000,12,21)]
CAPRICORN1 = [date(2000,12,22), date(2000,12,31)]
CAPRICORN2 = [date(2000,1,1), date(2000,1,20)]
AQUARIUS = [date(2000,1,21), date(2000,2,19)]
PISCES = [date(2000,2,20), date(2000,3,20)]

def get_horoscope(bday):
    try:
        day = int(bday.split('.')[0])
        month = int(bday.split('.')[1])
        bday = date(2000,month,day)

        if ARIES[0] <= bday <= ARIES[1]:
            return 'ARIES'
        elif TAURUS[0] <= bday <= TAURUS[1]:
            return  'TAURUS'
        elif GEMINI[0] <= bday <= GEMINI[1]:
            return 'GEMINI'   
        elif CANCER[0] <= bday <= CANCER[1]:
            return 'CANCER'
        elif LEO[0] <= bday <= LEO[1]:
            return 'LEO'
        elif VIRGO[0] <= bday <= VIRGO[1]:
            return 'VIRGO'
        elif LIBRA[0] <= bday <= LIBRA[1]:
            return 'LIBRA'
        elif SCORPIO[0] <= bday <= SCORPIO[1]:
            return 'SCORPIO'
        elif SAGITTARIUS[0] <= bday <= SAGITTARIUS[1]:
            return 'SAGITTARIUS'
        elif CAPRICORN1[0] <= bday <= CAPRICORN1[1]:
            return 'CAPRICORN'
        elif CAPRICORN2[0] <= bday <= CAPRICORN2[1]:
            return 'CAPRICORN'
        elif AQUARIUS[0] <= bday <= AQUARIUS[1]:
            return 'AQUARIUS'
        elif PISCES[0] <= bday <= PISCES[1]:
            return 'PISCES'
    
    except ValueError:
        return None
        
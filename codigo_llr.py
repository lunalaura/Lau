def reditos( amount, anual_rate):
    reditos = (amount * anual_rate)/12 
    return round(reditos,2)

def isr (amount):
    totisr =((1.45/100) * amount)/12
    return round(totisr,2)

def calcular_fecha(def_fecha):
    from datetime import datetime
    datetime_object = datetime.strptime(def_fecha, '%d %m %Y ')
    datetime_object =datetime.strftime(datetime_object,'%Y-%m-%d')
    return datetime_object


print ('Cut off Date  Initial Capital Rate  Revenues  ISR  Accumulated Revenues')
i = 0
''' Valor de la inversion'''
amount = 1000

j =  reditos(amount,0.10) - isr (amount)
for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
    
    print(i ,calcular_fecha("2 " + str(i+1) + " 2019 "),' ', str(amount)+'            0.1    ', reditos(amount, 0.10), ' ' , isr(amount), ' ', round(j,2))
    j = j + reditos(amount,0.10) - isr(amount)
    i = i + 1

print (' ' ,'Total: ', j + 1000)

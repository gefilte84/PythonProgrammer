#input
print('###---Velkommen til HSN boligkalkulator---###')
print()
print('Tast 1 hvis du vet prisen på boligen du vil kjøpe.')
print('Tast 2 for å regne ut maksimalt lånebeløp.')
print()
kalkulator=int(input('Tast 1 eller 2: '))
print()

from tkinter import *
def beregn_lan():
    if kalkulator==1:
        boligpris=int(input('Hvor mye ønsker du å kjøpe for? '))
        #15% av kjøpesum
        boligpris_ek=(boligpris*0.15)

egenkapital=int(input('Hvor mye har du i egenkapital? '))
bruttoinntekt=int(input('Hva er din bruttoinntekt? '))
status=input('par eller enslig? ')
antall_barn=int(input('Skriv inn antall barn, 0-3? '))
print()



#Lånefaktor enslig
if status=='enslig':
 if bruttoinntekt<=300000:
    faktor=0
 elif bruttoinntekt<=450000:
    faktor=3
 elif bruttoinntekt<=650000:
    faktor=4
 elif bruttoinntekt<=900000:
    faktor=4.5
 elif bruttoinntekt<=1000000:
    faktor=5
 elif bruttoinntekt<=1200000:
     faktor=5.25
 else:
     faktor=5.25

#Lånefaktor gift
if status=='par':
 if bruttoinntekt<=450000:
    faktor=0
 elif bruttoinntekt<=650000:
    faktor=3
 elif bruttoinntekt<=900000:
    faktor=4.25
 elif bruttoinntekt<=1000000:
    faktor=5
 elif bruttoinntekt<=1200000:
    faktor=5.5
 else:
    faktor=5.75


#Beregning
    
#Barne trekk
if status=='enslig':
    barne_trekk=antall_barn*780000
else:
    barne_trekk=antall_barn*365000


#Beregninger for egenkapital

#Potensiell kjøpesum
makssummen=egenkapital/0.15    
#Potensiell lånebeløp
maksteo_sum=(egenkapital/0.15)-egenkapital
#Max teoretisk kjøpesum minus barn
makssum1=egenkapital/0.15-barne_trekk


#Beregninger for bruttoinntekt

#Maksum basert på bruttoinntekt
makssum_bi=(bruttoinntekt*faktor)
#Faktisk makslån
makssum_barn=(bruttoinntekt*faktor)-barne_trekk
#Maxsum med pluss egenkapital-barn
makssum_ek_barn=(bruttoinntekt*faktor)+egenkapital-barne_trekk
#Maxxerto
makssum_ek_barn2=(bruttoinntekt*faktor)-barne_trekk
#Maxsum med minus barn pluss egenkapital
makssum_ek=(bruttoinntekt*faktor)-barne_trekk+egenkapital
#makssum med egenkapital
makssum_ek2=(bruttoinntekt*faktor)+egenkapital

#Kalkulator 1 på if og Kalkulator 2 på else
if kalkulator==1:
    if egenkapital<boligpris_ek:
        print('Avslag. Du har ikke nok egenkapital for å ta dette lånet. Kravet for',boligpris,'er:',boligpris_ek)
        print()
    elif faktor<=0:
        print('Avslag. Bruttoinntekten er for lav.')
        print('Det kreves minimum bruttoinntekt på:')
        print('300.000,- for enslige')
        print('450.000,- for par')
        print()
    elif makssum_ek2<boligpris:
        print('Avslag. Bruttoinntekten er for lav.')
        print()
    elif makssum_ek2>boligpris and makssum_ek_barn<boligpris:
        print('Avslag. Du har fått avslag pågrunn av for mange barn')
        print()
    else:
        print('Godkjent. Du har fått lån på:',makssum_minus_ek,'forutsett at hele egenkapitalen på',egenkapital,'brukes')
        print('Lånet er beregnet på bakgrunn av:')
        print('Bruttoinntekt:',bruttoinntekt)
        print('Lånefaktor:',faktor)
        print('Egenkapital:',egenkapital)
        print('Trekk for barn:',barne_trekk)
        print()
else:
    if faktor<=0:
        print('Avslag. Bruttoinntekten er for lav.')
        print('Det kreves minimum bruttoinntekt på:')
        print('300.000,- for enslige')
        print('450.000,- for par')
        print()
if makssum_bi>=makssummen:
    print('Din maksimale kjøpesum blir:',format (makssum1,'.2f'),'og er basert på egenkapitalen')
    print('Ditt lån blir              :',format (maksteo_sum,'.2f'))
    print('Lånet er blitt beregntet på bakgrunn av:')
    print('Bruttoinntekt:',bruttoinntekt)
    print('Lånefaktor:',faktor)
    print('Egenkapital:',egenkapital)
    print('Trekk for barn:',barne_trekk)
else:
    print('Din maksimale kjøpesum blir:',format (makssum_ek_barn,'.2f'),'og er basert på bruttoinntekt')
    print('Ditt lån blir              :',format (makssum_ek_barn2,'.2f'))
    print('Lånet er blitt beregntet på bakgrunn av:')
    print('Bruttoinntekt:',bruttoinntekt)
    print('Lånefaktor:',faktor)
    print('Egenkapital:',egenkapital)
    print('Trekk for barn:',barne_trekk)
    

    
        


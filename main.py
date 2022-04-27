import pandas as pd

v = nvdbVegnett()

# Sett filbanen til der du har din csv fil lagret.
# (NB! Mulig feil kan være at filen ligger i One Drive!)
filename = 'C:/Users/DIN-BURKER/DIN/FIL-STI/TIL-FILA.csv'

# Definer hvilke felter du ønsker skal leses fra CSV filen. 
# Alle feltene utenom 'Koblingsnokkel' skal brukes til å bygge en streng, 'Vegsystemreferanse'.
fields = ['Koblingsnokkel', 'Veg_nr', 'Strekning_Delstrekning_fra', 'Km_fra', 'Km_til']

# Her leses filen og informasjon om de angitte feltene vil bli lagret i en dataframe. 
# sep=';' er skilletegnet mellom verdiene i csv filen
# low_memory=True gjør sånn at filen leses i deler.
# usecols=fields er feltene du definerte på linje 11. Dette er feltene som faktisk blir lest.
# skipinitialspace=True vil fjerne ekstra whitespace, ikke relevat i qgis. Men blir penere ved testing mot console output.
# filename er filen du definerte på linje 7.
df = pd.read_csv(filename,
                     skipinitialspace=True,
                     usecols=fields,
                     low_memory=True,
                     sep=';'
                     )
                     

# Her bygges vegsystemreferanse strengen. 
# Det er viktig at denne bygges riktig, da denne brukes direkte mot nvdbapiet. 
# Her må du passe på at rekkefølgen på de forskjellige verdiene ligger riktig. 
# Strengen du ønsker å bygge skal ha samme oppbyggning som denne: FV3358S1D1m2156-2568
# Du kan dele strengen opp i 6 deler "FV3358" "S1D1" "m" "2156" "-" "2568". 
# Her er det 4 variabler som du kan endre på, det er:
#   1. df['Veg_nr'] = FV3358
#   2. df['Strekning_Delstrekning_fra'] = S1D1
#   3. df['Km_fra'] = 2156
#   4. df['Km_til'] = 2568
# "m" og "-" bør ikke endres eller flyttes med mindre disse har blitt endret på hos NVDB.
df['Vegsystemreferanse'] = df['Veg_nr'] + \
                               df['Strekning_Delstrekning_fra'] + 'm' + \
                               df['Km_fra'].astype(str) + '-' + \
                               df['Km_til'].astype(str)

# På linje 48 til 67 gjøres en sjekk for å se om intervallet (eks: m2156-2568) er stigende.
# Om dette intervallet ikke er stigende vil du få en feilmelding og hele spørringen mot nvdb vil feile.
# Denne sjekken vil fjerne alle vegsystemreferanser hvor intervallet ikke er stigende for å forhindre dette.
# Brukeren vil få en melding i Python-konsollen om det er noen systemreferanser som er fjernet og hvilke det gjeler.
# Om du skulle oppleve å ha andre feil vil du få en feilmelding i Python-konsollen.

# Informasjonen fra 'Km_fra' og 'Km_til' kollonen blir lagt i hver sin liste.  
x, y = [], []
for i in df['Km_fra']:
    x.append(i)
for j in df['Km_til']:
    y.append(j)

index = 0
vegsystemreferanse = ''

# Listene blir sammenlignet og sjekket mot hverandre for å se om intervallet er stigende.
for (i, j) in zip(x, y):
    if i > j:
        # Om intervallet ikke er stigende vil raden fjernes fra dataframen og ikke brukes i spørringen mot nvdb.
        # Det vil si at denne dataen ikke vil havne i qgis.
        vegsystemreferanse = df['Vegsystemreferanse'].drop([index])
        print(df['Vegsystemreferanse'][index],
            'Ikke gyldig vegsystemreferanse. Intervall skal være stigend, eks: m0-100')
    index += 1

# Her gjøres spørringen mot nvdb.
v.filter({'vegsystemreferanse': vegsystemreferanse})
nvdbsok2qgis(v)

# qgis_vegsystemreferanser

Et Python script som benytter seg av NVDB api'et for å skrive vegsystemreferanser til QGIS. 

# Forutsetninger

For at scriptet skal fungere er det noen forutsetninger knyttet til programvare og ditt QGIS miljø. Da scriptet er laget for å fungere i QGIS sin Python editor. 

## QGIS

Scriptet er utviklet for å fungere i QGIS 3.16 LTS. Men fungerer mest sannsynlig fint i andre versjoner av QGIS også. Det anbefales ikke å bruke en versjon av QGIS eldre enn versjon 3.

## NVDB-API

For at scriptet skal kunne gjøre søk mot NVDB er det en forutsetning at du har satt opp miljøet i QGIS til å gjøre nettopp dette. Har du ikke gjort dette før eller er usikker på om du har gjort det tidligere kan du følge denne linken. https://github.com/LtGlahn/nvdbapi-V3/blob/master/README_qgis.md Her er det bare å følge stegene steg for steg. 
# Bruk

1.	Last ned koden ved å trykke på kode og pakk ut filene der du ønsker.

2.	I QGIS åpner du Python-konsollen 

![image](https://user-images.githubusercontent.com/46957821/165524326-25a914f9-e073-4556-b0c2-46bb1446cfb4.png)

3.	Så åpner du vinduet for redigering.

![image](https://user-images.githubusercontent.com/46957821/165524395-e217c965-3ee6-404f-b1ae-b942f6d593c2.png)

4.	Fra dette vinduet kan du åpne main.py filen. 

![image](https://user-images.githubusercontent.com/46957821/165524431-0da2bfec-20e8-4a2f-a53f-3006bf7fab43.png)
 
5.	Når du har åpnet main.py filen må du spesifisere hvilken fil du ønsker at scriptet skal lese og passe på at kolonene i filen matcher med de kolonene som bygger vegsystemreferanse strengen. 

6.	Når dette er gjort skal alt være klart.

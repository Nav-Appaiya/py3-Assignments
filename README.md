# py3-Assignments
Assignments for Python en Machine Learning


### Opdracht 1
Schrijf  een functie samenvatting(dataset) die van de dataset  (een list)  onder elkaar afdrukt:
```
N=....(aantal waarnemingen)
Min = .... (kleinste waarde)
Kw1= .... (eerste kwartiel)
Mediaan=.... (mediaan, ook wel tweede kwartiel  genoemd)
Gem=.... (gemiddelde)
Sd=.... (standaarddeviatie)
Kw3= (derde kwartiel)
Max=.... (grootste waarde)
```

Maak eerst zelf wat (kleine!) datasets om de functie te testen en run hem daarmee met:
Intelligentie_data_1: 10000 elementen gevuld met uniform(50,150)
Intelligentie_data_2: 10000 elementen gevuld met triangular(50,150,115)
Vergelijk de uitkomsten

### Opdracht 2
Schrijf een functie toppers(rapportcijfers, n=3) die van een list met rapportcijfers bepaalt wat de n beste leerlingen zijn (defaultwaarde=3). 
De functies geeft een lijst terug met tuples met een llnr en het gemiddelde, b.v. : (1206,6.8))
De elementen van de lijst zijn dicts met  de volgende structuur (voorbeeld):
`{'llnr': 1206, 'nl':7, 'en':8, 'fr':5, 'wi':6, 'sk':9, 'na':8, 'ak':4, 'gs':6, 'bi':10, 'lo':5}`
Vul de lijst met randomcijfers van 1000 leerlingen (llnr 1000 t.m. 1999) en gebruik hiervoor:
`choice([3,4,5,5,6,6,6,7,7,7,8,8,9,10])`
Bedenk een manier om je functie te testen.

### Opdracht 3
Scatterplots maken met matplotlib.pyplt om correlatie in te schatten.
http://matplotlib.org/users/pyplot_tutorial.html
We hebben een fictieve dataset met 30 records met 4 velden:
 Data
 Maak met mathplotlib scatterplots om te kijken tussen welke velden (een zekere mate van) correlatie is.

### Opdracht 4
Lijngrafieken van aantal timeseries (metingen: temperatuurmeting op verschillende locaties in Groene Poort), in één grafiek zetten met titel, getallen en eenheden op assen en legenda.
Vier sensoren meten om de 5 minuten de temperatuur bij de Groene Poort. We simuleren de meetdata van 1 dag met:

Zet in een grafiek het temperatuurverloop van de vier sensoren. Denk aan titel, legenda, beschrijving assen.
Er zitten door meetfouten outliers in de data.
Welke zijn dat?
Schrijf een kleine routine om die fouten eruit te halen en maak de grafiek opnieuw.
 
### Animals
Image result for olifant mug
 
bouw een systeem dat de gebruiker een aantal J/N-vragen stelt over dieren en tot slot een gokje waagt.
bijvoorbeeld:
Is het een insect? N
Is het soms een olifant? N
Wat was het dan? duif
Het systeem vraagt nu om een vraag die een kanarie en een olifant kan onderscheiden.
De gebruiker voert in: Kan het vliegen? (Dombo doet niet mee)
Het systeem heeft nu een beetje bijgeleerd.
Als je dit een aantal keer herhaalt, dan ontstaat er geleidelijk aan een systeem dat steeds meer dieren kan raden.


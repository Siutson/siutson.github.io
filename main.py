import folium
import pandas as pd

# pomiary

# sczytanie wartości z pliku .xls
valPogodno = pd.read_excel('pomiary/pogodno.xls') 
# obliczenie średniej wartości poziomu hałasu
valPogodno = 110 + (valPogodno["Sound pressure level (dB)"].mean()) 
# formowatowanie
valPogodno = '{:.2f}'.format(valPogodno) 

valSloneczne = pd.read_excel('pomiary/sloneczne.xls')
valSloneczne = 110 + (valSloneczne["Sound pressure level (dB)"].mean())
valSloneczne = '{:.2f}'.format(valSloneczne)

valPrzeclaw = pd.read_excel('pomiary/przeclaw.xls')
valPrzeclaw = 110 + (valPrzeclaw["Sound pressure level (dB)"].mean())
valPrzeclaw = '{:.2f}'.format(valPrzeclaw)

valMierzyn = pd.read_excel('pomiary/mierzyn.xls')
valMierzyn = 110 + (valMierzyn["Sound pressure level (dB)"].mean())
valMierzyn = '{:.2f}'.format(valMierzyn)

valGumience = pd.read_excel('pomiary/gumience.xls')
valGumience = 110 + (valGumience["Sound pressure level (dB)"].mean())
valGumience = '{:.2f}'.format(valGumience)

valSwierczewo = pd.read_excel('pomiary/swierczewo.xls')
valSwierczewo = 110 + (valSwierczewo["Sound pressure level (dB)"].mean())
valSwierczewo = '{:.2f}'.format(valSwierczewo)

valSikorskiego = pd.read_excel('pomiary/sikorskiego.xls')
valSikorskiego = 110 + (valSikorskiego["Sound pressure level (dB)"].mean())
valSikorskiego = '{:.2f}'.format(valSikorskiego)

valCentrum = pd.read_excel('pomiary/centrum.xls')
valCentrum = 110 + (valCentrum["Sound pressure level (dB)"].mean())
valCentrum = '{:.2f}'.format(valCentrum)

valGoclaw = pd.read_excel('pomiary/goclaw.xls')
valGoclaw = 110 + (valGoclaw["Sound pressure level (dB)"].mean())
valGoclaw = '{:.2f}'.format(valGoclaw)

valNiebuszewo = pd.read_excel('pomiary/niebuszewo.xls')
valNiebuszewo = 110 + (valNiebuszewo["Sound pressure level (dB)"].mean())
valNiebuszewo = '{:.2f}'.format(valNiebuszewo)

valDabie = pd.read_excel('pomiary/dabie.xls')
valDabie = 110 + (valDabie["Sound pressure level (dB)"].mean())
valDabie = '{:.2f}'.format(valDabie)

valParnica = pd.read_excel('pomiary/parnica.xls')
valParnica = 110 + (valParnica["Sound pressure level (dB)"].mean())
valParnica = '{:.2f}'.format(valParnica)

# stworzenie mapy
m = folium.Map(location=[53.428543, 14.552812], tiles='Stamen Terrain', zoom_start=12)

# dodanie markerów
folium.Marker(location=[53.374199,14.475112],popup='Przecław' + "\n" + str(valPrzeclaw) + "dB",icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[53.377681,14.659444],popup='Słoneczne' + "\n" + str(valSloneczne) + "dB",icon=folium.Icon(color='orange')).add_to(m)
folium.Marker(location=[53.442428,14.509582],popup='Pogodno' + "\n" + str(valPogodno) + "dB",icon=folium.Icon(color='orange')).add_to(m)
folium.Marker(location=[53.429901,14.466576],popup='Mierzyn' + "\n" + str(valMierzyn) + "dB",icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[53.408914,14.493657],popup='Gumieńce' + "\n" + str(valGumience) + "dB",icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[53.431190,14.505628],popup='Świerczewo' + "\n" + str(valSwierczewo) + "dB",icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[53.423873,14.533871],popup='Sikorskiego' + "\n" + str(valSikorskiego) + "dB",icon=folium.Icon(color='orange')).add_to(m)
folium.Marker(location=[53.435354,14.554602],popup='Centrum' + "\n" + str(valCentrum) + "dB",icon=folium.Icon(color='red')).add_to(m)
folium.Marker(location=[53.469525,14.594542],popup='Gocław' + "\n" + str(valGoclaw) + "dB",icon=folium.Icon(color='green')).add_to(m)
folium.Marker(location=[53.454716,14.554858],popup='Niebuszewo' + "\n" + str(valNiebuszewo + "dB"),icon=folium.Icon(color='orange')).add_to(m)
folium.Marker(location=[53.397951,14.669019],popup='Dąbie' + "\n" + str(valDabie) + "dB",icon=folium.Icon(color='orange')).add_to(m)
folium.Marker(location=[53.411440,14.579026],popup='Parnica' + "\n" + str(valParnica) + "dB",icon=folium.Icon(color='orange')).add_to(m)

# zapisanie gotowej mapy do pliku .html
m.save('index.html')
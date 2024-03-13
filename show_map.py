import folium


class ShowMap:
    def __init__(self, lat, long):
        lat = lat
        long = long
        
        coords_1 = [[47.75927,27.46054], [47.75779,27.45999], [47.75621,27.45903], [47.7572011, 27.4578334], [47.75666,27.45695], [47.7605340, 27.4525276], [47.7615223, 27.4543951], [47.76372,27.45269], [47.76390,27.45315], [47.76366,27.45369], [47.76356,27.45418], [47.76371,27.45491], [47.76373,27.45523], [47.76361,27.45570], [47.76322,27.45665], [47.76201,27.45822], [47.75960,27.45889], [47.75950,27.45917]]
        self.territories = [
    {"name": "Территория 1", "coords": [[47.774777, 27.493026], [47.782002, 27.496112], [47.779407, 27.506153], [47.767593, 27.497700]]},
    {"name": "Teritoriu 1", "coords": coords_1}
     ]
        self.make_map(lat, long)

    def make_map(self, lat, long):
        # Создание карты
        mymap = folium.Map(location=[lat, long], zoom_start=17)

        # Добавление маркера для текущей геолокации
        folium.Marker([lat, long], tooltip='Текущее положение').add_to(mymap)

        for territory in self.territories:
            folium.Polygon(territory["coords"], color='blue', fill=True, fill_color='blue', fill_opacity=0.2, tooltip=territory["name"]).add_to(mymap)

# Сохранение карты в файл
        mymap.save('templates/map.html')


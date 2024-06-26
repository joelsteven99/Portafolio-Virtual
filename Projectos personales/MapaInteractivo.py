import folium
from folium.plugins import MiniMap, HeatMap, LocateControl, Draw, MeasureControl
mapa = folium.Map(location = (4.7109, -74.0721), zoom_start=12)# Crear un mapa centrado en unas coordenadas específicas
html_Chicago= """
    <h3>Información Enriquecida de Chicago, Illinois, USA</h3>
    <p>Chicago, en el lago Michigan de Illinois, se encuentra entre 
    las ciudades más grandes de los EE.UU. Es famosa por su 
    arquitectura atrevida y tiene un perfil en el que destacan 
    rascacielos como el icónico Centro John Hancock, la torre 
    Willis de 1,451 pies (antigua torre Sears) y Tribune Tower 
    de estilo neogótico. La ciudad también es famosa por sus 
    museos, incluido el Instituto de Arte de Chicago con sus 
    famosas obras impresionistas y posimpresionistas.</p>
    <p><a href="https://es.wikipedia.org/wiki/Chicago" target="_blank">Saber mas</a></p>
    <iframe width="300" height="200" src="https://youtu.be/r1LNTEgHFMw?si=OgPaK1f-esUn_odM" frameborder="0" allowfullscreen></iframe></p>
"""
html_bogota = """
    <h3>Información Enriquecida de Bogotá, Colombia</h3>
    <p>Bogotá es la extensa capital en altura de Colombia. La 
    Candelaria, su centro con adoquines, cuenta con sitios 
    coloniales como el Teatro Colón neoclásico y la Iglesia de 
    San Francisco del siglo XVII. También alberga museos 
    populares, incluido el Museo Botero, que exhibe arte de 
    Fernando Botero, y el Museo del Oro, con piezas de oro 
    precolombinas..</p>
    <iframe width="300" height="200" src="https://youtu.be/r1LNTEgHFMw?si=OgPaK1f-esUn_odM" frameborder="0" allowfullscreen></iframe></p>
    <p><a href="https://es.wikipedia.org/wiki/Bogot%C3%A1" target="_blank">Saber mas</a></p>
"""
#Agregar Marcador deacuerdo con las cordenadas
folium.Marker(
    (41.8781, -87.6298), 
    popup=folium.Popup(html_Chicago, max_width=300),
    icon=folium.Icon(color='blue', icon='user')
    ).add_to(mapa)

folium.Marker(
    (4.7109, -74.0721), 
    popup=folium.Popup(html_bogota, max_width=300),
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(mapa)
# Agregar diferentes capas de mosaico con atribución
folium.TileLayer(
    'openstreetmap',
    name='OpenStreetMap',
    attr='Map data © OpenStreetMap contributors, CC-BY-SA'
).add_to(mapa)
folium.TileLayer(
    'stamentoner',
    name='Stamen Toner',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
).add_to(mapa)
folium.TileLayer(
    'stamenwatercolor',
    name='Stamen Watercolor',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
).add_to(mapa)
folium.TileLayer(
    'cartodbpositron',
    name='CartoDB Positron',
    attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
).add_to(mapa)
folium.TileLayer(
    'stamenterrain',
    name='Stamen Terrain',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
).add_to(mapa)
folium.TileLayer(
    'cartodbdark_matter',
    name='CartoDB Dark Matter',
    attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
).add_to(mapa)
folium.LayerControl().add_to(mapa)# Agregar control de capas
LocateControl().add_to(mapa)# Agregar control de geolocalización
# Agregar un minimapa
minimap = MiniMap()
mapa.add_child(minimap)
# Agregar herramientas de dibujo
draw = Draw()
mapa.add_child(draw)
# Agregar control de medición
measure_control = MeasureControl(
    primary_length_unit='meters',
    secondary_length_unit='miles',
    primary_area_unit='sqmeters',
    secondary_area_unit='acres'
)
mapa.add_child(measure_control)
mapa.save(f'Mapa_Interactivo.html')# Guardar el mapa en un archivo HTML
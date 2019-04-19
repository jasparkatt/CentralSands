import os
import sys
import json
import folium
import pandas as pd
import branca.colormap as cm
import webbrowser
import jenkspy

print("Python version is %s.%s.%s" % sys.version_info[:3])
print("folium version is" + " " + folium.__version__)

WrkDir = r'C:\Users\jon.galloy\PycharmProjects\Py3_Work\My3Projs'
MAPDir = 'Results/'
MAPPath = os.path.join(WrkDir, MAPDir)
foli_map = os.path.join(MAPPath, 'index.html')

tables_src = r'C:\Users\jon.galloy\PycharmProjects\Py3_Work\My3Projs\data\ACS_17_5YR_S0101_DependencyRatios_NoDescription.csv'
geo_src = r'C:\Users\jon.galloy\PycharmProjects\Py3_Work\My3Projs\data\CENTRAL_SANDS_TRACTS.json'
table = pd.read_csv(tables_src)
tracts = json.load(open(geo_src))
#print(tracts)
ratio_dict = table.set_index('GEOID')['HC01_EST_VC40'].sort_values(ascending=True)
# print(ratio_dict.sort_values(ascending=True))
print(len(ratio_dict))
print(len(tracts))
# datasrc = tracts['HC01_EST_VC40'].dropna(how='any').sort_values(ascending=True)
# breaks = jenkspy.jenks_breaks(datasrc, nb_class=8)
# print(breaks)

m = folium.Map(
    #location=[44.465, -89.45],
    tiles='CartoDB positron',
    zoom_start=8.5,
    control_scale=True,
    attr='CSR Productions'
)
m.fit_bounds([[45.120608,-90.318032],[43.641046,-88.605033]])
folium.Choropleth(
    geo_data=tracts,
    data=table,
    name='Where dem old folks at?',
    columns=['GEOID2', 'HC01_EST_VC40'],
    key_on='feature.properties.GEO_Join',
    fill_color='YlOrRd',
    fill_opacity=0.70,
    bins=[9.6, 17.8, 27.5, 34.1, 42.9, 50.2, 65.4, 89.5, 106.8],
    highlight=True,
    legend_name='Old Age Dependency Ratio, 2013-2017',
    show=False
).add_to(m)

folium.LayerControl().add_to(m)
m.save(os.path.join(MAPPath, foli_map))
webbrowser.open(foli_map)


# print(table.head(1))
# print(table.info())
# print(table.describe())
# columns = table.columns#
# print(table.GEOID.values)
# print(table.GEOID.dtype)


import os
import sys
import json
import folium
import pandas as pd
import branca.colormap as cm # for colormap work...not called yet
import webbrowser
import jenkspy

print("Python version is %s.%s.%s" % sys.version_info[:3])
print("folium version is" + " " + folium.__version__)

tables_src = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
geo_src = 'CentralSands-master/CENTRAL_SANDS_TRACTS.json'
table = pd.read_csv(tables_src)
tracts = json.load(open(geo_src))

ratio_dict = table.set_index('FIPS')['Admin2'].sort_values(ascending=True)
print(ratio_dict)

# # use jenkspy to get our class break points
datasrc = table['HC01_EST_VC40'].dropna(how='any').sort_values(ascending=True)
breaks = jenkspy.jenks_breaks(datasrc, nb_class=8)
print(breaks)

# # create our folium map
m = folium.Map(
    tiles='CartoDB positron',
    zoom_start=8.5,
    control_scale=True,
    attr='CSR Productions'
)
# fix the position on opening to Central Wisconsin tracts BB
m.fit_bounds([[45.120608,-90.318032],[43.641046,-88.605033]])
# # create the choropleth by joining our data coloumn to geography
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
# add our control
folium.LayerControl().add_to(m)
# open in notebook
m
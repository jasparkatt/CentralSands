import pandas as pd
import folium
import numpy as np
import json

tables_src = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
table = pd.read_csv(tables_src, index_col=0)
print(table.head(10))
print(table.tail(10))
# get WI data using .loc on the Index col set above which is 'UID'
# write to a dataframe
WI_table = table.loc[84055001: 84055141]
print(table.loc[84055001: 84055141])
print('***************')
print(WI_table.index)
print('***************')
print(WI_table.columns)
print('***************')
print(WI_table.values)
print('***************')
# whittle down some of the columns in the wi table
print(WI_table.loc[84055001: 84055141, 'FIPS':])
WI_data = WI_table.loc[84055001: 84055141, 'FIPS':]

# location is the mean of every lat and long point to centre the map.
location = WI_data['Lat'].mean(), WI_data['Long_'].mean()

# A basemap is then created using the location to centre on and the zoom level to start.
m = folium.Map(location=location, zoom_start=15)

# Each location in the DataFrame is then added as a marker to the basemap points are then added to the map
for i in range(0, len(WI_data)):
    folium.Marker([WI_data['Lat'].iloc[i], WI_data['Long_'].iloc[i]]).add_to(m)

'''
Created on Apr 12, 2016

@author: Max Ruiz
'''

import folium
# https://pypi.python.org/pypi/folium

phx_coords = [33.441957, -112.072913]
map_osm_phx = folium.Map(location=phx_coords)
map_st_phx = folium.Map(location=phx_coords,
                         tiles='Stamen Terrain')

# Used google maps and right clicked "What's here" on "Phoenix"
# to get Downtown coordinates

map_osm_phx.save(outfile='osm_phx.html')
map_st_phx.save(outfile='st_phx.html')

# Unfortunately I cannot get the IPython to work with the maps

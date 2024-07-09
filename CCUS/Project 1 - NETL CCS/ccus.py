import math
import numpy as np
import pandas as pd
import geopandas as gpd
import geodatasets
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px


f = open("output.txt", "w")
f = open("output.txt", "a")

df = pd.read_csv("ccs_jan_23.csv")
df.dropna()
print("CCUS data loaded.")
sorted_data = df.sort_values(by='Project Date')
# sorted_data.dropna(axis='Project Date')
print("Data sorted by project date.\n")
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326"
)

print("Geo Data Frame:")
print(gdf)
world = gpd.read_file(
    "/Users/svperclvster/Documents/webdev/data-analytics/CCUS/Project 1 - NETL CCS/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

# n = len(world)
# i = 0
# print("List of countries in data set")
# abcountries = df.sort_values(by='Country Location')
# print(abcountries['Country Location'])

# countries = abcountries

# while i < n:
#     f.write("\n" + countries['Country Location'][i] + "")
#     i += 1

world = world[~world['ADMIN'].isin(['Antarctica'])]
ax = world.plot(color="#dddddd", edgecolor="black")

usa = gdf[df['Country Location'] == 'United States']
australia = gdf[df['Country Location'] == 'Australia']
brazil = gdf[df['Country Location'] == 'Brazil']
canada = gdf[df['Country Location'] == 'Canada']
china = gdf[df['Country Location'] == 'China']
england = gdf[df['Country Location'] == 'England']
france = gdf[df['Country Location'] == 'France']
germany = gdf[df['Country Location'] == 'Germany']
italy = gdf[df['Country Location'] == 'Italy']
japan = gdf[df['Country Location'] == 'Japan']
mexico = gdf[df['Country Location'] == 'Mexico']
netherlands = gdf[df['Country Location'] == 'Netherlands']
norway = gdf[df['Country Location'] == 'Norway']
poland = gdf[df['Country Location'] == 'Poland']
spain = gdf[df['Country Location'] == 'Spain']
sweden = gdf[df['Country Location'] == 'Sweden']
skorea = gdf[df['Country Location'] == 'South Korea']
safrica = gdf[df['Country Location'] == 'South Africa']
sarabia = gdf[df['Country Location'] == 'Saudi Arabia']
scotland = gdf[df['Country Location'] == 'Scotland']
gdf.plot(ax=ax, color="#11ffff")
usa.plot(ax=ax, color="#0A3161")
australia.plot(ax=ax, color="#012169")
brazil.plot(ax=ax, color="#009739")
canada.plot(ax=ax, color="#D80621")
china.plot(ax=ax, color="#EE1C25")
england.plot(ax=ax, color="#012169")
france.plot(ax=ax, color="#002654")
germany.plot(ax=ax, color="#dd0000")
italy.plot(ax=ax, color="#008C45")
japan.plot(ax=ax, color="#BC002D")
mexico.plot(ax=ax, color="#006341")
netherlands.plot(ax=ax, color="#003DA5")
norway.plot(ax=ax, color="#00205B")
poland.plot(ax=ax, color="#DC143C")
spain.plot(ax=ax, color="#AA151B")
sweden.plot(ax=ax, color="#FECC02")
skorea.plot(ax=ax, color="#0F64CD")
safrica.plot(ax=ax, color="#007749")
sarabia.plot(ax=ax, color="#165d31")
scotland.plot(ax=ax, color="#005EB8")

plt.title('Carbon Capture/Storage projects worldwide as of Jan 2023')
# plt.show()

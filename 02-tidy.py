import pandas as pd
from pandas import read_csv
# do not want to import like this:
# from pandas import *

# this will not work
pew = pandas.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/pew.csv")

# this will work
pew = read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/pew.csv")

# this will work
pew = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/pew.csv")

# pd.melt(pew)
pew.melt(id_vars="religion")

pew.melt(id_vars="religion", var_name="income", value_name="count")

billboard = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/billboard.csv")
billboard

billboard_long = billboard.melt(
  id_vars=["year", "artist", "track", "time", "date.entered"],
  var_name="week",
  value_name="rating"
)

billboard_long

billboard_long.groupby("week")["rating"].mean()


ebola = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/country_timeseries.csv")
ebola

ebola_long = ebola.melt(id_vars=["Date", "Day"])
ebola_long

"Cases_Guinea".split("_")
type("Cases_Guinea".split("_"))
"Cases_Guinea".split("_")[0]
"Cases_Guinea".split("_")[1]


ebola_long["variable"].str.split("_")

ebola_long["variable"].str.split("_", expand=True)

ebola_long[["case_death", "country"]] = ebola_long["variable"].str.split("_", expand=True)
ebola_long

weather = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/weather.csv")
weather

weather_long = weather.melt(id_vars=["id", "year", "month", "element"], var_name="day", value_name="temp")
weather_long

weather_tidy = weather_long.pivot_table(index=["id", "year", "month", "day"], columns="element", values="temp")
weather_tidy

weather_tidy.reset_index()

weather_tidy = (
  weather
  .melt(id_vars=["id", "year", "month", "element"], var_name="day", value_name="temp")
  .pivot_table(index=["id", "year", "month", "day"], columns="element", values="temp")
  .reset_index()
)

weather_tidy.columns
weather_long.columns
weather_tidy.columns.name = None

weather_tidy.index

weather_tidy


# normalization

billboard = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/billboard.csv")
billboard

billboard_long = billboard.melt(
  id_vars=["year", "artist", "track", "time", "date.entered"],
  var_name="week",
  value_name="rating"
)

billboard_long["track"] == "Loser"

billboard_long.loc[billboard_long["track"] == "Loser"]

billboard_song = billboard_long[["year", "artist", "track", "time"]]
billboard_song

billboard_song.shape

billboard_song = billboard_song.drop_duplicates()
billboard_song

billboard_song.index

billboard_song = billboard_song.reset_index()
billboard_song.index

billboard_song["id"] = billboard_song.index
billboard_song= billboard_song.drop(columns=["index"])
billboard_song

billboard_long

billboard_ratings = billboard_long.merge(billboard_song, on=["year", "artist", "track", "time"])
billboard_ratings = billboard_ratings[["id", "date.entered", "week", "rating"]]

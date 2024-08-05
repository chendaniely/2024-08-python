import pandas

pandas.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/gapminder.tsv", sep="\t")

import pandas as pd

pd.__version__

pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/gapminder.tsv", sep="\t")

df = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/gapminder.tsv", sep="\t")

type(df)

df.head()
df.tail()

df.shape

df.shape()

df.columns

type(df.columns)

df.index

type(df.index)

df.values

df.dtypes

df.info()

df["country"]

type(df["country"])

country_df = df["country"]
country_df

df[["country"]]

subset = df[["country", "continent", "year"]]
subset

df.loc[0]

df.loc[[0]]

df.sample(5).loc[0]

df.loc[-1]

df.iloc[[0]]

df.sample(5).iloc[0]

df.iloc[[-1]]


df.loc[[0, 1, 2], ["year", "pop"]]
df.iloc[[0, 1, 2], [2, 4]]

# <- # does not exist in python
df.groupby("year")["lifeExp"].mean()

grouped = df.groupby(["year", "continent"])[["lifeExp", "gdpPercap"]].mean()
grouped

type(grouped)

grouped.columns
grouped.values
grouped.index

grouped["year"]

grouped.reset_index()

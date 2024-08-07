def my_function():
  pass

def my_sq(x):
  return x ** 2

my_sq(4)

assert my_sq(4) == 16
assert my_sq(4) == 8

# type hint
def my_sq(x: int | float) -> int | float:
  return x ** 2

my_sq(4)
my_sq(16.5)


import pandas as pd

df = pd.DataFrame({
    "a": [10, 20, 30],
    "b": [20, 30, 40]
})

df

df["a"]

df.a

df.shape

df["a"] ** 2

type(df["a"])

df["a"].apply(my_sq)

def my_exp(x, e):
  return x ** e

assert my_exp(2, 2) == 4

df["a"].apply(my_exp, e=10)

def my_exp(e, x):
  return x ** e

df["a"].apply(my_exp, x=10)

# reset function arguments to original
def my_exp(x, e):
  return x ** e

# function(x) my_exp(2, x)
df["a"].apply(lambda value: my_exp(2, value))


def print_me(x):
  print(x)


print_me("hello")
x = print_me("hello")
x

df

df.apply(print_me)


df.apply(print_me, axis='index')

# avoid this, which is the same as axis=1
df.apply(print_me, axis='columns')


def avg_3(x, y, z):
  return (x + y + z) / 3


assert avg_3(0, 5, 10) == 5

df.apply(avg_3)

def avg_3_apply(col):
  x = col[0]
  y = col[1]
  z = col[2]
  return (x + y + z) / 3

df.apply(avg_3_apply)

import numpy as np

def avg_3_np(col):
  return np.mean(col)
  
df.apply(avg_3_np)

df.apply(avg_3_apply, axis='columns')
df

(df['a'] + df['b']) / 2

def avg_2(x, y):
  return (x + y) / 2

avg_2(df.a, df.b)

def avg_2_mod(x, y):
  if (x == 20):
    return np.nan
  else:
    return (x + y) / 2
  
avg_2_mod(df['a'], df['b'])

avg_2_mod(10, 20)
avg_2_mod(20, 30)

import numpy as np

avg_2_mod_vec = np.vectorize(avg_2_mod)

avg_2_mod_vec(20, 30)
avg_2_mod_vec(10, 30)

avg_2_mod_vec(df['a'], df['b'])

@np.vectorize
def v_avg_2_mod(x, y):
  if (x == 20):
    return np.nan
  else:
    return (x + y) / 2
  
v_avg_2_mod(10, 20)
v_avg_2_mod(20, 30)
v_avg_2_mod(df['a'], df['b'])

import numba

@numba.vectorize
def v_avg_2_mod_numba(x, y):
  if (x == 20):
    return np.nan
  else:
    return (x + y) / 2

v_avg_2_mod_numba(10, 20)
v_avg_2_mod_numba(20, 20)

v_avg_2_mod_numba(df['a'], df['b'])
v_avg_2_mod_numba(df['a'].values, df['b'].values)


t3 = pd.read_csv("https://raw.githubusercontent.com/chendaniely/2024-08-python/main/data/table3.csv")
t3

"745/19987071".split("/")[1]

# write a function that takes a rate value, and returns a population
# vectorize that function
# set the population to new column

# there is a tool called mypy that can check this during unit testing
def get_pop(rate: str) -> int:
  return int(rate.split("/")[1])

get_pop("745/19987071")


get_pop(t3["rate"])

@np.vectorize
def get_pop(rate: str) -> int:
  return int(rate.split("/")[1])

t3["population"] = get_pop(t3["rate"])
t3

t3.info()

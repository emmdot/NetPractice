import quandl
import pandas as pd

df = quandl.get('WIKI/GOOGL', returns = ':numpy')

print type(df)


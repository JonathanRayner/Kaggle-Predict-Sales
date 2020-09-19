import pandas as pd
import numpy as np

# summary of cleaning:
#
# small number of duplicates, remove these
# remove the single item with negative price
# remove the single large outlier item price (corporate software purchase)

df = pd.read_csv("sales_train.csv")

df.drop_duplicates(inplace=True)

df = df[(df['item_price'] > 0) & (df['item_price'] < 6e4)]

# save
df.to_csv('train_clean.csv', index=False)

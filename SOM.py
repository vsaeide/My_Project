from sklearn_som.som import SOM
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel(r'sample/sell.xlsx', engine='openpyxl')

df= df[['BUY_PRICE', 'PRODUCT_ID']]
df= df.to_numpy()


# Build a 3x1 SOM (3 clusters)
som = SOM(2,1, dim=2)

# Fit it to the data
som.fit(df)

# Assign each datapoint to its predicted cluster
predictions = som.predict(df)

print(predictions)

plt.scatter(df['BUY_PRICE'], df['PRODUCT_ID'], c=predictions.astype(float), s=50, alpha=0.5
            )
plt.show()

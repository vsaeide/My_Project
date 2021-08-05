# import data

import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel(r'sample/sell.xlsx', engine='openpyxl')

df= df[['BUY_PRICE', 'CATEGORY_ID', 'PRODUCT_ID']]
# learning knn


samples = df
# my samples
# samples = [[32000, 1, 2, 1, 2000], [3000, 2, 1, 1, 1200], [5000, 4, 1, 1, 3400],
#            [2000, 1, 1, 2, 1000], [5000, 2, 1, 2, 24000], [6000, 4, 1, 1, 3000],
#            [4000, 1, 2, 2, 1300], [65000, 2, 1, 1, 4200], [6000, 1, 1, 2, 4000],
#            [24000, 1, 1, 2, 1000], [6000, 2, 1, 1, 42300], [2000, 1, 1, 2, 5000],
#            ]
from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(n_neighbors=2)
neigh.fit(samples)

# NearestNeighbors(n_neighbors=2)

# my sample to test
result = neigh.kneighbors([[2000, 1, 8]])

print(result, "\n\n\n")

# print n nearest node to input
for i in range(2):
    print(df.iloc[[result[1][0][i]]])
    #print(samples[result[1][0][i]])



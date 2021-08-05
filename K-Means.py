import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

pd.set_option('display.max_columns', None)

df = pd.read_excel(r'sample/sell.xlsx', engine='openpyxl')

df= df[['BUY_PRICE', 'CATEGORY_ID', 'PRODUCT_ID']]


kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_

print(centroids)

# just plot by price and produnct id
print(df)
plt.scatter(df['BUY_PRICE'], df['PRODUCT_ID'], c=kmeans.labels_.astype(float), s=50, alpha=0.5
            )
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
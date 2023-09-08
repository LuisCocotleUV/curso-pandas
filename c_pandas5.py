### 1 ###
dtype = reviews.points.dtype

q1.check()
dtype


### 2 ####
point_strings = reviews.points.astype('str')

q2.check()
point_strings


### 3 ###
n_missing_prices = reviews.price.isnull().sum()

q3.check()
n_missing_prices


### 4 ###
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

q4.check()
reviews_per_region
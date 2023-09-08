### 1 ###
median_points = reviews.points.median()

q1.check()
median_points


### 2 ####
countries = reviews.country.unique()

q2.check()
countries


### 3 ###
reviews_per_country = reviews.country.value_counts()

q3.check()
reviews_per_country


### 4 ###
centered_price = reviews.price - reviews.price.mean()

q4.check()
centered_price


### 5 ###
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

q5.check()
bargain_wine


### 6 ###
tro = reviews.description.map(lambda desc:"tropical"in desc).sum()
fru = reviews.description.map(lambda desc : "fruity"in desc).sum()
descriptor_counts = pd.Series([tro,fru], index = ["tropical", "fruity"])

q6.check()
descriptor_counts


### 7 ###
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')

q7.check()
star_ratings
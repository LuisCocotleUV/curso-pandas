### 1 ###
desc = reviews ['description']

q1.check()


### 2 ####
first_description = reviews.description.iloc[0]

q2.check()
first_description


### 3 ###
first_row = reviews.iloc[0]

q3.check()
first_row


### 4 ###
first_descriptions = reviews.description.head(10)

q4.check()
first_descriptions


### 5 ###
a = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[a]

q5.check()
sample_reviews


### 6 ###
a = [0, 1, 10, 100]
b=['country','province','region_1','region_2']
df = reviews.loc[a,b]

q6.check()
df


### 7 ###
a = ['country','variety']
df = reviews.loc[:99, a]

q7.check()
df


### 8 ###
italian_wines = reviews.loc[reviews.country=='Italy']

q8.check()


### 9 ###
top_oceania_wines = reviews.loc [(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points>=95)]

q9.check()
top_oceania_wines
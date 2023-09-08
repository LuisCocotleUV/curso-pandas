### 1 ###
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

q1.check()
reviews_written


### 2 ####
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

q2.check()
best_rating_per_price


### 3 ###
price_extremes = reviews.groupby('variety').price.agg([min,max])

q3.check()
price_extremes


### 4 ###
sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min', 'max'], ascending=False)

q4.check()
sorted_varieties


### 5 ###
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

q5.check()
reviewer_mean_ratings


### 6 ###
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)

q6.check()
country_variety_counts
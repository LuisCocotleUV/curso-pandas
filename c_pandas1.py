### 1 ###
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

q1.check()
fruits


### 2 ####
fruit_sales = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]}, index = ['2017 Sales','2018 Sales'])

q2.check()
fruit_sales


### 3 ###
ingredients = pd.Series (['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'], name='Dinner')

q3.check()
ingredients


### 4 ###
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

q4.check()
reviews


### 5 ###
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals


animals.to_csv('cows_and_goats.csv')

q5.check()
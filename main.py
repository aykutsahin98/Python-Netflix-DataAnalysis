import pandas as pd
import numpy as np
import seaborn as sns
sns.set(color_codes = True)  #sets nice background color
import matplotlib.pyplot as pl
netflix =pd.read_csv('NetflixOriginals.csv', encoding="latin-1")

#Viewing first few rows of the dataset
print(netflix.head())
#We have 6 column entries and 584 rows
print(netflix.shape)
#To understand more about the datatypes
print(netflix.info())

print(netflix.describe())
# 5-point summaey
#Average movie run time is 94 mins and average IMDB score is 6

# To find if there are any null values
print(pd.DataFrame( netflix.isnull().sum(), columns= ['Number of missing values']))
print()
netflix["Date"] = pd.to_datetime(netflix.Premiere)
print (netflix["Date"])

print("---------------------------------------------------------------------------------")

netflix['Year'] = netflix['Date'].dt.year
netflix['Month'] = netflix['Date'].dt.month
netflix['Day'] = netflix['Date'].dt.day_of_week
print(netflix.head())

print("---------------------------------------------------------------------------------")

#Hangi yılda en fazla film yayımlanmıştır?
year = netflix.Year.value_counts()
print(year)

print("---------------------------------------------------------------------------------")

#En çok 2020 yılında yayınlanmıştır. Görselleştirilmiş hali
sns.barplot(x=year.index, y=year.values, palette="OrRd")
pl.show()

print("---------------------------------------------------------------------------------")

#Veri setinde kullanılan en popüler 3 dil
top_3_lang = netflix.Language.value_counts().nlargest(3)
print(top_3_lang)

print("---------------------------------------------------------------------------------")

#IMDB Puanı en yüksek olan ilk 10 film
top_10_movies = netflix[["IMDB Score", "Title",]].sort_values(["IMDB Score"], ascending=False)[:10]
print(top_10_movies)

print("---------------------------------------------------------------------------------")

#IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
print(netflix.groupby("Genre")["IMDB Score"].mean().nlargest(10))

print("---------------------------------------------------------------------------------")

#IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
sns.regplot(data=netflix,x='IMDB Score',y='Runtime');
pl.title('Scatter plot of runtime and IMDB score');
pl.show()

print("---------------------------------------------------------------------------------")

#'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
top_10_runtime = netflix[["Title", "Runtime"]].sort_values(["Runtime"], ascending=False)[:10]
print(top_10_runtime)

#Görsel Hali
sns.catplot(data = top_10_runtime, x='Runtime', y='Title')
pl.show()

print("---------------------------------------------------------------------------------")

#Genre kategorisi kaç tane
print(netflix['Genre'].nunique())

print("---------------------------------------------------------------------------------")

#Genre Kategorileri Nelerdir
print(netflix['Genre'].unique())

print("---------------------------------------------------------------------------------")

#IMDB Puanı en düşük olan 10 film ve dili
imdblanguage=(netflix.groupby("Language")["IMDB Score"].mean().nsmallest(10))
print(imdblanguage)

#IMDB Puanı en düşük olan 10 film ve dili. Görselleştirilmiş hali
imdblanguageplot = sns.barplot(x=imdblanguage.values, y=imdblanguage.index, orient='h')
imdblanguageplot.set(ylabel="Language", xlabel="IMDB scores")

print("---------------------------------------------------------------------------------")

#IMDB Puanı en düşük olan 10 film ve dili. Görselleştirilmiş hali
imdblanguageplot = sns.barplot(x=imdblanguage.values, y=imdblanguage.index, orient='h')
imdblanguageplot.set(ylabel="Language",xlabel="IMDB scores")
pl.show()

print("---------------------------------------------------------------------------------")





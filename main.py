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

print("Veri Setine Göre Uzun Soluklu Filmler Hangi Dilde Oluşturulmuştur? Görselleştirme Yapınız.")
print("Uzun Soluklu Film 90 Ve Üstü Seçildi\n")

find_long = netflix.where(netflix['Runtime'] >= 90)
find_long = find_long[["Language", "Title", "Runtime"]].dropna()
print(find_long)

#Görselleştirilmiş Hali
language_high_plot = sns.barplot(data = find_long, x='Runtime', y='Language')
pl.show()

print("---------------------------------------------------------------------------------")

print("2019 Ocak İle 2020 Haziran Tarihleri Arasında 'Documentary' Türünde Çekilmiş Filmlerin IMDB Değerlerini Bulup Görselleştiriniz.\n")
find_Documentary = netflix.where(netflix['Genre'] == 'Documentary')
find_Documentary_imdb = find_Documentary[["Year", "IMDB Score", "Title", "Genre"]]
find_Documentary_imdb_2019 = find_Documentary_imdb.where(netflix['Year'] == 2019)
find_Documentary_imdb_2020 = find_Documentary_imdb.where(netflix['Year'] == 2020)

find_Documentary_imdb_year = pd.concat([find_Documentary_imdb_2019, find_Documentary_imdb_2020])
find_Documentary_imdb_year = find_Documentary_imdb_year.dropna()
print(find_Documentary_imdb_year)

#Görselleştirilmiş Hali
find_Documentary_imdb_year_plot = sns.barplot(data = find_Documentary_imdb_year, x='Year', y='IMDB Score')
pl.show()

print("---------------------------------------------------------------------------------")

print("İngilizce Çekilen Filmler İçerisinde Hangi Tür En Yüksek IMDB Puanına Sahiptir?\n")
find_english_imdb = netflix.where(netflix['Language'] == 'English')
find_english_imdb = find_english_imdb[["Language", "Genre", "IMDB Score"]].dropna()
maks = find_english_imdb.max()
print(maks)

print("---------------------------------------------------------------------------------")

print("'Hindi' Dilinde Çekilmiş Olan Filmlerin Ortalama 'Runtime' Süresi Nedir?\n")
find_Hindi = netflix.where(netflix['Language'] == 'Hindi')
find_Hindi = find_Hindi[["Year", "Language", "Title", "Runtime"]].dropna()
average = find_Hindi[["Runtime"]].mean()
print(find_Hindi)

print("---------------------------------------------------------------------------------")

print("Genre Kategorisi Kaç Tanedir?")
print(netflix['Genre'].nunique())

print("Genre Kategorileri Nelerdir?\n")
print(netflix['Genre'].unique())

print("---------------------------------------------------------------------------------")

print("Veri Setinde Kullanılan En Popüler 3 Dil\n")
top_3_lang = netflix.Language.value_counts().nlargest(3)
print(top_3_lang)

print("---------------------------------------------------------------------------------")

print("IMDB Puanı En Yüksek Olan İlk 10 Film\n")
top_10_movies = netflix[["IMDB Score", "Title",]].sort_values(["IMDB Score"], ascending=False)[:10]
print(top_10_movies)

print("---------------------------------------------------------------------------------")

print("IMDB Puanı İle 'Runtime' Arasında Nasıl Bir Korelasyon Vardır? İnceleyip Görselleştiriniz\n")
sns.regplot(data=netflix,x='IMDB Score',y='Runtime');
pl.title('Scatter plot of runtime and IMDB score');
pl.show()

print("---------------------------------------------------------------------------------")

print("IMDB Puanı En Yüksek Olan İlk 10 'Genre' Hangileridir?\n")
print(netflix.groupby("Genre")["IMDB Score"].mean().nlargest(10))

print("---------------------------------------------------------------------------------")

print("'Runtime' Değeri En Yüksek Olan İlk 10 Film Hangileridir?\n")
top_10_runtime = netflix[["Title", "Runtime"]].sort_values(["Runtime"], ascending=False)[:10]
print(top_10_runtime)

#Görsel Hali
sns.catplot(data = top_10_runtime, x='Runtime', y='Title')
pl.show()

print("---------------------------------------------------------------------------------")

print("Hangi Yılda En Fazla Film Fayımlanmıştır?\n")
year = netflix.Year.value_counts()
print(year)

#Görselleştirilmiş hali
sns.barplot(x=year.index, y=year.values, palette="OrRd")
pl.show()

print("---------------------------------------------------------------------------------")

print("IMDB Puanı En Düşük Olan 10 Film Ve Dili\n")
imdblanguage=(netflix.groupby("Language")["IMDB Score"].mean().nsmallest(10))
print(imdblanguage)

#Görselleştirilmiş hali
imdblanguageplot = sns.barplot(x=imdblanguage.values, y=imdblanguage.index, orient='h')
imdblanguageplot.set(ylabel="Language", xlabel="IMDB scores")
pl.show()

print("---------------------------------------------------------------------------------")

print("Hangi Yılın Toplam 'Runtime' Süresi En Fazladır?\n")
find_year_runtime = netflix[["Year","Title", "Runtime"]]
find_year_runtime_year_s = find_year_runtime.drop(find_year_runtime.index[0:])

for x in range(2014,2022):

    find_year_runtime_year = find_year_runtime.where(netflix['Year'] == x)
    find_year_runtime_year = find_year_runtime_year[["Year","Title", "Runtime"]].sort_values(["Runtime"], ascending=False)[:1]
    find_year_runtime_year_s = pd.concat([find_year_runtime_year_s, find_year_runtime_year])
print(find_year_runtime_year_s)





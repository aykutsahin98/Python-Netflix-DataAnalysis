import pandas as pd
import seaborn as sns
import numpy as np
#sns.set(color_codes = True)  #sets nice background color
import matplotlib.pyplot as pl
import plotly.express as px
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
pl.figure(figsize=(12,12))
language_high_plot = sns.barplot(data = find_long, x='Runtime', y='Language')
pl.title("Dillere Göre Süreler")
pl.xticks(rotation = 90)
pl.show()

print("---------------------------------------------------------------------------------")

print("2019 Ocak İle 2020 Haziran Tarihleri Arasında 'Documentary' Türünde Çekilmiş Filmlerin IMDB Değerlerini Bulup Görselleştiriniz.\n")
netflix["Date"] = pd.to_datetime(netflix.Premiere)

DateSort = netflix.loc[(netflix["Genre"] == "Documentary") & (netflix["Date"] > "2019-01-31") & (netflix["Date"] < "2020-06-01")]
DateSortFig = px.bar(DateSort, x=DateSort.Title, y = DateSort["IMDB Score"])
DateSortFig.show()

print("---------------------------------------------------------------------------------")

print("İngilizce Çekilen Filmler İçerisinde Hangi Tür En Yüksek IMDB Puanına Sahiptir?\n")
find_english_imdb = netflix.where(netflix['Language'] == 'English')
find_english_imdb = find_english_imdb[["Language", "Genre", "IMDB Score"]].dropna()
maks = find_english_imdb.max()
print(maks)

print("---------------------------------------------------------------------------------")

print("'Hindi' Dilinde Çekilmiş Olan Filmlerin Ortalama 'Runtime' Süresi Nedir?\n")
Hindi = netflix.loc[(netflix["Language"] == "Hindi")]
b = Hindi.Runtime
print(b.mean())

print("---------------------------------------------------------------------------------")

print("Genre Kategorisi Kaç Tanedir?")
print(netflix['Genre'].nunique())

print("Genre Kategorileri Nelerdir?\n")
print(netflix['Genre'].unique())

print()
genre = netflix.Genre.value_counts().nlargest(20)
print(genre)

fig = px.bar(data_frame=genre, x=genre.index, y=genre.values, labels={"y":"Genre Movies", "index":"Genres"})
fig.show()

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

print(netflix["Runtime"].corr(netflix["IMDB Score"]))

#Grafikte de görüldüğü üzere belirli bir dağılım gözükmemekte.
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

print("---------------------------------------------------------------------------------")

print("Her Bir Dilin En Fazla Kullanıldığı 'Genre' Nedir?")
print(netflix.groupby("Language")["Genre"].value_counts().groupby(level=0).head(1))

print("---------------------------------------------------------------------------------")

print("Veri Setinde Outlier Veri Varmı? Açıklayınız")

print(netflix['IMDB Score'].head(3))
print()
print(netflix['IMDB Score'].describe().T)

print("Burada verilen maksimum puanın 9,0 ve minimum puanın 2,5 olduğunu ve ortalama puanın 6,27 olduğunu ve tüm puanların\n "
      "medyanının 6,35 olduğunu görebiliriz, çünkü medyan ortalama puandan daha büyük olduğundan verilerimiz aykırı olabilir.\n "
      "Bunun için bir histogram çizerek görselleştirelim.\n")

sns.histplot(x=netflix['IMDB Score'],color='blue',data=netflix)
pl.show()

import warnings
warnings.filterwarnings('ignore')
sns.boxplot(netflix['IMDB Score'])

print("---------------------------------------------------------------------------------")

print("Veri Setinde Outlier Veri Varmı? Açıklayınız")

runtime_nr=len(netflix.Runtime)
print("Toplam film sayısı:",runtime_nr)
print("------")
print("Boxplot chart of Runtime:")
sns.boxplot(x=netflix.Runtime);

# Runtime verisi üzerinde Outlier Analizi

outliers=[]
threshold=3
meanflix=np.mean(netflix.Runtime)
stdflix=np.std(netflix.Runtime)
print("Ortalama süre",meanflix, "dakikadır.")
print("---------------------------------------------------------------------")

q1=np.quantile(netflix.Runtime, 0.25)
q2=np.quantile(netflix.Runtime, 0.5)
q3=np.quantile(netflix.Runtime, 0.75)
iqr=q3-q1

print("Q1=",q1)
print("Q2=",q2)
print("Q3=",q3)
print("IQR=",iqr)
print("---------------------------------------------------------------------")

for y in netflix.Runtime:
  z_score = (y- meanflix)/stdflix
  if np.abs(z_score) > threshold:
    outliers.append(y)
#return outliers
print("Outlier veri olarak görülebilecek film süreleri:", outliers)
print("Bu değerler değerlendirmeye alınamayacak kadar küçük ve büyük değerlerdir.")


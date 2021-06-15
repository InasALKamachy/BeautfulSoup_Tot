import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")

soup = BeautifulSoup(webpage.content, "html.parser")

all_ratings_tags = soup.find_all(attrs={"class": "Rating"})
ratings=[]
for tag in all_ratings_tags[1:]:
  ratings.append(float(tag.get_text()))
  
plt.hist(ratings)

company_tags = soup.select(".Company")
companies = []

for company in company_tags[1:]:
  companies.append(company.get_text())

cocoa_percentages = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for td in cocoa_percent_tags[1:]:
    percent = float(td.get_text().strip('%'))
    cocoa_percentages.append(percent)
  
df_thingy = {"Company": companies, "Rating": ratings, "Cocoa Percent": cocoa_percentages}
dataframe = pd.DataFrame.from_dict(df_thingy)


mean_vals = dataframe.groupby("Company").mean()
average_rating = dataframe.groupby("Company").Rating.mean()

ten_best = mean_vals.nlargest(10, "Rating")
print(ten_best)

plt.clf()
plt.scatter(dataframe["Cocoa Percent"], dataframe.Rating)

plt.show()

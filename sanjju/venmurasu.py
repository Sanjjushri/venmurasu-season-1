from bs4 import BeautifulSoup
import requests
from requests.api import head
import csv

source1 = requests.get("https://venmurasu.in/mutharkanal/chapter-1").text
soup1 = BeautifulSoup(source1, 'lxml')

source2 = requests.get("https://venmurasu.in/mutharkanal/chapter-2").text
soup2 = BeautifulSoup(source2, 'lxml')

source3= requests.get("https://venmurasu.in/mutharkanal/chapter-3/").text
soup3 = BeautifulSoup(source3, 'lxml')

source4 = requests.get("https://venmurasu.in/mutharkanal/chapter-4/").text
soup4 = BeautifulSoup(source4, 'lxml')

source5 = requests.get("https://venmurasu.in/mutharkanal/chapter-5").text
soup5 = BeautifulSoup(source5, 'lxml')

csv_file = open('../datasets/முதற்கனல்.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['column1'])


for data1 in soup1.find_all("p"):
    chap_1 = data1.get_text()
    print(chap_1)
    csv_writer.writerow([chap_1])

for data2 in soup2.find_all("p"):
    chap_2 = data2.get_text()
    print(chap_2)
    csv_writer.writerow([chap_2])

for data3 in soup3.find_all("p"):
    chap_3 = data3.get_text()
    print(chap_3)
    csv_writer.writerow([chap_3])

for data4 in soup4.find_all("p"):
    chap_4 = data4.get_text()
    print(chap_4)
    csv_writer.writerow([chap_4])
    
for data5 in soup5.find_all("p"):
    chap_5 = data5.get_text()
    print(chap_5)

    csv_writer.writerow([chap_5])

csv_file.close

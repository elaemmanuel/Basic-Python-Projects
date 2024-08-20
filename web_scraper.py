import requests
from bs4 import BeautifulSoup


url ="https://pypi.org/project/opencv-python/"
r = requests.get(url) 
r

soup = BeautifulSoup(r.content, 'lxml')

#Use the tag and class in the find method for the detail you are trying to get 
requested_doc = soup.find("h6", {"class":"sidebar-section__title"})
requested_doc.getText()






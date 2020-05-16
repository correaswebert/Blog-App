from bs4 import BeautifulSoup #Library Used for scraping
import requests
import time #To stop for a second after scraping one post, done to avoid breaking the website
import re #To get '\n' and '\t'
title_list = [] #List of all titles
content_list = [] #List of all content

def pretitle(title):
    title = re.sub("\\n","",title)
    title = re.sub("\\t","",title)
    return title


def gencontent(htmlstr):  #Parses through a post and gets the content of the post
    source = requests.get(htmlstr).text
    content_soup = BeautifulSoup(source,'lxml') #bs4 object of the post
    content = ""
    for i in content_soup.find_all('p'):
        if(i.text=='Read the rules you agree to by using this website in our Terms of Service.'): #Most posts terminate with this sentence, so this is where we stop scraping
            break
        content+=i.text #Content of the post
    return content


for i in range(1,6): #Iterating through 5 pages of posts
    source = requests.get('https://boingboing.net/grid/page/'+str(i)).text
    soup = BeautifulSoup(source,'lxml') #bs4 object of page with posts
    title_soup = soup.find_all('a',class_='headline') #iterable of post titles
    
    for title in title_soup:
        title_list.append(pretitle(title.text)) #Appending title of the post
        content_list.append(gencontent(title['href'])) #Appending content of the post
        time.sleep(1.0) #Sleeps for 1 second
    print(title_list)





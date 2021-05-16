#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import requests 
from bs4 import BeautifulSoup

mainurl='https://iiitd.ac.in/'

kk = requests.get('https://iiitd.ac.in/people/faculty').text 
#print(kk)
soup=BeautifulSoup(kk, 'html.parser') #or you could pass lxml too , extracting text and html tags
iiitd=[]

#finding all faculty using div 
#faclist= soup.find_all("div", {"class":"card rteleft facultycard"}, {"style":"width:245px"} , {"dept":"5"}, {"type":"regular"})
faclist= soup.find_all("div", {"class":"card rteleft facultycard"}, {"type":"regular"})
#print(faclist)
names=[]
positions=[]
unis=[]


#finding names of professor and appending to list 
for i in faclist:
    
   
    for a in i.find_all('a'):
        
        n=a.text
        names.append(n)
        

#finding positions of professors and appending to list 
for j in faclist:
    for k in j.find_all('p'):
        
        for kk in k.find_all('strong'):
            kkk=kk.text
            #if "iiitd" not in kkk:
            if 'Associate' in kkk or 'Assistant' in kkk :
                pos=k.text 
                positions.append(pos)
 
#finding university and appending to list 
for j in faclist: 
    for k in j.find_all('p'):
        kk= k.text
        if 'PhD' in kk :
            #u=kk.text
            unis.append(kk)
            
            
#print(names) 
#print(len(names))
print(" ")
#print(positions)
#print(len(positions))
print(" ")
#print(unis)
#print(len(unis))


a= {'Name': names,'Position': positions,'Education': unis}
df1 = pd.DataFrame.from_dict(a, orient='index')
df1=df1.transpose()
df1.to_csv('IIITD_Faculty.csv')
print(df1)
#df1 = pd.DataFrame({'Name': names,'Position': positions,'Education': unis})
#df1 = pd.DataFrame({'Name':names,'Position':positions})
#df1= pd.DataFrame({"Name": names, "Position":positions, "Education":unis})
#df1=pd.DataFrame({"Position": positions})


#n=i.find('a').contents[0]
#print(div.find('a').contents[0])
#n=i.find('a')['href']
#print(i.find('a')['href'])
#n=i.find("a").get("href")
#n= i.findNext('a').text
#n=i.find('a').text
#names.append(n)
    
   
    

    


    
    
    



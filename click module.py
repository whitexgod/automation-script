#!/usr/bin/env python
# coding: utf-8

# In[1]:
from twilio.rest import Client
import smtplib
from datetime import date
import mechanize
import bs4
import requests
import random
import re


# In[2]:


today=date.today()
print(today)


# In[ ]:


email='********@gmail.com'
password='***********'

account_sid = '********************************'
auth_token = '*********************************'
client = Client(account_sid, auth_token)

# In[4]:


#Login_module

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

sign_in = br.open("http://classroom.campusx.in/")  #the login url

br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
#br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

br["email"] = "*********************@gmail.com" #the key "username" is the variable that takes the username/email value

br["password"] = "******"    #the key "password" is the variable that takes the password value

logged_in = br.submit()   #submitting the login credentials

src = logged_in.read()  #reading the page body that is redirected after successful login


# In[10]:


soup = bs4.BeautifulSoup(src, 'html.parser')
#print(soup.prettify())


# In[ ]:





# In[8]:


#hiting gyan links for Ritayan 


src=br.open("http://classroom.campusx.in/gyan")
soup = bs4.BeautifulSoup(src, 'html.parser')

url=[]

for cell in soup.find_all("div", class_="card-body"): 
    name = ""
    a_tag=''
    
    namecell = cell.find("h6", class_="card-title", text='Ritayan Dhara')
    if namecell is not None:
        name = namecell.get_text(strip=True)
        a_tag = cell.find('a')
        url.append(str(a_tag.attrs['href']))
            
    
url_to_hit1=url[0]
url_to_hit2=url[1]
url_to_hit3=url[2]
url_to_hit4=url[3]
url_to_hit5=url[4]
link_generated1=('http://classroom.campusx.in'+url_to_hit1)
link_generated2=('http://classroom.campusx.in'+url_to_hit2)
link_generated3=('http://classroom.campusx.in'+url_to_hit3)
link_generated4=('http://classroom.campusx.in'+url_to_hit4)
link_generated5=('http://classroom.campusx.in'+url_to_hit5)
br.open(link_generated1)
br.open(link_generated2)
br.open(link_generated3)
br.open(link_generated4)
br.open(link_generated5)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email,password)

    subject='Ritayan post click'
    body='Doneeeeeeee'

    msg=f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email,'******************@gmail.com',msg)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Ritayan gyan link has been clicked',
    to='whatsapp:+91700399****'
)


# In[ ]:





# In[13]:


#hiting gyan links for Wasif


src=br.open("http://classroom.campusx.in/gyan")
soup = bs4.BeautifulSoup(src, 'html.parser')

url=[]

for cell in soup.find_all("div", class_="card-body"): 
    name = ""
    a_tag=''
    
    namecell = cell.find("h6", class_="card-title", text='Wasif Ekbal')
    if namecell is not None:
        name = namecell.get_text(strip=True)
        a_tag = cell.find('a')
        url.append(str(a_tag.attrs['href']))
            
    
url_to_hit1=url[0]
url_to_hit2=url[1]
url_to_hit3=url[2]
url_to_hit4=url[3]
url_to_hit5=url[4]
link_generated1=('http://classroom.campusx.in'+url_to_hit1)
link_generated2=('http://classroom.campusx.in'+url_to_hit2)
link_generated3=('http://classroom.campusx.in'+url_to_hit3)
link_generated4=('http://classroom.campusx.in'+url_to_hit4)
link_generated5=('http://classroom.campusx.in'+url_to_hit5)
br.open(link_generated1)
br.open(link_generated2)
br.open(link_generated3)
br.open(link_generated4)
br.open(link_generated5)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email,password)

    subject='wasif post click'
    body='Doneeeeeeeeee'

    msg=f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email,'******************@gmail.com',msg)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='wasif gyan link has been clicked',
    to='whatsapp:+91700399****'
)
# In[ ]:





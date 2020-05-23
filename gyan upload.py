#!/usr/bin/env python
# coding: utf-8

# In[1]:

import smtplib
from datetime import date
import mechanize
import bs4
import requests
import random
from twilio.rest import Client
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


# In[7]:


#extracting gyaan link

src = requests.get("https://indianexpress.com/section/technology/tech-news-technology/")
soup = bs4.BeautifulSoup(src.content , 'html.parser')

urls=[]
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(str(a_tag.attrs['href']))
    
random_choice1=(random.choice(urls))
random_choice2=(random.choice(urls))
random_choice3=(random.choice(urls))


# In[ ]:





# In[9]:


#Login_module

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

sign_in = br.open("http://classroom.campusx.in/")  #the login url

br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
#br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

br["email"] = "*******************@gmail.com" #the key "username" is the variable that takes the username/email value

br["password"] = "******"    #the key "password" is the variable that takes the password value

logged_in = br.submit()   #submitting the login credentials

src = logged_in.read()  #reading the page body that is redirected after successful login

print (src) #printing the body of the redirected url after login

#req = br.open("http://school.dwit.edu.np/mod/assign/").read()
#accessing other url(s) after login is done this way 


# In[ ]:





# In[15]:


#Gyaan upload 

br.open("http://classroom.campusx.in/gyan")

#try1
br.select_form(nr = 0)
br["gyanlink"] = random_choice1
logged_in = br.submit()   #submitting the form
#try2
br.select_form(nr = 0)
br["gyanlink"] = random_choice2
logged_in = br.submit()   #submitting the form
#try2
br.select_form(nr = 0)
br["gyanlink"] = random_choice3
logged_in = br.submit()   #submitting the form


src = logged_in.read()  #reading the page body that is redirected after form submit login
soup = bs4.BeautifulSoup(src, 'html.parser')
alert = soup.find('div', class_="alert alert-warning alert-dismissible")
msg=alert.text
if msg=='\n×\n\n    You have already shared today. Try again tomorrow\n':

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        subject = 'Hi Tuhin, This is a python generated email'
        body = 'Gyann have been submitted today'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email, '********************@gmail.com', msg)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Gyann have been submitted today',
        to='whatsapp:+91700399****'
    )



else:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        subject = 'Hi Tuhin, This is a python generated email'
        body = 'Gyann have not been submitted today, upload it manually'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email, '**************************@gmail.com', msg)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Gyann have not been submitted today',
        to='whatsapp:+91700399****'
    )







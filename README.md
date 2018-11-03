# python-Automate
I will be uploading all the python scripts I will be using to make my life a little easier

## Download Python3:-
I made all of my projects using python3, it will be replaced in the future by its succesor but I belive the changes in the syntax will be minimal so if you have python version other than 3.X look out for changes in my code

[To download python](https://www.python.org/downloads/)

## Automated emails
What I wanted to do was automate the task of sending email with same content(body,subject) to more than one people and with a image as an attachment so  I created 3 programs for this task.
Please remember to change the directory according to your pwd if you use my code as i have the source variable set to my directory
I used a for loop to loop through the data stored in the excel sheet which I collected from google forms. I created a goole form which asks the user to input their name and email address.
### project5.py
(This was my project no 5 hence the name)

#### Important modules to download:-
1)yagmail:-
This will help you in automating the email sending procedure just type 
```
pip install yagmail
``` 
to install the python module


2)keyring:-
This helped me with saving my gmail password. You can use this with any website you want to store the password. I used this so that I would'nt have to display my passcode for my account when i upload it the code on GitHub. Just type
```
pip install keyring
``` 
to download this module. Also set your password for your email in terminal not in your program

[How to use this module read here](https://alexwlchan.net/2016/11/you-should-use-keyring/)


3)xlrd:- 
I used this module to read the excel file which had the data stored from the google forms. If you would like to learn how to use this module in depth then please read its documentation.To install it type 
```
pip install xlrd
```
in your command prompt or teminal window

[Documentation](https://xlrd.readthedocs.io/en/latest/)

[If you would like to know just the part I used, use this website](https://www.geeksforgeeks.org/reading-excel-file-using-python/)


#### Description:-
This is the main part of the Automate program folder this is the part where the user will start the connection,register,enter the contents and  send the email. I used the for loop to send the email to multiple people

### imagesdownload.py

I used this script to download google images in bulk without me having to manually download them 

just type 
```
pip install google_images_download
``` 
to download the necessary packages.

[How to use this module please read here](https://github.com/hardikvasa/google-images-download)

### filerename.py
The images which were downloaded were named with different names and I wanted to rename them. For this I used the os module of python(it comes pre installed with python). I renamed all the images in a order so that I can use it in the for loop   


### motivational-quotes-
The folder with the images I downloaded

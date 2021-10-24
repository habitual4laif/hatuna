#variables and strings
dat = "we are here already. "
p = 3
bee = dat * p
print(bee)

#
players = [34, 64, 74, 92, 16, 73]
players[:2] #we need the first two

#
players = [34, 64, 74, 92, 16, 73]
players[2:] #we need the numbers after the first two

#if/else statement
name = 19
if name < 18:
    print("Drink is not for you")
elif name == 18:
    print("You have to have celebrated your 18th")
else:
    print("Enjoy your drink")

#for loop
food = ['beans', 'rice', 'eba', 'garri', 'fufu']

for f in food:
    print(f)
    print(len(f))

#
food = ['beans', 'rice', 'eba', 'garri', 'fufu']

for f in food[3:]:
    print(f)
    print(len(f))

#appending/adding more items to a list
food = ['beans', 'rice', 'eba', 'garri', 'fufu']

food.append('moi-moi')
print(food)

#
food = ['beans', 'rice', 'eba', 'garri', 'fufu']

print(food)
food[:3] = ['moi-moi', 'bread'] #This permanently delete the items and add new ones
print(food)
food[3:] = ['moi-moi', 'bread']
print(food)

#The use of range()
for x in range(5):
    print(x)

#
for x in range(5, 12):
    print(x)

#
for x in range(3):
    print("Who's home?")

#The first value tell it where to start from  and the next where to stop while the last determine the interval
for x in range(10, 30, 5):
    print(x)

#video10
num = 5

while num < 10:
    print(num)
    num += 1


#
NumberRange = 26

for n in range(101):
    if n is NumberRange:
        print(n, 'This is the number')
        break

#Assignment
for n in range(1, 41):
    if n % 4 == 0:
        print(n, 'This number is divisible by 4')

#
NumbersTaken = [2, 5, 7, 4, 8]

for n in range(1, 10):
    if n in NumbersTaken:
        continue
    print(n)


#Creating a function
def usd_naira(usd):
    total = 489 * usd
    print(total)
    
usd_naira(80)
usd_naira(1000)

#You can't use the result of a function without the keyword RETURN
def allow_to_date(guys_age):
    girls_age = guys_age/2 + 7
    return girls_age

for n in range(26, 36, 2): #this select ages of guys
    guy_1 = allow_to_date(n)
    print("Your age is ",n, " and you are allowed to date ladies of year ", guy_1, " or older")


#Setting a default value for a function 
def gender(sex = "Unknown"):
    if sex == 'm':
        sex = "Male"
    elif sex == 'f':
        sex = "Female"
    print(sex)

gender('m')
gender('f')
gender()


#Key argument 
def key_argument(name ='Ade', action = 'is', obj = 'boy', ans = 'Yes'):
    print(name, action, obj, ans)

key_argument()
key_argument('Ola', 'went', 'to school', 'today')
key_argument(action='mumu')
key_argument(ans = 'no', name ='Sade')


#Flexible number argument
def addition(*anyword): #Any word after * sign can accommodate large variables
    total = 0
    for a in anyword:
        total += a
    print(total)
    
addition(50)
addition(32, 44, 37)
addition(474464, 5775858, 334)

#Unpacking argument
def cgpa(math, phy, chem, eng):
    gpa = (math*0.25) + (phy*0.25) + (chem*0.25) + (eng*0.25)
    print(gpa)
    
score = [76, 71, 65, 53]
cgpa(score[0], score[1], score[2], score[3]) #Instead going this route, unpack everything with a short code
cgpa(*score) #This is the unpacking


#Dictionary what has {} is called set in python video20
classmates = {'Ola':' is tallest', 'Ade':' is shortest', 'Bisi':' is smartest', 'Ada':' is dumbest'} #first parameter is call key while the second parameter is call value

for key, value in classmates.items(): #You can use any word or letter for 'key' and 'value'
    print(key + value)



#Modules
import another #this file is available on same folder
import random #this file came with python

another.beans()
y = random.randrange(1, 200)
print(y)


#To download image from a webpage Video22
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + '.jpg'   #To change number to string datatype, use "str()"
    urllib.request.urlretrieve(url, fullname)
    
download_web_image("http://www.strutchannelfittings.com/assets/images/LED%201.jpg")


#How to write on a file video23
fw = open('simple.txt', 'w') #the first string in open() name the file and the next tell it what to do. w (a keyword) means write
fw.write('This is what I intend writing on this file\n')
fw.write('What do you think i should write on this next line\n')
fw.close() #Ensure each file is closed after writing or reading


fr = open('simple.txt', 'r') #This is to read the file created earlier
text = fr.read()
print(text)
fr.close()


#Download a csv file video24
from urllib import request

csv_url = 'https://support.spatialkey.com/wp-content/uploads/2021/02/Sacramentorealestatetransactions.csv'

def download_csv(csv_url):
    result_of_url = request.urlopen(csv_url) #This open the url of the csv file we want to download
    csv = result_of_url.read() #This will read the data gotten we just got
    csv_str = str(csv) #We want to be sure the data is a string
    lines = csv_str.split(r'\r') #We want ensure the data is not one line but break the lines 
    destination = r'data_real11001a.csv' #This is the name we give the file
    file_name = open(destination, "w") #We will paste/write the data on the file
    for line in lines:
        file_name.write(line + "\n")
    file_name.close()

download_csv(csv_url)

#Web crawlers Videos 25-27
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        url = 'https://www.hotnigerianjobs.com/field/223/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html5lib')
        for link in soup.findAll('a', {'rel': 'bookmark'}):
            href = link.get('href')
            title = link.string
           # print(href)
            #print(title)
            get_single_item_data(href)

        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html5lib')
    for item_name in soup.findAll('a', {'rel': 'bookmark'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)

trade_spider(1)


#Creating Class and Object
class Enemy:
    life = 3

    def attack(self):  #for functions inside a class, 'self' is what will be inside the bracket
        print('ouchi')
        self.life -= 1

    def check(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print('Enemy has ' + str(self.life) + ' life left')

enemy1 = Enemy() #enemy1 is an objet of class Enemy
enemy2 = Enemy() 
enemy1.attack()
enemy1.attack()
enemy1.check()
enemy2.check()


#Initiallizing init
class Enemy:

    def __init__(self, x):
        super().__init__()
        self.energy = x
        print('What again!') #Even if this is not called, it will definitely run first

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()


#Initiallizing init
class Girl:

    gender = 'female'  #This is a class variable (It will be default for everyone - as female)

    def __init__(self, name):
        super().__init__()
        self.name = name #This is an instance variable
        self.gender = 'male'

a = Girl('Sade')
b = Girl('Jumoke')

print(a.gender)
print(a.name)
print(b.gender)
print(b.name)


#Class inheritance
class Parent():

    def last_name(self):
        print('Biden')

class Child(Parent): #By default once the Parent classname is added to a child class, the child inherit everything the parent has
    def first_name(self):
        print('Joe')

#    def last_name(self):
#        print('Bush') #The childclass has power to over write whatsoever the parent has by creating it's own

name = Child()
name.first_name()
name.last_name()


#Multiple inheritance 
class Mario():
    
    def move(self):
        print('I can move around')

class BigMario():

    def eat(self):
        print('I eat to be big')

class SmallMario():

    def smaller(self):
        print('I am smaller because of an enemy')

class BiggerMario(Mario, BigMario, SmallMario): #This class can inherit as many class as possible
    pass #This do nothing but use to continue the execution with getting error

life = BiggerMario()
life.move()
life.eat()
life.smaller()


#Threading
import threading

class Messager(threading.Thread):
    def run(self):
#        return super().run()
        for _ in range(10): #What _ means is that we don't care about what the value of the looping is. Just loop for us jare
            print(threading.currentThread().getName())


send = Messager(name = 'We are sending a Message')
receive = Messager(name = 'We are receiveing a Message')
send.start()
receive.start()


#Word frequency counter
import requests
from bs4 import BeautifulSoup #Whenever we want to pick things from the webpage we need BeautifulSoup
import operator

def bstart(url):
    word_list = []
    source_code = requests.get(url).text #the dot text (.text) makes it return text and not other form of dataset
    bsoup = BeautifulSoup(source_code, 'html5lib') #whenever we use BeautifulSoup, we will need a soup object (name it anything)
    for post_text in bsoup.findAll('a', {'rel': 'bookmark'}): #find all a tags that has this class attributes
        content = post_text.string #dot string (.string) will only take the content in the html tag
        words = content.lower().split() #dot lower (.lower) makes all words in lower case while .split break each word
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*)(_-+=~<>?:|}{\"[];'\/.,"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print(key, value)

bstart('https://www.hotnigerianjobs.com/field/223/electrical-electronic-engineering-jobs-in-nigeria')
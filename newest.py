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


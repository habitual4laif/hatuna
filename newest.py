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
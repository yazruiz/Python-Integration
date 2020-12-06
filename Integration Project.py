# Yazmin Ruiz

# Combination of programing knowledge

# Disney Vacation Budget/planning
# Meant to give users a better idea as to how much they will be spending and
# what decisions they will have to make during their Disney Vacation


name = input("What is your name? ")
print("Hello", name)
resident = input("Are you a Florida resident? ")
if (resident == "yes") or (resident == "Yes") or (resident == "YES"):
    print("Congratulations!, You qualify for a Florida Resident Discount")
else:
    print("No available discount")

stay = input("Are you interested in staying on Disney Property? ")
if (stay == "Yes") or (stay == "yes") or (stay == "YES"):
    print("Great, Let the magic begin!")
else:
    print("We'll gather other options")

# All of the following information comes from: https://disneyworld.disney.go.com/resorts/

resort = input("Would you like to stay in a 1. value, 2. moderate, 3. deluxe, or 4. deluxe villa resort? ")
if (resort == "1") or (resort == "value"):
    print("Options: All Star, All-Sports, and Pop Century")
elif (resort == "2") or (resort == "moderate"):
    print("Options: Coronado Springs, Port Orleans- Riverside, Port Orleans- French Quarter, Caribbean Beach")
elif (resort == "3") or (resort == "deluxe"):
    print("Options: Grand Floridian, Contemporary, BoardWalk Inn, Polynesian, Beach Club, Yacht Club, Animal Lodge")
elif (resort == "4") or (resort == "deluxe villa resort"):
    print("Options: Old Key West, B.W Villas, B.C Villas, Saratoga, G.F Villas, Polynesian Bungalows,& Riviera Resort")
else:
    print("We suggest to look into Airbnb, Expedia, Trivago, or Hotel.com")
price_range = input("What is the highest you are willing to pay a night? ")
# print(price_range + 100)
# Note: Update prices
if price_range <= "268":
    print("Suggested: a value resort")
elif price_range >= "505":
    print("Suggested: a moderate resort")
elif price_range >= "1,626":
    print("Suggested: a deluxe resort")
elif price_range >= "2,539":
    print("Suggested: a deluxe villa resort")
else:
    print("No available matches")

nights = input("How many nights will you be staying? ")
children = input("Number of Children under the age of 10: ")
adults = input("Number of Adults: ")
total_guests = (int(children) + int(adults))

estimated_stay = input("Estimated price of stay per night: ")
# cpa = "Cost Per Adult"

estimated_stay_total = (int(estimated_stay) * int(nights))
cpa = (int(estimated_stay_total) / int(adults))
print("Total Cost Per Adult:", cpa)

# estimated_budget = input("How much do you think you should be saving? ":)
# final_cost =

# BEGINNING OF SPRINT 2: #

num = 1
while num <= 2:
    print("Are you excited yet?!")
    num = num + 1

tickets = input("Are you looking into booking park tickets? ")
if (tickets == "Yes") or (tickets == "yes") or (tickets == "YES"):
    print("More excitement to come!")
else:
    print("No worries, you can still have an exciting time!")

child = input("Are you looking into booking children's tickets? ")
if (child == "Yes") or (child == "yes") or (child == "YES"):
    print("Stay tuned to find out if your child qualifies for the ticket")
else:
    print("An adult getaway it is!")

age = input("How old is your oldest child looking for a children's ticket? ")
if age <= "10":
    print("Your child qualifies for the children's ticket!")
else:
    print("Sorry, your child does not qualify for a child's ticket")

meal = input("The disney meal plan applies to everyone, yes or no? ")
if (meal == "Yes") or (meal == "yes") or (meal == "yEs") or (meal == "YEs") or (meal == "YES"):
    print("False")
if (meal == "No") or (meal == "NO") or (meal == "nO") or (meal == "no"):
    print("True")
else:
    print("Not a valid choice")

propertyStay = input("Are you planning on staying on Disney property? ")
extraPay = input("Are you willing to pay extra $90 per person per night? ")
plan = (propertyStay == "yes") and (extraPay == "yes")
if plan == "yes":
    print("True")
if plan == "no":
    print("False")
print("The Disney meal plan is right for you", plan)

food = input("Are you interested in different nearby food options besides disney meal plan")
if (food == "yes") or (food == "Yes") or (food == "YES"):
    print("Stay tuned for more information")
else:
    print("We suggest thinking about the disney dining plan again")

# enter number without the "."
foodType = input("Are you interested in dining 1. fast food, 2. restaurant, 3. bar, 4. Fine/Formal dining?")
if foodType == "1":
    print(
        "Options: McDonald's, Chick-fil-A, Wendy's, Burger King, Taco Bell, Siestas Cantina, or QDOBA Mexican Eats")
elif foodType == "2":
    print(
        "Options: LongHorn, Millers Ale House, T-Rex Cafe, Cheesecake Factory, Rainforest Cafe, or The Boathouse,")
elif foodType == "3":
    print(
        "Options: Geyser Point B&G, Hurricane Hanna's Waterside B&G, Oasis B&G, or The Hideaway B&G")
elif foodType == "4":
    print(
        "Options: Victoria & Alberts, Bull & Bear Steakhouse, Chatham's Place, Urbain 40, Ocean Prime, or The Boheme")
else:
    print("Not a valid option")

import random
opt1 = ('McDonalds', 'Chick-fil-A', 'Wendys', 'Burger King', 'Taco Bell', 'Siestas Cantina', 'QDOBA Mexican Eats')
opt2 = ('LongHorn', 'Millers Ale House', 'T-Rex Cafe', 'Cheesecake Factory', 'Rainforest Cafe',
        'The Boathouse')
opt3 = ('Geyser Point B&G', 'Hurricane Hannas Waterside B&G', 'Oasis B&G', 'The Hideaway B&G')
opt4 = ('Victoria & Alberts', 'Bull & Bear Steakhouse', 'Chathams Place', 'Urbain 40', 'Ocean Prime', 'The Boheme')
cantDecide = input("Can't decide where to eat? No problem. Did you previously decide on : 1, 2, 3, or 4?")
if cantDecide == "1":
    print(random.choice(opt1))
elif cantDecide == "2":
    print(random.choice(opt2))
elif cantDecide == "3":
    print(random.choice(opt3))
elif cantDecide == "4":
    print(random.choice(opt4))
else:
    print("Not a valid choice")

# staying on disney property
# willing to pay extra $90 per person per night

# Notes to self #
# parks
# how many days planned on spending in parks
# days off planned?
# disney hotel amenities/ activities
# suggest a stay/ resort based on activity interest on their day off park if applicable
# generate random park suggestion if unsure where they would like to visit based on interest
# Notes to self end #

# BEGINNING OF SPRINT 3 :) #
# rearrange #

parks = input("How many days would you like to visit Disney parks? ")
if parks >= "15":
    print("Each day is a new experience!")
else:
    print("Let's make the most out of it!")

parkDecision = input("Are you unsure of which park to visit first? ")
if (parkDecision == "Yes") or (parkDecision == "yes") or (parkDecision == "YES"):
    print("We can help with that!")
else:
    print("Sounds like you've made up your mind!")

park = input(
    "Choose a category: 1. Thrill rides, 2. Food/ Culture, 3. Character meets, 4. Animals/ Wildlife")
if (park == "1") or (park == "1."):
    print("A more suited park for this category would be: Hollywood Studios")
elif (park == "2") or (park == "2."):
    print("A more suited park for this category would be: Epcot")
elif (park == "3") or (park == "3."):
    print("A more suited park for this category would be: Magic Kingdom")
elif (park == "4") or (park == "4."):
    print("A more suited park for this category would be: Animal Kingdom")
else:
    print("Sorry, not a valid choice")

pick = "Not sure which park to go to first since they are all so unique?,no problem we'll randomly pick for you! "
print(pick)

import random
parkChoice = ('Hollywood Studios', 'Epcot', 'Magic Kingdom', 'Animal Kingdom')
randomResult = random.choice(parkChoice)
print(randomResult)

# works now ^

relax = input("Do you have any relaxation days planned where you want to take a break from parks? ")
if (relax == "Yes") or (relax == "yes") or (relax == "YES"):
    print("No worries all have those days ")
elif (relax == "No") or (relax == "no") or (relax == "NO"):
    print("Kudos to you for braving the parks")
elif (relax == "not sure") or (relax == "maybe") or (relax == "Maybe") or (relax == "idk"):
    print("Let's see if we can come to a solution")
else:
    print("Orlando is full of exciting of activities")

# https://disneyworld.disney.go.com/things-to-do-orlando/

act = input("Are you looking for any activities to do in Orlando if you consider having days off? ")
if (act == "Yes") or (act == "yes") or (act == "YES") or (act == " of course"):
    print("Let's work on finding some that are of your interest")
elif (act == "No") or (act == "no") or (act == "not likely") or (act == "NO"):
    print("We hope you'll reconsider, there's so much to do!")
elif (act == "maybe") or (act == "idk") or (act == "not sure") or (act == " i don't know") or (act == "i don't know"):
    print("No pressure!")
else:
    print("Not a valid choice")
# https://www.westgatereservations.com/blog/50-things-to-do-in-orlando/

orlandoAct = input(
    "Choose a category: 1. Outdoor Activities, 2. Shopping, 3. Education/Museums, 4. Indoors ")
if (orlandoAct == "1") or (orlandoAct == "1."):
    print(
        "Activities: Golfing, Horseback Riding, Archery, Boating, Nature Trails, Jet Ski, or Swimming with Dolphins")
elif (orlandoAct == "2") or (orlandoAct == "2."):
    print("Activities include: Disney Springs, Mall at Millennia, Orlando Premium Outlets, or The Florida Mall ")
elif (orlandoAct == "3") or (orlandoAct == "3."):
    print("Activities include: Kennedy Space Center, Titanic Exhibition, Orlando Museum of Art, or Madame Tussauds")
elif (orlandoAct == "4") or (orlandoAct == "4."):
    print("Activities include: Wonderworks, Escape Rooms, Go-kart, Indoor skydiving, Paintball, or Bowling")
else:
    print("Sorry, not a valid choice")

import random
pick1 = ('Golfing', 'Horseback Riding', 'Archery', 'Boating', 'Nature Trails', 'Jet Ski', 'Swimming with Dolphins')
pick2 = ('Disney Springs', 'Mall at Millennia', 'Orlando Premium Outlets', 'The Florida Mall')
pick3 = ('Kennedy Space Center', 'Titanic Exhibition', 'Orlando Museum of Art', 'Madame Tussauds')
pick4 = ('Wonderworks', 'Escape Rooms', 'Go-kart', 'Indoor skydiving', 'Paintball,Bowling')
pick = input("Interested in activities but not sure which you'd rather do?, please type in your previous response ")
if (pick == "1") or (pick == "1."):
    print(random.choice(pick1))
elif (pick == "2") or (pick == "2."):
    print(random.choice(pick2))
elif (pick == "3") or (pick == "3."):
    print(random.choice(pick3))
elif (pick == "4") or (pick == "4."):
    print(random.choice(pick4))
else:
    print("Sorry, not a valid choice")

final = "By now you should have a general idea on your trip to Disney, Let the adventure begin!"
print(final)

# continue to work on project to make improvements even after submission

# NEEDED THE FOLLOWING FOR SPRINT 2: #
# Already had, just switched it to the bottom so it wouldn't get in the way of actual project program #

# Range:
num = range(1, 5)
for num in num:
    print(num)

# try to figure out where to place ^ in code

# For:
for item in range(3):
    print(item ** 4)

# In:
nums = [2, 4, 6]

for num in nums:
    for letter in "abc":
        print(num, letter)


# Passing Parameter:
def example(param):
    var1 = param * 2
    return var1


var2 = 2
returnValue = example(var2)
print(returnValue)

# !=:
num1 = int(input("Enter a value: "))
num2 = int(input("Enter a value: "))
if num1 == num2:
    print("True")
if num1 != num2:
    print("False")

# Not:
x1 = 2
y1 = 2
x2 = "Python"
y2 = "Python"
x3 = [3, 4, 5]
y3 = [3, 4, 5]
print(x3 is not y3)

# NEEDED THE FOLLOWING FOR SPRINT 1 #
# Already had, just switched it to the bottom so it wouldn't get in the way of actual project program #

# Using %:
c = 4
d = 3
print("Total:", c % d)

# Using **:
number1 = int(input("Enter value: "))
number2 = int(input("Enter value: "))
print("Total of values: ", number1 ** number2)

# Using // :
students = int(input("Number of students: "))
groups = int(input("Number of groups needed: "))
print("Total of groups possible: ", students // groups)

# Using - :
value1 = int(input("Enter a value: "))
value2 = int(input("Enter a value: "))
print("Answer: ", value1 - value2)



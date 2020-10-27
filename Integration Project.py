# Yazmin Ruiz

# Combination of programing knowledge

# Disney Vacation Budget/planning
# Meant to give users a better idea as to how much they will be spending and what decisions they will have to make during their Disney Vacation
            
name = input("What is your name? ")
print("Hello",name)
resident = input("Are you a Florida resident? ")
if (resident == "yes") or (resident == "Yes") or (resident == "YES"):
    print("Congratulations!, You qualify for a Florida Resident Discount")
else:
    print("No available discount")
    
stay = input("Are you interested in staying on Disney Property? ")
if stay == (stay == "Yes") or (stay == "yes") or (stay == "YES") :
    print("Great, Let the magic begin!")
else:
    print("We'll gather other options")
    
# All of the following information comes from: https://disneyworld.disney.go.com/resorts/

resort = input("Would you like to stay in a 1. value, 2. moderate, 3. deluxe, or 4. deluxe villa resort? ")
if resort == "1":
    print("Your options include: All Star, All-Sports, and Pop Century")
elif resort == "2":
    print("Your options include: Coronado Springs, Port Orleans- Riverside, Port Orleans- French Quarter, Caribbean Beach")
elif resort == "3":
    print("Your options include: Grand Floridian, Contemporary, BoardWalk Inn, Polynesian, Beach Club, Yacht Club, Animal Lodge")
elif resort == "4":
    print("Your options include: Old Key West, Board Walk Villas, Beach Club Villas, Saratoga Springs, G.F Villas, Polynesian Bungalows,& Riviera Resort")
else:
    print("We suggest to look into Airbnb, Expedia, Trivago, or Hotel.com")
price_range = input("What is the highest you are willing to pay a night? ")
#print(price_range + 100)
# Note: Update prices
if price_range <= ("268"):
    print("Suggested: a value resort")
elif price_range >= ("505"):
    print("Suggested: a moderate resort")
elif price_range >= ("1,626"):
    print("Suggested: a deluxe resort")
elif price_range >= ("2,539"):
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

############ BEGINNING OF SPRINT 2: ############ 

num = 1
while num <= 2:
    print("Are you excited yet?!")
    num = num + 1

tickets = input("Are you looking into booking park tickets? ")
if (tickets == "Yes") or (tickets == "yes") or (tickets == "YES"):
    print("More excitment to come!")
else:
    print("No worries, you can still have an exciting time!")
    
child = input("Are you looking into booking childrens tickets? ")
if (child == "Yes") or (child == "yes") or (child == "YES"):
    print("Saty tuned to find out if your child qualifies for the ticket")
else:
    print("An adult getaway it is!")
    
age = input("How old is your oldest child looking for a childrens ticket? ")
if age <= ("10"):
    print("Your child qualifies for the childrens ticket!")
else:
    print("Sorry, your child does not qualify for a childs ticket")

meal = input("The disney meal plan applies to everyone")
if (meal == Yes) or (meal == yes) or (meal == yEs) or (meal == YEs) or (meal == YES):
    print("False")
if (meal == No) or (meal == NO) or (meal == nO) or (meal == no):
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
    
#enter number without the "."
foodType = input("Are you interested in dining 1. fast food, 2. resturant, 3. bar, 4. Fine/Formal dining?" )
if foodType == "1":
    print("Some popular options include: McDonalds, Chick-fil-A, Wendy's, Burger King, Taco Bell, Culver's, Siestas Cantina, or QDOBA Mexican Eats")
elif foodType == "2":
    print("Some popular options include: LongHorn, The Melting Pot, Millers Ale House, T-Rex Cafe, Cheesecake Factory, Rainforest Cafe, or The Boathouse,")
elif foodType == "3":
    print("Some popular options include: Geyser Point B&G, Hurricane Hanna's Waterside B&G, Oasis B&G, or The Hideaway B&G")
elif foodType == "4":
     print("Some popular options include: Victoria & Alberts, Bull & Bear Steakhouse, Chatham's Place, Capa, Urbain 40, Ocean Prime, or The Boheme")
else:
    print("Not a valid option")

import random
opt1 = ('McDonalds', 'Chick-fil-A', 'Wendys', 'Burger King', 'Taco Bell', 'Culvers', 'Siestas Cantina', 'QDOBA Mexican Eats')
opt2 = ('LongHorn', 'The Melting Pot', 'Millers Ale House', 'T-Rex Cafe', 'Cheesecake Factory', 'Rainforest Cafe', 'The Boathouse')
opt3 = ('Geyser Point B&G', 'Hurricane Hannas Waterside B&G', 'Oasis B&G', 'The Hideaway B&G')
opt4 = ('Victoria & Alberts', 'Bull & Bear Steakhouse', 'Chathams Place', 'Capa', 'Urbain 40', 'Ocean Prime', 'The Boheme')
cantDecide = input("Can't decide where to eat? No problem we'll randomly select for you. Did you previously decide on : 1, 2, 3, or 4?")
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

############ NEEDED THE FOLLOWING FOR SPRINT 2: ############

# Range:
num = range(1,5)
for num in x:
    print(num)

#Still trying to figure out where to place ^ in code

# For:
for item in range(3):
    print(item**4)

# In:
nums = [2,4,6]

for num in nums:
    for letter in "abc":
        print(num, letter)

# Passing Parameter:
def example(param):
    num1 = param *2
    return num1
num2 = 2
returnValue = example(num2)
print(returnValue)

# !=:
num1 = int(input("Enter a value: "))
num2 = int(input("Enter a value: "))
if num1 == num2:
    print("True")
if num1 != num2:
    print("False")

# Not: ???
x1 = 2
y2 = 2
x2 = "Python"
y2 = "Python"
x3 = [3,4,5]
y3 = [3,4,5]
print(x3 is not y3) 

####### NEEDED THE FOLLOWING FOR SPRINT 1 #######
### Already had, just switched it to the bottom so it wouldnt get in the way of actual project program ###

#Using %:
c = 4
d = 3
print("Total:", c % d)


#Using **:
number1 = int(input("Enter value: "))
number2 = int(input("Enter value: "))
print("Total of values: ", number1 ** number2)

#Using // :
students = int(input("Number of students: "))
groups = int(input("Number of groups needed: "))
print("Total of groups possible: ", students // groups)

#Using - :
value1 = int(input("Enter a value: "))
value2 = int(input("Enter a value: "))
print("Answer: ", value1 - value2)



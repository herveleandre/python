#

def foo(amount):
    output = amount * amount
    return output

print(foo(3))



#######  Function that converts fliud ounces to milliliters 1 ounce to 29.57353 militrs

def foo(amount):
    output = amount * 29.57353
    return output

print(foo(5))


################################### Warm or COld ################################
def foo (tempature):
    if tempature > 7:
        return "Warm"
    else:
        return "Cold"
    
print(foo(10))


#################################   Password Controller      ###################

def foo (password):
    if len(password) >= 8:
        return "True"
    else:
        return "False"

print (foo("mypasxcvcxvVFs"))


############################# HOT WARM OR COLD ###############################

def foo (tempature):
    if tempature > 25:
        return "Hot"
    elif 25 >= tempature >= 15:
        return "Warm"
    else:
        return "Cold"
    
print(foo(10))


############################# Formatting and UPPERCASE ###############################

def foo(person):

    return f"Hi {name.title()}"
name = input("Enter name: ")
print (foo(name))


############################# LOOPING OVER DICTIONARY AND REPLACE ###############################

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for number in phone_numbers.values():
    
    print(number.replace("+", "00"))


    ############################# SENTENCE MAKER TEXT PRO ###############################
def sentence_maker(phrase):
    special_words = ("how", "when", "what")
    capitalized = phrase.capitalize()
    if phrase.startswith(special_words):
        return "{}?".format(capitalized)
    else:
        return "{}.",format(capitalized)

results = []    
while True:
    user_input = input ("Say Something:")
    if user_input == ("end"):
        break
    else: results.append(sentence_maker(user_input))

print(results)


#############################  ###############################
def foo(*args):
    return sum(args) / len(args)
print (foo(10, 20, 30, 40))

############################# INFINITE ARGS args  ###############################
def foo(*args):
     args = [x.upper() for x in args]
     return sorted(args)
print(foo("snow", "glacier", "iceberg"))


############################# READING AND PROCESSING TEXT  ###############################
file = open("bear.txt")
content = file.read()
file.close()
print(content[:90])

#############################   ###############################
with open("file.txt", "w") as file:
    file.write("snail")


############################# EXTRACTING DATA FROM TEXT FILE AND WRITE TO NEW TEXT FILE  ###############################
file = open("bear.txt")
content = file.read()
file.close()
with open("first.txt", "w") as first:
    first.write(content[:90])
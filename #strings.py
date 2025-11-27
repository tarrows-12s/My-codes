#string, space, symbols inside 3x quotes will be saved 
poem2 = ''' I do not like thee, Doctor Fell.
            The Reason why, I cannto tell.
            But this I know, and know full well.
            I do not like thee, Doctor Fell. '''

#Placing qutoes in text with \"
testimony = '\"I did nothing!\" hes said. \"Or that other thing.\"'
fact = "The world's largest rubber was 54'2\" by 65'7\" by 105'"

#But if you need Blackslash, use (\\)
speech = "The backslash (\\) bends over backwards to please you."

#escape-symbols do not work in unproccesed strings 
info = r"Type a \n to get a new line in a normal string"

#In unprocceced strings work the real(and not '\n') switching to a new string.
poem = r"""Boys and Grils, come out to play.
The moon doth shine as brught as day."""

#In python you can connect a string to another string with the symbol '+'
'Realease the kraken!' + 'No, wait!'

#You can connect strings just putting them near to the another string.
"My word!" "A gentleman caller!"

#If similiar things are too many, to avoid switching to a new line, you can use brackets.
vowels = ('a'
          "e" '''i'''
          'o' """u""")
print(vowels)

#Python does not create space between strings. Python creates space between strings using 'print()'
a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c 
print(a, b, c)

#You can multiply strings using the symbol '*'
start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye'
print(start + start + middle + end)     #Attention: operator '*' has more priority than the oprator '+'

#Extracting symbols using the symbol '[]'. To extract a symbol, type the the number of its position.
#Example: from [0] you are extracting from the beginning and [-1] from the end.
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]      #The result will be 'a' 
letters[1]      #Here it will be 'b'
letters[-1]     #Here will be the result 'z'

#A string with and without a Control Character '\n':
no_ControlCharacter = "My name is bob"
yes_ContolCharacter = "My name is \nbob"

#Creating string using function 'str()'
str(53.5)       #result: '53.5'
str(1.0e4)      #result: '10000.0
str(True)       #result: 'True'

#Extracting substring, using division 
letters[:]  #result: "abcdefghijklmnopqrstuvwxyz"
letters[10:]    #result: "klmnopqrstuvwxyz"
letters[3:5]    #result: ""
letters[:7]
letters[9:5:3]
letters[-4:]
letters[18:-3]

#with function, len(), you can measure the length of strings:
len(letters)    #result: 26

empty = ''
len(empty)      #result:0

#splitting strings with the help of function "split()":
tasks = "get gloves,get mask,give cat vitamins,call ambulance"
tasks.split(',')                                                    #result: ["get gloves", "get mask", "give cat vitamins", " call ambulance"]

#joining strings with the of the function "join()"
crypto_list = ["yeti", "Bigfoot", "Loch Ness Monster"]
crypto_string = ", ".join(crypto_list)
print("Found and signing book deals:", crypto_string)   #result: Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

#replacing symbols using function replace():
setup = "a duck goes swimming..."
setup.replace("duck", "dog")    #output: a dog goes swimming...
#here, 50, stands for how many times should it get replaced
setup = "a duck goes swimming..."
setup.replace("duck", "dog", 50)    #output: a dog goes swimming...

#elimating symbols using function strip():
world = "     earth     "
world.strip()   #output: "earth"
#with function lstrip():
world = "     earth     "
world.lstrip()  #output: "earth     "
#with function rstrip():
world = "     earth    "
world.rstrip()  #output: "     earth"

#Search and Option:
poem2 = "All that doth flow we cannot liquid name Or else would fire and water be the same; But that is liquid which is moist and wet Fire that porperty can never get."
#First 13 symbols of poem2(from 0 to 12):
poem2[:12]  #output: "All that doth"
#How many symbols does poem2 contain?:
len(poem2)  #output: 158
#Does poem2 begin with "All"?:
poem2.startswith("All")     #output: True
#Does it end with the phrase "can never get"?:
poem2.endswith("can you get")     #output: False
#In python we have two methods to find a substring in the string - find() and index()

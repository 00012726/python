message = "I am a communist"
# print(len(message))# len(variable) shows the length of string
# input()

# print(message[0:5]) #starting from 0 index to 5th index, but 5th index is not included
# input()

# print(message[:5])  #you can do the same thing without including 0 itself, it will automatically start
#                     #from the beginning
# input()

# print(message[6:])  #the same thing but opposite
# input()

# print(message.lower())  #printing in lowercase the whole string
# print(message[0].lower())   #or only one letter

# print(message.upper()) #the same thing but makes uppercase whole string
# print(message[0].upper()) #or only one letter

# print(message.count('I')) #you can find the count of the string in the string

# print(message.find("communist")) #it will show the starting index of found string you gave

# print(message.replace('communist', 'capitalist'))   #you can replace any indicated and existing word
#                                                     #or piece of it by the next indicated string

# badMessage = message.replace("communist", "capitalist") #the same thing by declaring it into new variable
# print(badMessage)

name = "Azizbek"
greeting = "Hello"
# #1st option to print:
# intro = greeting + ", " + name + ". Welcome!"
# print(intro)

# #2nd option to print:
# intro = "{}, {}. Welcome!".format(greeting, name) #the same thing!
# print(intro)

# #3rd option to print:
# intro = f"{greeting}, {name}. Welcome!"
# print(intro)

# # some custom printing:
# intro = f"{greeting}, {name.upper()}. Welcome!"
# print(intro)

# if you want to know all functions that can be used:
# print(dir(message))

# # if you need detailed instructions to use all string functions:
# print(help(str))
# # you can indicate exact function:
# print(help(str.lower))

#==================INTEGERS AND FLOATS=========================

# #let's do a division
# print(3 / 2)

# #if you want floor division
# print(3 // 2)

# #exponent(numbers with the power of other number)
# print(3 ** 2)

# # absolute value
# print(abs(-3))

# # rounding(normal)
# print(round(3.75)) #4

# # rounding by indicating decimal index
# print(round(3.75, 1))

# # how to parse into integer:
# num1 = "100"
# print(int(num1) + 1)

# ====================================================LISTS=============================================================


courses = ['History', 'Physics', 'CompScience', 'Biology']
courses2 = ['Art', 1000]
nums = [1, 6, 5, 23, 55]

# print(courses) # printing whole list

# print(len(courses)) # printing length of list

# print(courses[0]) # printing by indicating element inside of list

# print(courses[-1]) # printing last item by indicating with negative numbers

# print(courses[:4]) # printing with index


# courses.append('Arts') # adding new item to list
# print(courses)

# courses.insert(0, 'Art') # adding item with index position
# print(courses)

# # you can add whole lists not only variables, but it will take the place of one index position
# courses.append(courses2)
# print(courses)

# # or by indicating position
# courses.insert(0, courses2)
# print(courses)
# print(len(courses))


# to add like to each other with separate index positions
# courses.extend(courses2)
# print(courses)

# courses.remove('History') # you can remove elements inside list
# print(courses)

# print(courses)
# courses.pop() # removes last item as default
# print(courses)


# courses.reverse() # reverse order
# print(courses)

# courses.sort() # will sort in alphabetical order
# print(courses)


# nums.sort() # will sort in ascending order
# print(nums)

# courses.sort(reverse=True) # sorting in reversed alphabetical order
# print(courses)

# nums.sort(reverse=True) # sorts in descending order
# print(nums)

# sortedCourses = sorted(courses)
# print(sortedCourses)

# print(min(nums)) # printing the minimum value from list

# print(sum(nums)) # printing total value of the values in list

# print(courses.index('CompScience')) # can get the index position of indicated value

# you can check the presence of a value in list
# print('Biology' in courses) # returns true of false

# for index, item in enumerate(courses, start = 1):
#     print(index, item)

# coursesStr = ', '.join(courses) # redeclaration with new variable and separating with comma
# print(coursesStr)

# # you can comeback to the previous state with this:
# newList = coursesStr.split(', ')
# print(newList)






# ==================================================TUPLES =====================================================

# tuples are immutable and list are mutable

tuple1 = ('Hello', 'Bye' , 'Hru')
# print(tuple1)

# tuple1[0] = 'Art'
# print(tuple1) # this will return error, cuz 'tuple' object does not support item assignment





# ==================================================SETS ==================================================================
courseSet = {'History', 'Biology', 'Informatic', 'Arts'}
courseSet2 = {'History', 'Biology', 'Math', 'CompScience'}
# print(courseSet) # sets does not care about order!
# # sets thow away duplicates

# print('Math' in courseSet) #returns true or false

# you can show the similar values in two sets like this:
# print(courseSet.intersection(courseSet2)) 

# # you can print different values which does not include similar ones:
# print(courseSet.difference(courseSet2))

# # you can unite values:
# print(courseSet.union(courseSet2))



# CREATING EMPTY LISTS, TUPLES AND SETS

# EMPTY LIST:
emptyList = []
emptyList = list()

# empty tuple
emptyTuple = ()
emptyTuple = tuple()

# empty set
# emptySet = {} # => this is not right way to create empty set, instead this will create a dictionary
emptySet = set() # this is the right way to crate empty set

    
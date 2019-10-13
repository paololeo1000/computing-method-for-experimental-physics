# Here we define the class
class Television:
    """ Television class. I will follow the convention of starting class names 
    with an uppercase. """
    pass # oops we have no code yet!

""" To create instances of a class in Python we use the parenthesis operator
'()'. The syntax is similar to calling a function -- which is actually what is 
happening behind the scenes, as we will see """
my_television = Television() # my_television is an instance of the class

print(type(my_television)) # Check its type

your_television = Television() # An this is another istance

# Let's check that they are really two different objects
print(my_television is not your_television)


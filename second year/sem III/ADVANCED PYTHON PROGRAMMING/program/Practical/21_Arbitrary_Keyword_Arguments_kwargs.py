# Program: Arbitrary Keyword Arguments **kwargs
# Question: Write a python program of Arbitrary arguments which accepts a dictionary of arguments.

# **kwargs collects keyword arguments into a dictionary
def my_function(**kid):
    print("Dictionary of arguments:", kid)
    print("Name is", kid["name"])
    print("Location is", kid["place"])

my_function(name="sachin", place="Mumbai")

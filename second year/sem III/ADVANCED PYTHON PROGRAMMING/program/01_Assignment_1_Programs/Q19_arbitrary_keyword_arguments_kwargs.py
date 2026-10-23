# Q19. Arbitrary Keyword Arguments (**kwargs) which accepts a dictionary of arguments (From Professor's Notes)
def my_function(**kid):
    print("location is", kid["place"])

my_function(name="sachin", place="Mumbai")  # call

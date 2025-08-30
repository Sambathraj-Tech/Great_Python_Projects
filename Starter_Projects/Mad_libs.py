# Story Telling Project

def get_input(word_type: str): # : str --> represent its a string
    user_input: str = input(f"Enter a {word_type}")
    return user_input

name1 = get_input("name1 : ") # Sambath Raj  -> noun
verb1 = get_input("verb1 : ") # Studing
verb2 = get_input("verb2 : ") # study

story = f"""{name1} is decided and move to chennai from his native 
for {verb1} in Besant Technologies.{name1} is {verb1} with his 
friends for more than 3 weeks but {name1} did'nt feel the course
improved {name1}'s knowledege so {name1} decided to {verb2} on his own 
by watching YouTube tutorials and {name1} learned SQL and improves
Query knowledge day by day.

Every single day {name1} decide to {verb2} for 6 hours.

I wish you {name1} to get your dream job ,keep your hope always."""           
print(story)

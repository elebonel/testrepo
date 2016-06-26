#write a function that takes two arguments, name of country and a major language spoken there
#call it three times, using a mix of positional and keyword arguments

def languages(country, language):
	print("country: %s, language: %s" %(country, language))

languages("Germany", "Germans")
languages(language = "Spanish", country = "Spain")
languages(language = "Italian", country = "Italy")



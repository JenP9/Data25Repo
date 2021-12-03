import requests
# In python we pip install the requests module
# Calling the requests module allows use request
# data from an api.


response = requests.get("http://randomfox.ca/floof")
# The get method is used to "get" information from the api.
# "floof" is a resource containing the data we are interested
# in
print(response.status_code)
# In http we want to see the 200 status code
# this means the requests was succesful and no errors occured.
print(response.text)
# The text method will show use the json information we
# requested from the api. We can see this is a dictionary
# with the keys "image" and "link".
print(response.json())
# The json method will make the links active and alter how
# the dictionary is printed
fox = response.json()
# We can set our api request to a variable.
print(fox["image"])
# Finally we will print just the image link by printing
# the fox variable with the key "image".
# We can now enjoy the results of our request!

# If we send another request to the api we will recieve
# a new image as a response.

# # All Imports
import re # regular expressions
import json # json

# ## Reading txt file

# read websiteData.txt file with encoding utf-8 otherwise encoding error

with open ('websiteData.txt', 'r',encoding='utf-8') as f: 
    lines=f.readlines() # readlines() returns a list of strings, one for each line in the file
    
    # for line in lines:    # testing if the file is read correctly
    #     print(line)


# ## Extract emails from txt file


# use regular expression to find email address
# findall >>	Returns a list containing all matches
# to find email address :
# \w for word character,digit,underscore
# + for one or more word character,digit,underscore, period, dash
# @ for @ symbol
# \. for . symbol (generally used to separate domain name from the top level domain ) and first_name(.)second_name(@)domain_name(.)top_level_domain
# - for - symbol (used to separate the first name from the last name)


string=str(lines) # convert the list to a string
email_list=re.findall('[\w\.=-]+@[\w\.-]+',string)  # find all email addresses in the string and store in email_list

# print(email_list) # print the list of email addresses



# ## Count and type of emails

#create dictionary with key as email address and value as the number of times the email address appears in the list
# email_list.count(email) # Count the number of times it appears in the list 


def email_type(em): # function to categorize the email address as Human or Non-Human
    if (re.search('[\w-]+\.[\w-]+', em.split('@')[0])) or len(em.split('@')[0])>=8: # if the first part of the email address is a word character,digit,underscore, dash and contain period (.) in between then it is a human email address  else it is a non-human email address    Also  if the first part of the email address is more than 8 characters then it is a human email address
        return 'Human'
    else:
        return 'Non-Human'


# Using dictionary  comprehension
email_dict={email:{'Occurance':email_list.count(email),'EmailType':email_type(email)} for email in email_list} # create a dictionary with key as email address and value as a dictionary with key as Occurance and EmailType


### Simplied version

# email_dict={} # create an empty dictionary
# for email in email_list:
#     email_dict[email]={'Occurance':email_list.count(email),'EmailType':email_type(email)} # add the email address and the number of times it appears in the list to the dictionary


print(email_dict) # print the dictionary



# ## Create result.json file

# Convert email_dict to result.json file
with open('result.json','w') as f: # create a new file with name result.json
    json.dump(email_dict,f,separators=(',', ':') )# dump the email_dict dictionary to the file result.json. The separators are used to separate the key and value in the dictionary and get rid of unwanted white spaces




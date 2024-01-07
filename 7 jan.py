#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sets (A set is a set of characters inside a pair of square brackets [] with a special meaning:)
#[arn]Returns a match where one of the specified characters (a, r, or n) is present	
import re
txt = "The rain in Spain"
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[1]:


#[a-n]Returns a match for any lower case character, alphabetically between a and n	
import re
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[2]:


#[^arn]	Returns a match for any character EXCEPT a, r, and n
import re
txt = "The rain in Spain"
x = re.findall("[^arn]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[3]:


#[0-9]	Returns a match for any digit between 0 and 9
import re
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[5]:


#[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
import re
txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[6]:


#[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
import re
txt = "8 times before 11:45 AM"

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[ ]:





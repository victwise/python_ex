# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:56:02 2018

@author: vict
"""

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
       Alright, so you said %r about liking me.
       You live in %r. Not sure Where that is.
       And you have a %r computer. Nice.
       """ % (likes, lives, computer))
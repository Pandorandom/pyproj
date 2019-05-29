#!/usr/bin/env python
#
#
#
# TOOL NAME: Pyproj
# WRITTEN BY: tacree
# DATE: 05-28-2019
# REV:
# First Worked: 05-28-2019
# Purpose: The purpose of this script is to offer a project creator application written in python over the original tool (bash).

# Style Notes (W.I.P. Idead for a section):
#
# Use camelCase notation for variables, etc.
#
#
#
#


#
# REV LIST:
# BY:
# DATE:
# CHANGES MADE:
#
#
#

#############################################################
# Section 1: Imports
#############################################################
import os, getpass, time, socket, sys
from github import Github
from Tkinter import *





#############################################################
# Section 2: Misc. Variables
#############################################################
username = getpass.getuser()
homeDirectory = os.path.expanduser("~")
hostname = socket.gethostname()

#############################################################
# Section 3: Functions
#############################################################

def checkProfile():
	bashProfile = '%s/.bash_profile' % homeDirectory
	check = os.path.exists(bashProfile)
	if check == True:
		bashProfile = '%s/.bash_profile' % homeDirectory
	elif check == False:
		bashProfile = '%s/.bashrc' % homeDirectory
		check2 = os.path.exists(bashProfile)
		if check2 == False:
			print("%s/.bash_profile and %s/.bashrc not found.")
			bashProfile = raw_input("Please indicate the location of your bash profile: ")
	else:
		print(usage)


def usage():
	print '''
	This script will create a new project directory in a target directory and offer the user the option to open a new tab of the directory as well as open the project folder in Atom Text editor.
'''

def clicked():
	lbl.configure(text="Button was clicked !!")

#############################################################
# Section 4: Main Body
#############################################################

#alias = raw_input("Do you want to create an alias in ~/.bash_profile?")

#if alias = "y":
#	bashProfile = open("~/.bash_profile","w+")
#	if bashProfile:
#		pass

window = Tk()
window.title("Welcome to Pyproj app")
window.geometry('350x200')
lbl = Label(window, text="Pyproj - Project Creator")
uNameButton = Button(window, text="Get system Username: ")
profilePath = Button(window, text="Get bash profile filepath: ")
uNameButton.pack(padx=10)
profilePath.pack(padx=10)
window.mainloop()

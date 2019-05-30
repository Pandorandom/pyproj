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

##########################################
# Style Notes (W.I.P. Idea for a section):
##########################################
# Use camelCase notation for variables, etc.
# Colored text output is done using ANSI escape codes. See:
# https://en.wikipedia.org/wiki/ANSI_escape_code
# for more info
#
#
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
# Going to run command line args to create folders and such. Getpass will allow sudo/password entry to be protected, time in case there's any sleep timers necessary, and sys/socket for system info.
import os, getpass, time, socket, sys
from github import Github
from Tkinter import *





#############################################################
# Section 2: Misc. Variables
#############################################################
# get system username
username = getpass.getuser()

# expands symlink of /home directory
homeDirectory = os.path.expanduser("~")

# Get hostname of machine - for git commit tracking in the future
hostname = socket.gethostname()


#############################################################
# Section 3: Functions
#############################################################

# Checks if bash profile is located in ~/.bash_profile or ~/.bashrc.
def checkProfile():
	bashProfile = '%s/.bash_profile' % homeDirectory
	check = os.path.exists(bashProfile)
	if check == True:
		bashProfile = '%s/.bash_profile' % homeDirectory
	elif check == False:
		bashProfile = '%s/.bashrc' % homeDirectory
		check2 = os.path.exists(bashProfile)
		# check2 fails (bashrc and bash_profile don't exist) and prompts the user for the full file location of their profile.
		if check2 == False:
			print("%s/.bash_profile and %s/.bashrc not found.")
			bashProfile = raw_input("Please indicate the location of your bash profile: ")
	else:
		print(usage)

	return;

def usage():
	print '''
	This script will create a new project directory in a target directory and offer the user the option to open a new tab of the directory as well as open the project folder in Atom Text editor.
'''
	return;

# Run git init on newly created project and sub files. Can also add a remote repository (github API to come one day, to allow for repo creation via the tool)
def gitInit( str ):
	initRepo = 'cd %s/projects/%s && git init' % (homeDirectory, projectName)
	doGit = raw_input("Would you like to git init this new project to begin tracking code changes? (y|n): ")
	addRemote = 'cd %s/projects/%s && git git remote add origin %s' % (homeDirectory, projectName, remoteRepo)

	if doGit == "y":
		os.system(initRepo)
	elif doGit == "n":
		print("Did NOT git init the new project.")
		return;
	else:
		print("Oops, this is a yes or no question. Please enter y or n.")

	# HTTPS or SSH git clone works. In the future when using the GitHub API, I have gotten https via api access token working, will need to review SSH settings to see if it's possible.
	remoteRepo = raw_input("Do you have a remote repository to add a url for? (y|n): ")
	if remoteRepo == "y":
		os.system(addRemote)
	elif remoteRepo == "n":
		print ("No remote repository added to new repository.")
		return;
	else:
		print("Oops, this is a yes or no question. Please enter y or n.")

	return;

# Made a little different structure for php applications. This function will take projectType, homeDirectory, and projectName to create a new project directory.
def makeProj( projectType, homeDirectory, projectName ):
	isPhp = raw_input("Is this a php application? (y|n): ")
	if isPhp == "y":
		projectType = "php"
	elif isPhp == "n":
		projectType = "mainTemplate"
	else:
		print("Please enter y for yes if this is a PHP application, or n for no if it is another language.")

	makeProj = 'cp -R /resources/templates/%s %s/projects/%s' % (projectType, homeDirectory, projectName)
	cdProj = 'cd %s/projects/%s' % (homeDirectory, projectName)
	chMod = 'chmod 755 %s/projects/%s/src/* && chmod 755 %s/projects/%s/bin/*' % (homeDirectory, projectName)
	ttabProj = 'ttab cd %s/projects/%s/' % (homeDirectory, projectName)
	openAtom = 'atom %s/projects/%s/' % (homeDirectory, projectName)

	os.system(makeProj)
	os.system(cdProj)
	os.system(chMod)
	openProj = raw_input("Open the new project directory and Atom text editor? (y|n): ")
	if openProj == "y":
		os.system(ttabProj)
		os.system(openAtom)
	elif openProj == "n":
		print('Project folder created at %s/projects/%s/' % (homeDirectory, projectName))
	else:
		print("Y or n, only, please.")

	return;




#############################################################
# Section 4: Main Body
#############################################################

projectLanguage = raw_input("Enter the language of your new project: ")
projectName = raw_input("Enter the name of your new project: ")


makeproj( projectType = '%s', homeDirectory = '%s', projectName = '%s' % (projectType, homeDirectory, projectName) )
gitInit()

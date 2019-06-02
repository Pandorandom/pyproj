#!/usr/bin/env python
#
#
#
# TOOL NAME: Pyproj
# WRITTEN BY: tacree
# DATE: 05-28-2019
# REV:
# First Worked: 05-28-2019
# Purpose: The purpose of this script is to offer a project creator application written in python over the original tool (bash). Current set up is to have everything created to ~/projects/..

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
# BY: tacree
# DATE: 06-02-2019
# CHANGES MADE: Added license template files containing all the licenses supported via GitHub as of today.
# Adding in a prompt for a license to be generated as well. Several of the licenses available
# allow you to put in the year and your user/professional name. Going to do some find/replace
# the dates and usernames.
#
#
#

#############################################################
# Section 1: Imports
#############################################################
# Going to run command line args to create folders and such. Getpass will allow sudo/password entry to be protected, time in case there's any sleep timers necessary, and sys/socket for system info.
import os, getpass, time, socket, sys
#from github import Github
#from Tkinter import *
from os import system, name




#############################################################
# Section 2: Misc. Variables
#############################################################
# get system username
username = getpass.getuser()

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
def gitInit(homeDirectory, projectName):
	initRepo = 'cd %s/projects/%s && git init' % (homeDirectory, projectName)
	doGit = raw_input("Would you like to git init this new project to begin tracking code changes? (y|n): ")

	if doGit == "y":
		os.system(initRepo)
	elif doGit == "n":
		print("Did NOT git init the new project.")
		cd2Proj = raw_input("Would you like to switch to the new project directory? (y|n): ")
		if cd2Proj == "y":
			os.system('ttab cd %s/projects/%s/' % (homeDirectory, projectName))
			sys.exit()
		elif cd2Proj =="n":
			print("Exiting pyproj creator.")
			sys.exit()
		else:
			print("Oops, this is a yes or no question. Please enter y or n.")
	else:
		print("Oops, this is a yes or no question. Please enter y or n.")

	# HTTPS or SSH git clone works. In the future when using the GitHub API, I have gotten https via api access token working, will need to review SSH settings to see how to accomplish the same task.
	remoteRepo = raw_input("Do you have a remote repository to add a url for? (y|n): ")
	if remoteRepo == "y":
		repoUrl = raw_input("Please enter the URL of the remote repository: ")
		os.system('cd %s/projects/%s && git remote add remote %s' % (homeDirectory, projectName, repoUrl))
		print("Remote repository added as 'remote'.")
		cd2Proj = raw_input("Would you like to switch to the new project directory? (y|n): ")
		if cd2Proj == "y":
			os.system('ttab cd %s/projects/%s/' % (homeDirectory, projectName))
			sys.exit()
		elif cd2Proj =="n":
			print("Exiting pyproj creator.")
			sys.exit()
		else:
			print("Oops, this is a yes or no question. Please enter y or n.")
	elif remoteRepo == "n":
		print ("No remote repository added to new repository.")
		cd2Proj = raw_input("Would you like to switch to the new project directory? (y|n): ")
		if cd2Proj == "y":
			os.system('ttab cd %s/projects/%s/' % (homeDirectory, projectName))
			os.system('exit')
		elif cd2Proj =="n":
			print("Exiting pyproj creator.")
			sys.exit()
		else:
			print("Oops, this is a yes or no question. Please enter y or n.")
	return;

# Copies template files to homeDirectory/projects/projectName, offers to open a terminal tab and atom text editor.
def makeProj():
	projectName = raw_input("Enter the name of your new project: ")
	# expands symlink of /home directory
	homeDirectory = os.path.expanduser("~")
	#Based on some research. php projects have a little different structure. A lot of other languages employ/can be adapted to a structure as included with this tool.
	isPhp = raw_input("Is this a php application? (y|n): ")
	if isPhp == "y":
		projectType = "php"
	elif isPhp == "n":
		projectType = "mainTemplate"
	else:
		print("Please enter y for yes if this is a PHP application, or n for no if it is another language.")
		return makeProj()

	currentDir = os.getcwd()

	os.system('mkdir %s/projects/%s' % (homeDirectory, projectName))
	os.system('cp -R %s/src/lib/templates/%s/ %s/projects/%s' % (currentDir, projectType, homeDirectory, projectName))
	os.system('cd %s/projects/%s && chmod 755 %s/projects/%s/src/ && chmod 755 %s/projects/%s/bin/' % (homeDirectory, projectName, homeDirectory, projectName, homeDirectory, projectName))


	licenseProj = raw_input("Would you like to initialize this project with a GitHub-supported license? (y|n)")
	if licenseProj =="y":
		licenseProj = True
		while licenseProj:
			print ("""
			1. Mozilla Public License 2.0
			2. GNU General Public License v3.0
			3. Apache License 2.0
			4. Eclipse Public License 2.0
			5. BSD 2-Clause "Simplified"
			6. BSD 3-Clause "New"
			7. GNU Affero General Public License 3.0
			8. GNU General Public License v2.0
			9. GNU Lesser General Public License v2.1
			10. GNU Lesser General Public License v3.0
			11. MIT License
			12.The Unlicense (Be careful with this one!)
			""")
			licenseProj = raw_input("Which license would you like to apply? (This can be changed later): ")
			#  Mozilla Public License 2.0
			if licenseProj == "1":
				licenseName = "MPL2.0"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	GNU General Public License v3.0
			elif licenseProj == "2":
				licenseName = "GNU_GPLv3"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	Apache License 2.0
			elif licenseProj == "3":
				licenseName = "apache2"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	Eclipse Public License 2.0
			elif licenseProj == "4":
				licenseName = "EclipsePublic2.0"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	BSD 2-Clause "Simplified"
			elif licenseProj == "5":
				licenseName = "BSD2-Clause"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	BSD 3-Clause "New"
			elif licenseProj == "6":
				licenseName = "BSD3-Clause"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	GNU Affero General Public License 3.0
			elif licenseProj == "7":
				licenseName = "GNU_Afferov3.0"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	GNU General Public License v2.0
			elif licenseProj == "8":
				licenseName = "GNU_GPLv2.0"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	GNU Lesser General Public License v2.1
			elif licenseProj == "9":
				licenseName = "GNU_LGPLv2.1"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	GNU Lesser General Public License v3.0
			elif licenseProj == "10":
				licenseName = "GNU_LGPLv3.0"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	MIT License
			elif licenseProj == "11":
				licenseName = "MIT"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			#	The Unlicense (Be careful with this one!)
			elif licenseProj == "12":
				licenseName = "Unlicense"
				os.system('cp %s/src/lib/templates/LICENSES/%s %s/projects/%s/LICENSE' % (currentDir, licenseName, homeDirectory, projectName))
				licenseProj = False

			else:
				print("Invalid option. Please review supported licenses and select a number from the list above.")
				return;

	elif licenseProj =="n":
		print("No license added to the new project.")
	else:
		print("y or n, only, please.")

	openProj = raw_input("Open the new project in Atom text editor? (y|n): ")
	if openProj == "y":
		#os.system('ttab cd %s/projects/%s/' % (homeDirectory, projectName))
		os.system('atom %s/projects/%s/' % (homeDirectory, projectName))
		gitInit(homeDirectory, projectName)
	elif openProj == "n":
		print('Project folder created at %s/projects/%s/' % (homeDirectory, projectName))
		gitInit(homeDirectory, projectName)
	else:
		print("y or n, only, please.")
	return;

	gitInit(homeDirectory, projectName)

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#############################################################
# Section 4: Main Body
#############################################################
clear()
makeProj()

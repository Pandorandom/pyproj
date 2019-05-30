# Pyproj Project Creator!

## Name your project
  * The project creator will input the name of your new project to multiple places throughout your new project's source files.

## Multiple languages supported for your new projects!
  * Current languages supported: Python, Bash/Shell, Ruby, and a web app.
  - More to come with new formats for each language to follow more prevalent style guides!

## Create a new project in a few short steps, complete with git initialization, remote repo adding, and more!
  * If you have created a remote repository to accompany the new project, you can add the URL during the creation process.
  - If no remote repository is indicated, you can still init the project folder to start tracking source code changes.

## Future Features
  + Add a config file where user can set their preferred text editor, terminal application, bash profile location, GitHub username and tokens for API work, etc.
  * Utilize Tkinter to create a gui application with checkboxes and text boxes to accomplish the same tasks graphically.
  - Implement below file structure, research more templates for other languages as needed.
    * Potential File structure for the new project templates:
	 	```
	 	├── .gitignore
	 	├── .npmignore
	 	├── LICENSE
	 	├── README.md
	 	├── bin
	 	│   ├── script1
	 	│   └── script2
	 	├── docs
	 	├── etc
	 	│   └── user.cfg
	 	├── requirements.txt
	 	└── src
		│   ├── lib
		│      ├── templates
		│      ├── ...various library files...
		│	├── projectName.projectType
		│	├── ...other source code...
		```
    * Potential File structure for php:
  	 	```
  	 	├── .gitignore
  	 	├── .npmignore
  	 	├── LICENSE
  	 	├── README.md
  	 	├── public_html
  	 	│   ├── css
  	 	│   └── img
		│     ├── content
		│     ├── layout
		│   ├── js
  	 	├── docs
  	 	├── resources
  	 	│   ├── config.php
  	 	│   ├── user.cfg
		│   ├── library
  		│   ├── templates
  	 	├── requirements.txt
  		```
    - I'd like to further template-ize each supported language by getting the comments, shebangs (if necessary) and various other housekeeping tasks and add them to a language-specific template, housed in: src/lib/templates.
	 + Get all licenses on GitHub and offer License creation through the tool.

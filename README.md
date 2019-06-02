# Pyproj - Project Creator!

## Create a new project, git init, add remote, open terminal and Atom (currently) all with one tool!
  * The Pyproj tool's purpose is to assist with creating new small-medium scale projects with an existing source code/file structure, with open-source licensing, file/folder creation, git initialization and more.
  - Evolution: Over time, different IDEs/text editors, terminal applications, GitHub API integration, GUI to accomplish the command-line tasks.

## Standard template for project structure, with more to come.
  * There's never one perfect approach to something. Same goes for the project structure I've created with this project. Over time I'd like to include different structures as recommended/I come across.

## Create a new project in a few short steps, complete with git initialization, remote repo adding, and more!
  * If you have created a remote repository to accompany the new project, you can add the URL during the creation process.
  - If no remote repository is indicated, you can still init the project folder to start tracking source code changes.

  ## Structure your project for transferability
    * File structure for new projects:
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
  	 │      ├── ...various library files...
  	 │      ├── projectName.projectType
  	 │      ├── ...other source code...
  	 ```
    * File structure for php-based projects:
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

## Future Features
  + Add a config file where user can set their preferred text editor, terminal application, bash profile location, GitHub username and tokens for API work, etc.
  * Utilize Tkinter to create a gui application with checkboxes and text boxes to accomplish the same tasks graphically.
  - I'd like to further template-ize each supported language by getting the comments, shebangs (if necessary) and various other housekeeping tasks and add them to a language-specific template, housed in: src/lib/templates.

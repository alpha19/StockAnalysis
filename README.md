# Overview
Basic goals are twofold:
1. Work on Python programming skills
2. Design an infrastructure that can peridocially track and analyze stocks that are of interest to the user
3. Create an interface that can display stocks to a user
Right now, the source code is pretty simple. It provides a mechanism through which a user can setup a recurring task that will update one's tracked stocks, as well as a simple GUI for displaying, adding, and removing tracked stock. 
# Components
# Setup Windows Development Environment
1. Install PyCharm Community Edition
# Setup MacOS Development Environment
# Dependencies 
Recommended IDE - Pycharm Community Edition
Python3 (3.4 is what I use)
# Deficiencies
The overall stock database is local to the user and is tracked by the repository. The hope is to stop tracking the database - instead providing a template db in this repo - in the short term.
Longer term goal include actually deploying a server to host the db, task initiation (analysis and updates), and web server backend.

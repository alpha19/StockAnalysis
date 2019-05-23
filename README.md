# Overview
Basic goals are twofold:
1. Work on Python programming skills
2. Design an infrastructure that can periodically track and analyze stocks that are of interest to the user
3. Create an interface that can display stocks to a user
Right now, the source code is pretty simple. It provides a mechanism through which a user can setup a recurring task that will update one's tracked stocks, as well as a simple GUI for displaying, adding, and removing tracked stock. 
# Components
There are two main components to the Stock Analysis project so far:
1. GUI              - Displays list of tracked stocks and allows users to add or remove stocks from list of tracked stocks.
2. Update Service   - Updates list of currently tracked stocks (stored in a local SQLite database) with up to date information and sends email (to be deprecated)
3. Web Interface    - This is currently WIP. But the long-term goal is for the GUI to be deprecated in favor of a web service (developed with Django)
The expectation is for the GUI to be deployed and run by whoever; the update service should really only be run by the server backend. However, since this is just a pet project that isn't really worked on all that much, anyone should feel free to run the update service.
# Setup Development Environment
1. Install PyCharm Community Edition
> https://www.jetbrains.com/pycharm-edu/download/
2. Install Python (>=v3.4)
> https://www.python.org/downloads/release
3. Clone this repository locally (i.e. git clone)
4. Open Stock Analysis Project via PyCharm
5. Download package dependencies through PyCharm (see list of dependencies below). Steps are as follows:
    1. In PyCharm menu bar select **File->Settings**
    2. In Settings window, navigate to **Project: StockAnalysis**
    3. Select **Project Interpreter**, then select **+** button to add a dependency
    4. Search desired dependency (e.g. PyQt5) then select **Install**
### Running the GUI ##
Once the above steps are completed, a user should just have to run **gui_main.py** to show the GUI.
### Running the Update Service ###
Additional steps are required to run the update service due to the email functionality that is currently part of the update stock flow. This will be deprecated but it is how things work at the moment. A user wanting to setup the update service can do one of two things (the latter option is more involved):
1. Comment out all references to emails in cron_main.py
2. Set up the files and encryption needed to send an email.
To setup your system for sending emails through the update service, do the following to encrypt the email credentials of the account that will be sending emails:
1. Create a text file with email user in the first line, and the email password in the second line
2. Create SSH keys with ssh-keygen
> https://confluence.atlassian.com/bitbucketserver054/creating-ssh-keys-939508421.html
3. Encrypt the text file. The encrypted file should be save in the home directory under the name **stock_email_credentials_encrypt.txt**. To encrypt:
    1. cd ~/.ssh 
    2. openssl rsa -in id_rsa -pubout -outform pem > id_rsa.pub.pem
    3. openssl rsautl -encrypt -inkey id_rsa.pub.pem -pubin -in EMAIL_CREDENTIALS.txt -out ~/stock_email_credentials_encrypt.txt
To run the update service, a user can then run **cron_main.py**
### Dependencies ###
Recommended IDE - Pycharm Community Edition
Python3 (3.7 is what I use). Newer versions should work too.
#### Python Virtual Environment ####
It's recommended to use a python virtual environment to isolate the dependencies for the project from your system's python install (among other reasons). A good link describing virtual environments is here:
> https://docs.python-guide.org/dev/virtualenvs/
To set up a virtual environment perform the following steps:
1. Install virtualenv with pip
> pip install virtaulenv
2. Install virtualenvwrapper
> pip install virtualenvwrapper
3. For Windows users, also install virtualenvwrapper-win
> pip install virtualenvwrapper-win
4. Create the python virtual environment. You can call it whatever you want, but I am calling it **venv_stock_analysis**
> mkvirtualenv venv_stock_analysis
 You should now have a virtual environment setup for your project. In a bash terminal or command prompt, you can send the following command to start using the virtual envrionment.
> workon venv_stock_analysis
In PyCharm you will need to change the default python interpreter to the virtual environment interpreter we just created.
1. In PyCharm menu bar select **File->Settings**
2. In Settings window, navigate to **Project: StockAnalysis**
3. Select **Project Interpreter**, then select the dropdown next to the project interpreter row.
4. Select **Show All...**, then select **+** button to add a new python interpreter (e.g. the virtual interpreter)
    1. Navigate to the base directory of the virtual environment:
        1. On Windows, %USERPROFILE%\Envs\**NAME_OF_VIRTUAL_ENV**\Scripts\python.exe
        2. On Linux, ~/Envs/**NAME_OF_VIRTUAL_ENV**\Scripts\python
Once all these steps are complete your project should now point to the virtual environment in PyCharm.
 **NOTE: None of this is required - however, it can be helpful**
#### Python Packages ####
* PyQt5
* requests
* cryptography
* django
# Deficiencies
The overall stock database is local to the user and is tracked by the repository. The hope is to stop tracking the database - instead providing a template db in this repo - in the short term.
Longer term goal include actually deploying a server to host the db, task initiation (analysis and updates), and web server backend.

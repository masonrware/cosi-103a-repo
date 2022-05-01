    

CPA2
===

COSI 103A -- Brandeis University
================================

##### Professor Timothy J. Hickey

###### Date: 05/01/22

* * *

### Description

Portfol.io is a web portal to host and display any github repositories that you want to highlight and give thier own space. Simply by entering the name of a user and a repo name, portfol.io will generate a list of relevant repos that you can display to the front end.

### How Does It Work?

This app is written using the Embedded JS framework for JavaScript (EJS). The backend is serviced in nodeJS. You can find all rendered, front-end files located in `views`, all schema for persisting data in `models`, and the heart of the app in `app.js`.

* `app.js`

Within App.js, you will find commented sections of code. Most are labeled, aside from the section of gets and posts that I wrote to handle routing. These are clearly separated from the rest of the diagnostic code above and below it.

### How To Use Portfol.io

Interacting with Portfol.io is very straightforward. There are three main functionalities:

1. Searching for a repo by name
2. Addin a repo to your portfolio
3. Following a repo's card to the github page

When one first vists the `/` route of the page, after logging in via the prompt, they will see the following:

![home page](/public/index.png "Index")

Then, they can use the text boxes at the bottom of the page to add some information about a project they wish to add.

Once they add a project, for example this repo, it will appear in the list along with a github card for the project - if it exists:

### Dependencies

1. "axios": "^0.26.1",
2. "bcrypt": "^5.0.1",
3. "connect-flash": "^0.1.1",
4. "connect-mongo": "^4.6.0",
5. "connect-mongodb-session": "^3.1.1", 
6. "cookie-parser": "~1.4.4",
7. "debug": "~2.6.9",
8. "ejs": "^3.1.7",
9. "express": "~4.16.1",
10. "express-ejs-layouts": "^2.5.1",
11. "express-session": "^1.16.2",
12. "http-errors": "~1.6.3",
13. "mongoose": "^5.9.21",
14. "nodemon": "^2.0.15"

All dependencies can be found in the `package.json` file. Moreover, they can be automatically installed using the shell command: `npm install`.


* * *

Build & Run
-----------

### Downloading a Local Copy

To download a local copy, visit the github page located at (https://github.com/masonrware/cosi-103a-repo) and navigate to the dropdown in the upper right and click the *Download Zip* button. :

![download button](/public/github.png "Download")

Alternatively, you can run this command to obtain a local copy of the repo and its branches: `git clone https://github.com/masonrware/cosi-103a-repo.git portfol.io/`

NOTE: the app for cpa2 is located, by itself, on the branch **mrw_heroku**. Any other branches are for unrelated, outdated, or private work. 

### Build Instructions

There are no substantial build instructions to run this app locally. Should all dependencies be installed, then the run command is all you need.

If you have not yet installed dependcies, see the section on dependencies above or just run the command `npm install`.

### Run Instructions

In order to run the app in your browser locally, enter the command: `npm start`. This will start the Flask app at your localhost on port 15000, if it is free.

* * *

_© 2022 MASON WARE_
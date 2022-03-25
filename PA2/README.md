_Written By: Mason Ware_

PA2
===

COSI 103A -- Brandeis University
================================
Group 20: Ben B., Kevin B., Kayla H., Jason G., Mason W.

##### Professor Timothy J. Hickey

###### Date: 03/24/22

* * *

### Description

This PA manages a local database implemented in sequel via a console-based interface scripted in python. There are a number of commands accessible from within the console as well as a testing suite and a log of a successful interaction with the program located within the root directory.

The following are major additional methods and classes:

* `tracker.py`

Within the file tracker.py, the functionalities for commands 4-11 were added from lines 88 to 133. Within each, respective user interaction is performed if necessary and then manipulation of data within the database.

* `transactions.py`

The class for transactions `Transaction` was implemented in this file as well as specialized helper functions based off of the given functions from the skeleton. The methods added are `select_date`, `select_month`, `select_year`, and `select_category`. These all use variations of sql manipulation commands within python code to selectively filter the data in the database.


### Dependencies

1.  `pytest==7.1.1`

All dependencies can be found in the `./requirements.txt` file. Moreover, they can be automatically installed using the shell command: `pip install -r requirements.txt` and the most up to date versions of the dependencies can be installed using the shell command: `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U` .

  

* * *

Build & Run
-----------

### Build Instructions

There is no substantial build requirement as the database is low-form and locally held within the project's directory. One can however run `pylint` and `pytest` commands to evaluate the performace of the python code.

### Run Instructions

In order to run the program and simultaneously build a fresh database/interact with the persisting database you have been using, run the command: `$ python3 tracker.py` in the console. This will print the command list and the rest is self-explanatory.

* * *

### Testing

The testing of this program is done in two files: `test_transactions.py` and `test_category.py`. These files test the functionality of the data representations that fill the data points added to the database via the user commands. All other functionality of the program is printing or semantic in that it simply interacts with methods of the already tested classes. 

One can test the program simply by running the command: `$ pytest` in the console while in the root directory of the program.

A successul test output should look like this:
(base) <device>:<dir> <user>$ pytest
========================================================================================== test session starts ==========================================================================================
platform darwin -- Python 3, pytest-7.1.1, pluggy-1.0.0
rootdir: <route>, configfile: pytest.ini
plugins: anyio-3.4.0
collected 12 items                                                                                                                                                                                      

test_category.py ....                                                                                                                                                                             [ 33%]
test_transactions.py ........                                                                                                                                                                     [100%]

Additionally, one can run the command `$ pylint <filename>` to get the syntax score of the given script.


_© 2022 MASON WARE & GROUP 20_
_Written By: Mason Ware_

PA2
===

COSI 103A -- Brandeis University
================================

##### Professor Timothy J. Hickey

###### Date: 03/24/22

* * *

### Description

This program is a search engine that uses Washington Post articles stored in `pa4_data/wapo_pa4.jl`. Utilizing a Flask backend, the engine takes a user query, normalizes, stems, and tokenizes the text and then compares the set of words against an inverted index. Before the application can be deployable and runnable, a database containing collections of documents and the inverted index itself must be made in order for the user to be able to continually search. The program does this with the `--build` option command. 

Once that command is run, the program will construct an inverted index with keys of every stemmed and normalized term in the corpora and values of lists
of tuples of every document that term appears in and the tf of that term in the document. This will be inserted into a local db under the alias vs_index
alongside another index titled doc_length_index. This collection, as can probably be deduced, has keys of doc ids and values of cosine-normalized lengths of each document.


  

### Dependencies

1.  `Flask==2.0.2`
2.  `pymongo`
3.  `nltk==3.5`

All dependencies can be found in the `./requirements.txt` file. Moreover, they can be automatically installed using the shell command: `pip install -r requirements.txt` and the most up to date versions of the dependencies can be installed using the shell command: `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U` .

  

* * *

Build & Run
-----------

### Build Instructions

In order to build the database collections with the data contained in `pa4_data/wapo_pa4.jl`, one must navigate to the root directory of this project and run the command: `python3 hw4.py --build`. This will create an inverted index. Once that is finished, you can move onto running the program and deploying the Flask application.

### Run Instructions

In order to run the app in your browser locally, enter the command: `python3 hw4.py --run`. This will start the Flask app at your localhost on port 5000, if it is free, in debug mode.

* * *

### Testing

To test this program, I wrote unit tests for each major class and utility in the program aside from the database methods (as I am not sure how to test the pymongo methods). These tests are stored in the file: `test_hw3.py` and can be run from the terminal using the command: `python3 test_hw3.py`. This will prompt the test suite to run, running 7 total tests in multiple `unittest.TestCase` instances. If any fail, they will be conveniently displayed in the terminal with the initial exact difference marked. For example, if one were to change the assertion statement on line `32` of the file to this: `self.assertDictEqual(invidx.appearances_dict, {'bodi': [1], 'titl': [1], 'sampl': [2]}, message)`, and ran the test suites, one would get the following response from the tests:  
`$ python3 test_hw3.py   ..F....   ======================================================================   FAIL: test_index_document (__main__.TestInvertedIndex)   A document is indexed into the appearances dictionary correctly.   ----------------------------------------------------------------------   Traceback (most recent call last):   File "test_hw3.py", line 32, in test_index_document   self.assertDictEqual(invidx.appearances_dict, {'bodi': [1], 'titl': [1], 'sampl': [2]}, message)   AssertionError: {'titl': [1], 'bodi': [1], 'sampl': [1]} != {'bodi': [1], 'titl': [1], 'sampl': [2]}   - {'bodi': [1], 'sampl': [1], 'titl': [1]}   ? ^      + {'bodi': [1], 'sampl': [2], 'titl': [1]}   ? ^   : Inverted Index DS does not load appearances dict correctly      ----------------------------------------------------------------------   Ran 7 tests in 0.023s      FAILED (failures=1)   `

However, the above test suite is for a programmer who is only interested in the functionality of certain facets of the application. For everyone else, running the test suite and app all in one with a test set of documents is a preferable solution. In order to do this, the initial run command should be changed to match the following command: `python3 hw3.py --test`. Lastly, running the program in test mode will incorperate the customized text processor instead of the provided text processor that is used in the production deployment of the app. 

_© 2022 MASON WARE & GROUP 20_
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="PA1ReadMe">
        <meta name="keywords" content="ReadMe">
        <meta name="author" content="Mason Ware">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style='font-family:Arial, Helvetica, sans-serif'>
        <h1 style='border: 0; padding: 0; margin: 0;'>PA2</h1>
        <h1 style='border: 0; padding: 0; margin: 0'>COSI 132A -- Brandeis University</h1>
        <h4>Group 20</h4>
        <h5>Professor Timothy J. Hickey</h5>
        <h6>Date: 02/13/22</h6>
        <hr>
        <div id='description'>
            <h3>Description</h3>
            <p id='gen description'>
                This app parses and extracts JSON data about Brandeis University's Class Offerings from 2020-2021. 
                It does so by.....elaboration inbound...
            </p>
        </div>
        <br>
        <div id='Dependencies'>
            <h3>Dependencies</h3>
            <ol id='Dependencies List'>
                <li><code>Flask==2.0.2</code></li>
            </ol>
            <small>All dependencies can be found in the <code>./requirements.txt</code> file. Moreover, they can be automatically installed
            using the shell command: <code>pip install -r requirements.txt</code> and the most up to date versions of the dependencies can be installed using 
            the shell command: <code>pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
            </code>.</small>
        </div>
        <br>
        <hr>
        <div id='build and run'>
            <h2>Build & Run</h2>
            <div id='Build Instructions'>
                <h3>Build Instrcutions</h3>
                <p>In order to build the platform to interact with it and search for course info, the flask app needs to be locally
                hosted. After making sure all dependecies are installed, using the aforementioned <code>pip install -r requirements.txt</code> command, you can run the app via the terminal using the <code>python3 app.py</code> command (making sure you're in the root directory of this project). That's it, navigate to the local host window in your prefered browser and access port 2400, proceed to run instructions.</p> 
            </div>
            <div id ='Run Instrcutions'>
                <h3>Run Instrcutions</h3>
                <p>Now that the app is up and running locally and you are viewing its home page in the browser, you can interact with it. To get started enter help or h into the command field. That's it, follow the on-screen instructions and you're all set.</p>
            </div>
        </div>
        <hr>
        <div id='Testing'>
            <h3>Testing</h3>
            <p>...elaboration inbound...</p>
        </div>
    </body>
</html>
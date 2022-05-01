/*
  app.js -- This creates an Express webserver with login/register/logout authentication
*/

// *********************************************************** //
//  Loading packages to support the server
// *********************************************************** //
// First we load in all of the packages we need for the server...
const createError = require("http-errors"); // to handle the server errors
const express = require("express");
const path = require("path");  // to refer to local paths
const cookieParser = require("cookie-parser"); // to handle cookies
const session = require("express-session"); // to handle sessions using cookies
const debug = require("debug")("personalapp:server"); 
const layouts = require("express-ejs-layouts");
const axios = require("axios")
var MongoDBStore = require('connect-mongodb-session')(session);


// *********************************************************** //
//  Loading models
// *********************************************************** //
const ToDoItem = require("./models/ToDoItem")
const Project = require('./models/project')
// *********************************************************** //
//  Loading JSON datasets
// *********************************************************** //
//const courses = require('./public/data/courses21-22.json')
// const courses2021 = require('./public/data/courses20-21.json')
// const courses2122 = require('./public/data/courses21-22.json')
// const courses = courses2122

// *********************************************************** //
//  Connecting to the database 
// *********************************************************** //

const mongoose = require( 'mongoose' );

// const mongodb_URI = process.env.mongodb_URI
//const mongodb_URI = 'mongodb://localhost:27017/cs103a_todo'
const mongodb_URI = 'mongodb+srv://cs_sj:BrandeisSpr22@cluster0.kgugl.mongodb.net/Jason_Gordon?retryWrites=true&w=majority'

mongoose.connect( mongodb_URI, { useNewUrlParser: true, useUnifiedTopology: true } );
// fix deprecation warnings
// mongoose.set('useFindAndModify', false); 
// mongoose.set('useCreateIndex', true);

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {console.log("we are connected!!!")});

// *********************************************************** //
// Initializing the Express server 
// This code is run once when the app is started and it creates
// a server that respond to requests by sending responses
// *********************************************************** //
const app = express();

// Here we specify that we will be using EJS as our view engine
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");



// this allows us to use page layout for the views 
// so we don't have to repeat the headers and footers on every page ...
// the layout is in views/layout.ejs
app.use(layouts);

// Here we process the requests so they are easy to handle
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

// Here we specify that static files will be in the public folder
app.use(express.static(path.join(__dirname, "public")));

// Here we enable session handling using cookies
app.use(
  session({
    secret: "zzbbyanana789sdfa8f9ds8f90ds87f8d9s789fds", // this ought to be hidden in process.env.SECRET
    resave: false,
    saveUninitialized: false
  })
);

// *********************************************************** //
//  Defining the routes the Express server will respond to
// *********************************************************** //


// here is the code which handles all /login /signin /logout routes
const auth = require('./routes/auth');
const { deflateSync } = require("zlib");
app.use(auth)

// middleware to test is the user is logged in, and if not, send them to the login page
const isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  }
  else res.redirect('/login')
}

app.get("/about", (req, res, next) => {
  res.render("about");
});

//////////////////////////////////////////////////
//////////////////////////////////////////////////
// Below Written By: Mason Ware
// 4/30/22 
//////////////////////////////////////////////////
//////////////////////////////////////////////////

app.get("/",
  isLoggedIn,
  async (req,res,next) => {
    try{
      let userId = res.locals.user._id;  // get the user's id
      let items = await Project.find({userId:userId}); // lookup the user's todo items
      res.locals.items = items;
      res.render("portfolio");  // render to the toDo page
    } catch (e){
      next(e);
    }
  }
);

app.post('/portfolio/find',
isLoggedIn,
async (req,res,next) => {
  try{
    const title = req.body.find_title;
    const userId = res.locals.user._id;
    let items = await Project.find({title:title});
    res.locals.items = items;
    res.render("portfolio");
  } catch (e){
    next(e);
  }
}
)


app.get('/portfolio',
  isLoggedIn,   // redirect to /login if user is not logged in
  async (req,res,next) => {
    try{
      let userId = res.locals.user._id;
      let items = await Project.find({userId:userId});
      res.locals.items = items;
      res.render("portfolio");
    } catch (e){
      next(e);
    }
  }
  )

  app.post('/portfolio/add',
  isLoggedIn,
  async (req,res,next) => {
    try{
      const {title,github,description} = req.body;
      const userId = res.locals.user._id;
      const finishedOn = new Date();
      let data = {title, github, description, userId, finishedOn,}
      let item = new Project(data)
      await item.save()
      res.redirect('/portfolio')
    } catch (e){
      next(e);
    }
  }
  )

  app.get("/portfolio/delete/:itemId",
    isLoggedIn,
    async (req,res,next) => {
      try{
        const itemId=req.params.itemId;
        await Project.deleteOne({_id:itemId})
        res.redirect('/portfolio')
      } catch (e){
        next(e);
      }
    }
  )

//////////////////////////////////////////////////
//////////////////////////////////////////////////

// here we catch 404 errors and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// this processes any errors generated by the previous routes
// notice that the function has four parameters which is how Express indicates it is an error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};
  // render the error page
  res.status(err.status || 500);
  res.render("error");
});


// *********************************************************** //
//  Starting up the server!
// *********************************************************** //
//Here we set the port to use between 1024 and 65535  (2^16-1)
const port = process.env.PORT || "15000";
console.log('connecting on port '+port)

app.set("port", port);

// and now we startup the server listening on that port
const http = require("http");
const { reset } = require("nodemon");
const server = http.createServer(app);

server.listen(port);

function onListening() {
  var addr = server.address();
  var bind = typeof addr === "string" ? "pipe " + addr : "port " + addr.port;
  debug("Listening on " + bind);
}

function onError(error) {
  if (error.syscall !== "listen") {
    throw error;
  }

  var bind = typeof port === "string" ? "Pipe " + port : "Port " + port;

  // handle specific listen errors with friendly messages
  switch (error.code) {
    case "EACCES":
      console.error(bind + " requires elevated privileges");
      process.exit(1);
      break;
    case "EADDRINUSE":
      console.error(bind + " is already in use");
      process.exit(1);
      break;
    default:
      throw error;
  }
}

server.on("error", onError);

server.on("listening", onListening);

module.exports = app;
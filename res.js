app.get("/simpleform",
  (req,res,next) => {
    res.render("simpleform")
  }
)

app.post("/simpleform",
  (req,res,next) => {
    const {username,age} = req.body;
    res.locals.username=username;
    res.locals.age=age;
    res.render("simpleresponse")
  }
)

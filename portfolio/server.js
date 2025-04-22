const express = require('express');
const app = express();

app.set("view engine", "ejs");

app.get("/",(req, res)=>{
    res.render("index" , {
        title: "Home",
        description: "Welcome to the home page"
    });
})
app.listen(3000);

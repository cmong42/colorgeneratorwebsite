//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const { dirname } = require("path");
const spawn = require("child_process").spawn;

const app = express();
app.listen("3000")

let returnedData = []

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/", function(req, res){
    res.sendFile(__dirname+"/views/index.html")
})

app.post("/result", function (req, res){
    console.log(req.body.avatar)
    arg1 = req.body.avatar
    const pythonProcess = spawn('python3',["./colorGenerator.py", arg1])

    pythonProcess.stdout.on('data', (data) => {
    // Do something with the data returned from python script
    returnedData = data.toString().split(", ")
    console.log(arg1)
    res.render(__dirname+"/views/result.ejs", {color: returnedData, picture: arg1})
   });
})
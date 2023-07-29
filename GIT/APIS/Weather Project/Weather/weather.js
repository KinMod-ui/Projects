const express = require('express');
const https = require ('https');
const parser = require('body-parser')

const app = express();
app.use(parser.urlencoded({extended:true}))



const unit = "metric"



var link2=  "http://openweathermap.org/img/wn/10d@2x.png"

app.get("/" , function(req , res){

    

    res.sendFile(__dirname + "/index.html")

})


app.post("/" , function (req , res){
    console.log(req.body.city_name)
    console.log("Post Recieved")
    var query = req.body.city_name
    var link = "https://api.openweathermap.org/data/2.5/weather?q=" + query + "&appid=" + appId + "&units=" + unit 
    https.get(link , function(response){
        // console.log(response);

        response.on("data" , function(data){
            var weather = JSON.parse(data)
            const temp = weather.main.temp
            const desc = weather.weather[0].description
            const icon = weather.weather[0].icon
            var name = weather.name
            const imageURL = "http://openweathermap.org/img/wn/" + icon + "@2x.png"
            console.log(temp)
            console.log(desc);
            res.type('text/html')
            res.write("<h1>Welcome to " + name +"</h1>")
            res.write("<h2>The temperature is " + temp + " degrees celsius </h2>\n");
            // res.write("<p>The weather is currently " + desc + "<p>");
            res.write(`<img src=${imageURL}>`)
            res.send()
        })
    })
})

app.listen(3000 , function(){
    console.log("Server is running on rute 3000")
})

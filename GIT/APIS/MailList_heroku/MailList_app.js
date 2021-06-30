const express = require('express')
const request = require ('request')
const parser = require('body-parser')
const https = require('https')
const app = express()
app.use(parser.urlencoded({extended:true}))

app.use(express.static("public"))

// app.parser({urlencoded:true})

app.get("/" , function(req , res){
    res.sendFile(__dirname + '/signup.html')
})

app.post("/" , function(req , res){
    var email = req.body.Email
    var first_name = req.body.First_Name
    var last_name = req.body.Last_Name

    var data = {
        members : [
            {
                email_address: email ,
                status: "subscribed" ,
                merge_fields: {
                    FNAME: first_name,
                    LNAME: last_name
                }
            }
        ]
    }

    var json = JSON.stringify(data);
    const url = 'https://us10.api.mailchimp.com/3.0/lists/b4e2a19991'

    const options = {
        method: "POST",
        auth: ""
    }

    const request = https.request(url , options , function(response){
        if (response.statusCode === 200){
            res.sendFile(__dirname + '/success.html')
        }
        else{
            res.sendFile(__dirname + '/failure.html')
        }

        response.on("data" , function(data){
            console.log(JSON.parse(data))
        })
    })

    request.write(json)
    request.end()

})

app.post('/failure' , function(req,res){
    res.redirect("/")
})


app.listen(process.env.PORT || 3000 , function(){
    console.log("Server is running")
})

// const api_key = "c02a69c66fefdd063c66a71ac1e13de4-us10"

// 

// {"name":"Freddie'\''s Favorite Hats","contact":{"company":"Mailchimp","address1":"675 Ponce De Leon Ave NE","address2":"Suite 5000","city":"Atlanta","state":"GA","zip":"30308","country":"US","phone":""},"permission_reminder":"You'\''re receiving this email because you signed up for updates about Freddie'\''s newest hats.","campaign_defaults":{"from_name":"Freddie","from_email":"freddie@freddiehats.com","subject":"","language":"en"},"email_type_option":true}

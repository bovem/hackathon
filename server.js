const express = require('express')
const app = express()
const Users = require('./db').Users
const spawn = require("child_process").spawn;

const bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({extended: true}))

app.use(bodyParser.json({limit:'11mb'}))

app.get('/',(req,res)=>{
    res.send('Server started');
})


app.post('/login',(req,res)=>{
    
        Users.findOne({
            where:{
                id: req.body.pass
            }
        }).then((user)=>{
            if(!user)
            {
                return res.send('No such user');
            }
            console.log('users found');
            
            var aId = user.aadharId;
            let filePath = './data/'+req.body.pass;
            console.log(filePath)
            
            const pythonProcess = spawn('python3',['decrypt_n_save.py', aId]);
            pythonProcess.stdout.on('data', function(data) {
                res.send(data);
            } )
        })
    
})

const host = '0.0.0.0'

app.listen(process.env.PORT||8080,host,()=>{
    console.log("server started at port 8080");
})
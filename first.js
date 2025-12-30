import fs from 'fs'

fs.appendFile('first.txt',"hello how are you? what is your name", (err)=>{
    if(err){
        console.log(err)
    }   
})
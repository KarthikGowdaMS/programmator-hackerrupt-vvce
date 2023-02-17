const data = require('../routes/Drugs.json');

for (let i in data){
    if((data[i].toLowerCase()).includes("clostebol".toLowerCase())>0)
    {
        console.log(data[i]);
        // break;
    }
}
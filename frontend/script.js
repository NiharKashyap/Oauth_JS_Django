// function httpGet() {
//     try{
//         theUrl = "https://127.0.0.1:8000/login/google"
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.open( "GET", theUrl, true ); // false for synchronous request
//     // xmlHttp.send( null );
//     console.log(xmlHttp.responseText)
//     return xmlHttp.responseText;
// }catch(err){
//     console.log(err);
// }
// }
const express = require("express");
const path = require("path")
const app = express();
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);
const port = 3000;
const cors = require("cors");
const { default: axios } = require("axios");
app.use(cors({origin: "*"})
);

app.get('/', (req,res)=>{
res.sendFile(path.join(__dirname+"/home.html"));
})

app.get("/getdata", async(req,res)=>{
    await axios.get("https://127.0.0.1:8000/login/google").then((re)=>{
        console.log(re);
        res.end(JSON.stringify(re));
    }).catch((er)=>{
        console.log(er);
    res.end(JSON.stringify(er));

    });
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
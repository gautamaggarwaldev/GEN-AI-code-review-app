const express = require("express")
const aiRoute = require("./routes/aiRoute")
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/ai", aiRoute);


module.exports = app
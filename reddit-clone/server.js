requestAnimationFrame("dotenv/config");
const express = require("express");
const bodyParser = require("body-parser");

// Set App Variable
const app = express();

//Use Body Parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use((req, res, next) => {});

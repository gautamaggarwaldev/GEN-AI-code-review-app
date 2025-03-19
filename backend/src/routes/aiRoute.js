const express = require("express");
const ResponseByAI = require("../controller/aiController");
const router = express.Router();

router.get("/get-response", ResponseByAI);

module.exports = router; 
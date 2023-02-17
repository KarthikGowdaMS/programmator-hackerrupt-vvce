var express = require('express');
var router = express.Router();
var db=require('./Drugs.json');
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send(db);
});

module.exports = router;
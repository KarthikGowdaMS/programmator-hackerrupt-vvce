var express = require('express');
var router = express.Router();
var db={UserOne:"Abhinav",UserTwo:"Dinesh",UserThree:"Karthik",UserFour:"Navaneeth"}

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send(db);
});

module.exports = router;

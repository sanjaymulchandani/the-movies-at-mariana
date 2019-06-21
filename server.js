const express = require('express');
const app = express();
const path = (process.env.CUSTOM_STATICS_PATH || 'movies');

app.get('/*', function (req, res, next) {
    res.status(200);
    res.sendFile(__dirname + '/' + path + '/index.json');
  });

const port = (process.env.PORT || 3000);
app.listen(port, function () {
  console.log('Example app listening on port ' + port + '!');
});
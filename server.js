var http = require('http');

console.log('here');
//create a server object:
var portnumber = process.env.PORT || 8080;
http.createServer(function (req, res) {
	console.log('here');
  res.write('Hello World!'); //write a response to the client
  res.end(); //end the response
}).listen(8080); //the server object listens on port 8080 
var http = require('http');
var Docker = require('dockerode');
var docker = new Docker();


console.log('here');
//create a server object:
var portnumber = process.env.PORT || 8080;
http.createServer(function (req, res) {
	console.log('here');
	docker.createContainer({Image: 'sandbox', Cmd: ['python', 'progpy.py'], name: 'ubuntu-test'}, function (err, container) {
	  container.start(function (err, data) {
	    //...
	    console.log(data);
	  });
	});
  res.write(data); //write a response to the client
  res.end(); //end the response
}).listen(81, 'localhost'); //the server object listens on port 8080 
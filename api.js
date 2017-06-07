var Docker = require('dockerode');
var docker = new Docker();
docker.createContainer({Image: 'sandbox', Cmd: ['/bin/bash'], name: 'ubuntu-test'}, function (err, container) {
  container.start(function (err, data) {
    //...
  });
});
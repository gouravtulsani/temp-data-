var http = require('http');
var dt = require('./myfirstmodule');

http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write("The date and time are currently: " + dt.myDateTime() + '\n');
    response.write(request.url);
    response.end();
}).listen(8080);
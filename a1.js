// app1.js
const http = require('http');
const port = 3003;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello from Worker3!\n');
});

server.listen(port, () => {
  console.log(`App 3 is running on port ${port}`);
});


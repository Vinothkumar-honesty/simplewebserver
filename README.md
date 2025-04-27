# EX01 Developing a Simple Webserver
## Date:15.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
 <!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <table>
        <thead>
            <tr>
                <th>Layer</th>
                <th>Protocols</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Application Layer</td>
                <td>HTTP, FTP, SMTP, DNS, Telnet</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>IP, ICMP, IGMP, ARP</td>
            </tr>
            <tr>
                <td>Network Access Layer</td>
                <td>Ethernet, PPP, Frame Relay</td>
            </tr>
        </tbody>
    </table>
</body>
</html>

"""
class myhandle(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request recived")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd= HTTPServer(server_address,myhandle)
print("my webserver is running...")
httpd.serve_forever()

'''



## OUTPUT:
![alt text](<Screenshot (188).png>)
![alt text](<Screenshot (176).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

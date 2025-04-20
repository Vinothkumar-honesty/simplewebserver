from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
 <!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1 {
            color: #2c3e50;
        }
        table {
            width: 60%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #2c3e50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
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
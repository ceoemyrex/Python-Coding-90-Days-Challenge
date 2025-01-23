# Project:
#Build a simple HTTP request handler in Python to fetch and display the content of a webpage.

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class WebpageRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handles GET requests."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <head><title>Webpage Fetcher</title></head>
                <body>
                    <h1>Enter a URL to fetch:</h1>
                    <form method="GET" action="/fetch">
                        <input type="text" name="url" size="50"><br>
                        <input type="submit" value="Fetch Webpage">
                    </form>
                </body>
                </html>
            """)

        elif self.path.startswith('/fetch'):
            try:
                # Extract the URL from the query string
                query_components = dict(qc.split("=") for qc in self.path.split("?")[1].split("&"))
                target_url = query_components.get('url')

                if not target_url:
                    self.send_response(400)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"<h1>Error: No URL provided.</h1>")
                    return

                if not target_url.startswith("http"): #Add http if user forgets
                    target_url = "https://" + target_url

                response = requests.get(target_url)
                response.raise_for_status()  # Check for HTTP errors

                self.send_response(200)
                self.send_header('Content-type', response.headers.get('Content-Type', 'text/html')) #Use the websites content type or default to html
                self.end_headers()

                #Important: Write the content as bytes
                self.wfile.write(response.content)

            except requests.exceptions.RequestException as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"<h1>Error fetching URL: {e}</h1>".encode())
            except Exception as e: #Catch other errors
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"<h1>An unexpected Error occurred: {e}</h1>".encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
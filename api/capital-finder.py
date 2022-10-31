from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path=self.path
    url_Component=parse.urlsplit(path)
    query=parse.parse_qsl(url_Component)
    dictionary=dict(query)
    
    if country in dictionary:
        country=dictionary[country]
        api_url="https://restcountries.com/v3.1/name/"
        r=requests.get(api_url+country)
        data=r.json
        capital=data[0]["capital"][0]
        message = f'the capital of {country} is {capital} '    

    elif capital in dictionary:
        capital=dictionary[capital]
        api_url="https://restcountries.com/v3.1/capital/"
        r=requests.get(api_url+capital)
        data=r.json
        country=data[0]["name"]["common"]
        message = f'the capital of {capital} is {country} '    

    else :
        message="please provide me with a country or a capital"
     

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return

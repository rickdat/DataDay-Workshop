from os import lseek
import pulsar, time
from pulsar.schema import *
import time
import socket
import uuid 
import random
from datetime import datetime

rand_time = lambda: float(random.randrange(0,30))+time_uuid.utctime()
now = datetime.now()
service_url = 'pulsar+ssl://pulsar-gcp-uscentral1.streaming.datastax.com:6651'
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjkyNTYwMTksImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2I0Y2M4NzgwLTg1NzQtNGQwMS1hMzkzLWE0MzU4MDcyYjhhODtaR0YwWVhOMFlYZ3RZWFJ3OzI2ZmM2YTJiMmYiLCJ0b2tlbmlkIjoiMjZmYzZhMmIyZiJ9.V_7uF1h_2W3rpCIcAhu0HhlkqDfRgqi2A76yBc5mdwHVsDqadz4BLpvcD7hZdpUP1vbbb318PrbCEdpGbxyEmNeE_opEaKh2yNUh27QELUVxU-LqcREieLjDJEmwDNQz6Sm3MDd1fmUkefjJgdxkqhE4Vf0R2npqBaAxdfgfrjAFOVPUePJswCf74M20vTMFkpqj0A7ryyslKPG_2izwpTYZwaQ-qS5mas2xDICsOdvRm4s1yyMP5P3ihmzuJa9net0p7JLnlglz0FkoqBUjUQ5z4uLcFxYW1oi2OoMLfHWBujjFtdlDzq-IojsSkCigQFpkNQFaR-YsRYS8VTjwwA"
topic = 'persistent://datastax-atp/events-namespace/events-topic'

class Events(Record):
    device_name = String() 
    date = String()
    event_id = String()
    data = String()

client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))

producer = client.create_producer(topic,schema=JsonSchema(Events))

# Function to read ubuntu system logs. Remove the "." before /var when in a real environment.
def get_logs():
    with open('./var/log/syslog', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            print(str(line.split(" ")[3]),str(datetime.strftime(now,'%Y-%m-%dT%H:%M:%S')),str(uuid.uuid4()),str(line))
            producer.send(Events(device_name = str(line.split(" ")[3]), date=str(now.isoformat()), event_id=str(uuid.uuid1()), data=str(line)))
            
# function to extract datetime from syslog message
def get_datetime(line):
    return line.split(' ')[0:3]

get_logs()

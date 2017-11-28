# Distributed-SHA256-hash-cracker
Crack SHA256 in a distributed computing environment using a dictionary wordlist.
This program works using Gearman for implementing the parallel framework. It needs a Gearman job server and Gearman Python API. 

## Client.py 
client.py [-h] [-p PORT] [-b BATCHSIZE] wordlist hash server. For example 
```
./client.py -b 10 -p 8200 wordlist hash 192.168.122.2
```

## Worker.py
worker.py [-h] [-p PORT] server. For example
```
./worker.py -p 8200 192.168.122.2
```
Server and port must correspond to the server and port used by Gearman job server.
Batchsize refers to the number of words to be sent as a job to the worker by the client. This is done until all words are sent.

# Distributed-SHA256-hash-cracker
Crack SHA256 in a distributed computing environment using dictionary.

This program works using gearman for implementing the parallel framework. It needs a Gearman job server and Gearman Python API. It runs on localhost:4370

1) Install Gearman job server using "sudo apt-get install gearman".
2) Install Python library using "sudo pip install gearman".
3) Start job server using "sudo gearmand".
4) ./worker.py on all the worker machines.
5) ./client.py -w [ location to wordlist ] -f [location of hashfile stored as text ]

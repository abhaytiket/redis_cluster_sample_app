# about
A very basic application in python flask for testing redis cluster setup. In this we are creating a web application using flask framework in python and trying to connect the application with a redis cluster of 3 nodes with 0 replicas on local setup.

# local setup
To setup this application on your local machine you will need to install following items:
1. Docker
2. VSCode
3. **Remote Development extension** for VSCode  

On opening this project in VSCode you will be prompted with a notification to repoen and rebuild the application in container.  

To setup redis cluster use command `redis-cli --cluster create redis1:6379 redis2:6379 redis3:6379 --cluster-replicas 0` in any of the cluster nodes.

To run the application open `app.py` in your editor and use the `Run` option provided by VSCode. The api documentation for this project is already available in this repository.

# deployment guidelines
## staging env @tiket

Python CGI for Apache and Nginx + cherryPy
===============================================

For a personal project I needed a Python CGI service that would work both on a remote Apache server and my local Nginx server. This project accomplishes exactly that. 


Setup
=====

By default, the CherryPy server will call the main() function of your script. It is important that this function accepts an `env` argument. This way, any POST or GET data can be fed into your CGI application. Furthermore, this function **must** return its response (as opposed to printing it to stdout). 

Have a look at the supplied example.py file for an example of a working main function. 


Running
=======

First of all, nginx needs to be aware that .py scripts should be sent to the (not yet running) CherryPy server. This can be done by including the supplied python.conf file into your server configuration. 

browsing to the cgi file in the browser will now result in a 504 error, because nginx can't find the CherryPy server yet. 

To run the server, simply do
```sh 
python3 server.py 
```
Alternatively, you can use the virtualenv
```sh
source pyapp_venv/bin/activate
python3 server.py
```

Useful links
===========

* <a href="https://www.digitalocean.com/community/tutorials/how-to-deploy-cherrypy-web-applications-behind-nginx-reverse-proxy">How to Deploy CherryPy Web Applications Behind Nginx Reverse-Proxy</a>


Finally 
=======

I'm by no means an expert on either Nginx or CherryPy/CGI. If there is a better way to do this, I'd be glad to hear it. Also please ask any questions about this project here. 




BACKGROUND CONTEXT
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.


Application server vs web server
An application server and a web server are both important components of web application architecture, but they serve different purposes. Here's a brief explanation of each:

Web Server:
A web server's primary function is to handle HTTP requests and deliver web content to clients (usually web browsers) over the internet. It's responsible for hosting static files, such as HTML, CSS, JavaScript, images, and other resources that make up a website. When a client makes a request for a web page, the web server retrieves the requested files and sends them back to the client's browser for display.
Web servers often have additional features such as support for server-side scripting languages like PHP, Python, or Ruby, which allow the server to generate dynamic content based on user requests. However, their main focus is on handling HTTP requests, serving files, and managing basic web protocols.

Common examples of web servers include Apache HTTP Server, Nginx, and Microsoft IIS.

Application Server:
An application server provides a runtime environment for executing and managing web applications. It's designed to handle complex business logic, application processing, and data storage. Application servers support the development and deployment of dynamic, transactional, and scalable applications.
In addition to delivering static files, application servers provide services such as database access, security, session management, clustering, load balancing, and integration with other enterprise systems. They often support multiple protocols, including HTTP, to communicate with clients and other components of the application architecture.

Application servers typically support server-side technologies such as Java Enterprise Edition (Java EE), .NET, or other frameworks that enable developers to build sophisticated web applications.

Common examples of application servers include Apache Tomcat, JBoss/WildFly, IBM WebSphere, and Oracle WebLogic.

In summary, a web server primarily focuses on serving static content and handling basic web protocols, while an application server provides a more comprehensive environment for executing dynamic web applications, managing business logic, and offering additional services to support complex application requirements.




How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
If, instead, you are using Python 3, type:

sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx

Create a Python Virtual Environment
sudo pip3 install virtualenv
Now, we can make a parent directory for our Flask project. Move into the directory after you create it:

mkdir ~/myproject
cd ~/myproject
We can create a virtual environment to store our Flask project’s Python requirements by typing:

virtualenv myprojectenv
This will install a local copy of Python and pip into a directory called myprojectenv within your project directory.

Before we install applications within the virtual environment, we need to activate it. You can do so by typing:

source myprojectenv/bin/activate
Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this (myprojectenv)user@host:~/myproject$.



Set Up a Flask Application
Install Flask and Gunicorn
We can use the local instance of pip to install Flask and Gunicorn. Type the following commands to get these two components:

Note

Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).

pip install gunicorn flask


Create a Sample App
Now that we have Flask available, we can create a simple application. Flask is a micro-framework. It does not include many of the tools that more full-featured frameworks might, and exists mainly as a module that you can import into your projects to assist you in initializing a web application.

While your application might be more complex, we’ll create our Flask app in a single file, which we will call myproject.py:

nano ~/myproject/myproject.py
Within this file, we’ll place our application code. Basically, we need to import flask and instantiate a Flask object. We can use this to define the functions that should be run when a specific route is requested:

~/myproject/myproject.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
This basically defines what content to present when the root domain is accessed. Save and close the file when you’re finished.

If you followed the initial server setup guide, you should have a UFW firewall enabled. In order to test our application, we need to allow access to port 5000.

Open up port 5000 by typing:

sudo ufw allow 5000
Now, you can test your Flask app by typing:

python myproject.py
Visit your server’s domain name or IP address followed by :5000 in your web browser:

http://server_domain_or_IP:5000
You should see something like this:

Flask sample app

When you are finished, hit CTRL-C in your terminal window a few times to stop the Flask development server.



Create the WSGI Entry Point
Next, we’ll create a file that will serve as the entry point for our application. This will tell our Gunicorn server how to interact with the application.

We will call the file wsgi.py:

nano ~/myproject/wsgi.py
The file is incredibly simple, we can simply import the Flask instance from our application and then run it:

~/myproject/wsgi.py
from myproject import app

if __name__ == "__main__":
    app.run()
Save and close the file when you are finished.




Testing Gunicorn’s Ability to Serve the Project
Before moving on, we should check that Gunicorn can correctly.

We can do this by simply passing it the name of our entry point. This is constructed by the name of the module (minus the .py extension, as usual) plus the name of the callable within the application. In our case, this would be wsgi:app.

We’ll also specify the interface and port to bind to so that it will be started on a publicly available interface:

cd ~/myproject
gunicorn --bind 0.0.0.0:5000 wsgi:app
Visit your server’s domain name or IP address with :5000 appended to the end in your web browser again:

http://server_domain_or_IP:5000
You should see your application’s output again:

Flask sample app

When you have confirmed that it’s functioning properly, press CTRL-C in your terminal window.

We’re now done with our virtual environment, so we can deactivate it:
deactivate

Any Python commands will now use the system’s Python environment again.





Create a systemd Unit File
The next piece we need to take care of is the systemd service unit file. Creating a systemd unit file will allow Ubuntu’s init system to automatically start Gunicorn and serve our Flask application whenever the server boots.

Create a unit file ending in .service within the /etc/systemd/system directory to begin:

sudo nano /etc/systemd/system/myproject.service
Inside, we’ll start with the [Unit] section, which is used to specify metadata and dependencies. We’ll put a description of our service here and tell the init system to only start this after the networking target has been reached:

/etc/systemd/system/myproject.service
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target
Next, we’ll open up the [Service] section. We’ll specify the user and group that we want the process to run under. We will give our regular user account ownership of the process since it owns all of the relevant files. We’ll give group ownership to the www-data group so that Nginx can communicate easily with the Gunicorn processes.

We’ll then map out the working directory and set the PATH environmental variable so that the init system knows where our the executables for the process are located (within our virtual environment). We’ll then specify the commanded to start the service. Systemd requires that we give the full path to the Gunicorn executable, which is installed within our virtual environment.

We will tell it to start 3 worker processes (adjust this as necessary). We will also tell it to create and bind to a Unix socket file within our project directory called myproject.sock. We’ll set a umask value of 007 so that the socket file is created giving access to the owner and group, while restricting other access. Finally, we need to pass in the WSGI entry point file name and the Python callable within:

/etc/systemd/system/myproject.service
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
Finally, we’ll add an [Install] section. This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running:

/etc/systemd/system/myproject.service
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
With that, our systemd service file is complete. Save and close it now.

We can now start the Gunicorn service we created and enable it so that it starts at boot:

sudo systemctl start myproject
sudo systemctl enable myproject





Configuring Nginx to Proxy Requests
Our Gunicorn application server should now be up and running, waiting for requests on the socket file in the project directory. We need to configure Nginx to pass web requests to that socket by making some small additions to its configuration file.

Begin by creating a new server block configuration file in Nginx’s sites-available directory. We’ll simply call this myproject to keep in line with the rest of the guide:

sudo nano /etc/nginx/sites-available/myproject
Open up a server block and tell Nginx to listen on the default port 80. We also need to tell it to use this block for requests for our server’s domain name or IP address:

/etc/nginx/sites-available/myproject
server {
    listen 80;
    server_name server_domain_or_IP;
}
The only other thing that we need to add is a location block that matches every request. Within this block, we’ll include the proxy_params file that specifies some general proxying parameters that need to be set. We’ll then pass the requests to the socket we defined using the proxy_pass directive:

/etc/nginx/sites-available/myproject
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
That’s actually all we need to serve our application. Save and close the file when you’re finished.

To enable the Nginx server block configuration we’ve just created, link the file to the sites-enabled directory:

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
With the file in that directory, we can test for syntax errors by typing:

sudo nginx -t
If this returns without indicating any issues, we can restart the Nginx process to read the our new config:

sudo systemctl restart nginx
The last thing we need to do is adjust our firewall again. We no longer need access through port 5000, so we can remove that rule. We can then allow access to the Nginx server:

sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
You should now be able to go to your server’s domain name or IP address in your web browser:

http://server_domain_or_IP
You should see your application’s output:

Flask sample app

Note

After configuring Nginx, the next step should be securing traffic to the server using SSL/TLS. This is important because without it, all information, including passwords are sent over the network in plain text.

The easiest way get an SSL certificate to secure your traffic is using Let’s Encrypt. Follow this guide to set up Let’s Encrypt with Nginx on Ubuntu 16.04.



WHAT IS GUNICORN?
Gunicorn (short for "Green Unicorn") is a Python web server gateway interface (WSGI) HTTP server. It's designed to serve Python web applications, including those built with frameworks like Flask and Django. Gunicorn acts as a middle layer between your web application and the web server (such as Nginx or Apache), handling incoming requests, executing your application code, and returning responses.

Gunicorn supports multiple worker processes, allowing it to handle concurrent requests efficiently and take advantage of multiple CPU cores. Each worker process can handle one request at a time, and Gunicorn manages the load balancing and coordination between these workers. This architecture makes Gunicorn suitable for production deployments, where high performance and scalability are important.

When deploying a Python web application, Gunicorn is often used as the WSGI server in conjunction with a reverse proxy server (like Nginx). The reverse proxy server handles tasks such as serving static files, SSL termination, load balancing, and caching, while Gunicorn focuses on executing the Python application code and handling dynamic requests.

Gunicorn provides various configuration options to customize its behavior, including the number of worker processes, timeouts, logging, and more. It's a widely used and well-established tool in the Python ecosystem, known for its simplicity, reliability, and performance.



Be careful with the way Flask manages slash in route - strict_slashes
it's important to be mindful of how Flask handles trailing slashes in routes when using the strict_slashes option. By default, Flask treats routes with and without trailing slashes as separate endpoints. For example, /example and /example/ are considered distinct routes. This behavior can affect how your routes are matched and can lead to unexpected results.

To control the handling of trailing slashes in routes, Flask provides the strict_slashes option. Here's how it works:

strict_slashes=False (default):

/example and /example/ are treated as separate routes.
Requests to /example will result in a 404 Not Found if the route is defined as /example/.
Requests to /example/ will result in a 404 Not Found if the route is defined as /example.
strict_slashes=True:

/example and /example/ are treated as the same route.
Requests to /example will match the route defined as /example/.
Requests to /example/ will match the route defined as /example.
When defining routes in your Flask application, it's important to be consistent with your trailing slashes and consider how you want to handle them. Here are a few best practices:

Choose a consistent style for your routes with or without trailing slashes, and stick to it throughout your application.
If you prefer routes with trailing slashes, define your routes with /example/ and set strict_slashes=True.
If you prefer routes without trailing slashes, define your routes with /example and leave strict_slashes at its default value (False).
Make sure to test your routes and handle redirects or error responses appropriately based on your chosen trailing slash style.
Being aware of how Flask handles trailing slashes and using the strict_slashes option appropriately can help you maintain consistent route behavior and prevent potential issues with route matching in your Flask application.




Upstart documentation
Upstart is an event-based init system used in some Linux distributions, including Ubuntu versions prior to 15.04. It has been replaced by systemd in recent Ubuntu releases. Nevertheless, if you still need information on Upstart, you can refer to the following resources:

Upstart Wiki: The official Upstart wiki provides detailed documentation, including an introduction, job configuration, events, environment variables, and more. You can access it at:

Link: https://wiki.ubuntu.com/SystemdForUpstartUsers
Upstart Cookbook: The Upstart Cookbook offers practical examples and recipes for common use cases. It covers various topics such as starting and stopping services, managing multiple instances, managing environment variables, and more. You can find it here:

Link: https://upstart.ubuntu.com/cookbook/
Ubuntu Upstart Man Page: The Upstart man page provides a comprehensive reference for Upstart configuration and usage. You can access it by running the following command in your terminal:

Copy code
man upstart
Please note that while Upstart was widely used in the past, it has largely been replaced by systemd. If you're running a newer version of Ubuntu or another Linux distribution, it's recommended to refer to systemd documentation for managing services and system initialization.



RESOURCES
Read or watch:

Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
Running Gunicorn
Be careful with the way Flask manages slash in route - strict_slashes
Upstart documentation


GENERAL
A README.md file, at the root of the folder of the project, is mandatory
Everything Python-related must be done using python3
All config files must have comments


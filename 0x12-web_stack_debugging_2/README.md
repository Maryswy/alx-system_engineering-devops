TEST AND VERIFY YOUR ASSUMPTIONS
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

Is the web server started? - You can check using the service manager, also double check by checking process list.
On what port should it listen? - Check your web server configuration
Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
It is listening on the correct server IP? - netstat is also your friend here
Is there a firewall enabled?
Have you looked at logs? - usually in /var/log and tail -f is your friend
Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
There is a good chance that at this point you will already have found part of the issue.


NETWORK ISSUE 
For the machine level, you want to ask yourself these questions:
Does the server have the expected network interfaces and IPs up and running? ifconfig
Does the server listen on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
Does the server have the correct firewall rules? iptables, ufw:
iptables -L
sudo ufw status



PROCESS ISSUE
If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).
Is the software started? init, init.d:
service NAME_OF_THE_SERVICE status
/etc/init.d/NAME_OF_THE_SERVICE status


Is the software process running? pgrep, ps:
pgrep -lf NAME_OF_THE_PROCESS
ps auxf

Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend

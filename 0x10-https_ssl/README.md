0x10. HTTPS SSL
DevOps
SysAdmin
Security

DNS
DNS is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP:

Be sure to know the main DNS record types:
A
CNAME
MX
TXT

Advanced
Use DNS to scale with round-robin DNS
What’s an NS Record?
What’s an SOA Record?


The root domain and sub domain - differences
A root domain is the parent domain to a sub domain, and its name is not, and can not be divided by a dot.

While creating any domain at a website of domain provider, the provider system will always ask you to choose a domain name without a dot in the name. In other words, the address of the root domain may be mydomain.com but it can never be my.domain.com. Domain providers block the ability to create such a root domain until you type a name without the dot. Why?

The dot in the domain name delimits the sub domain name (the part of the name before the dot, eg. www.my.) and the root domain name ( the part after the dot, ie .domain.com). This means that the address my.domain.com is a sub domain of the root domain, whose name is domain.com

In an administrator panel at domain provider account, you can create any number of sub domains. This means that for the root domain called domain.com it is possible to create different sub domains eg. my.domain.com, your.domain.com, school.domain.com… Creating multiple sub domains is always free and does not require you to set up new accounts on a domain provider website.

As you can see, all of the domain addresses used as an example (above) do not start with the www prefix. www is also a sub domain. The www prefix always leads to the main domain. See: What’s the point in having www in a url?



WHAT IS HTTPS?
HTTPS stands for Hypertext Transfer Protocol Secure. It is a secure version of HTTP, the protocol used for transferring data over the internet. HTTPS uses encryption to protect the data transmitted between a user's web browser and a website, ensuring that sensitive information such as login credentials, credit card details, and other private data is kept safe from hackers and eavesdroppers.

When a website uses HTTPS, it means that the data transmitted between the user and the website is encrypted and secure. HTTPS is implemented using SSL (Secure Socket Layer) or TLS (Transport Layer Security) encryption protocols, which use a combination of symmetric and asymmetric encryption to ensure that data is protected.

In order to use HTTPS, a website must obtain an SSL/TLS certificate from a trusted Certificate Authority (CA). This certificate is used to verify the identity of the website and to establish a secure connection between the user's browser and the website. When a user visits a website that uses HTTPS, their browser will display a padlock icon in the address bar, indicating that the connection is secure and that their data is being protected.



WHAT ARE THE 2 MAIN ELEMENTS THAT SSL IS PROVIDING?
SSL (Secure Socket Layer) is a predecessor of TLS (Transport Layer Security) protocol, which provides security for communication over the internet. SSL/TLS provides two main elements to ensure secure communication:

Encryption: SSL/TLS uses encryption algorithms to scramble data transmitted between a user's web browser and a website, making it unreadable to anyone who intercepts it. This prevents eavesdroppers and hackers from stealing sensitive information such as login credentials, credit card details, and other private data. Encryption ensures that the data is protected during transmission, even if it is intercepted by unauthorized parties.

Authentication: SSL/TLS provides authentication mechanisms to ensure that the website a user is communicating with is legitimate and not an imposter. This is done by verifying the identity of the website using a digital certificate issued by a trusted Certificate Authority (CA). When a user connects to a website using SSL/TLS, their browser will verify the website's identity by checking its digital certificate. If the certificate is valid and issued by a trusted CA, the browser will establish a secure connection with the website. This helps prevent phishing attacks and other forms of online fraud.

In summary, SSL/TLS provides encryption to protect data during transmission and authentication to ensure that users are communicating with legitimate websites.



SSL termination
SSL termination is the process of terminating an SSL (Secure Sockets Layer) connection at a proxy server or load balancer instead of allowing it to reach the destination server.

When a client initiates an SSL connection to a server, the SSL protocol ensures that the connection is encrypted and secure. However, SSL encryption can put a heavy load on servers, especially when dealing with a large number of connections. This is where SSL termination comes in - by terminating the SSL connection at a proxy server or load balancer, the SSL encryption and decryption workload is offloaded from the destination server, which can improve performance and scalability.

In the context of a load balancer, SSL termination is often used to offload SSL processing from backend servers, which allows them to focus on handling application requests instead of SSL encryption and decryption. The load balancer terminates the SSL connection from the client, decrypts the traffic, and forwards the unencrypted traffic to the backend servers. The backend servers then process the unencrypted traffic and return the response to the load balancer, which encrypts the traffic again and sends it back to the client.

SSL termination can also be used to implement security features such as SSL inspection and content filtering, which would not be possible if the SSL connection was allowed to pass through to the backend servers without being terminated first.

In summary, SSL termination is a technique used to offload SSL processing from backend servers and can improve performance, scalability, and security of web applications.



Bash function
#!/usr/bin/env bash

# Define a function that checks if a website is using HTTPS SSL
check_ssl() {
    local website=$1
    local response=$(curl -sI https://"$website" | head -n 1 | cut -d' ' -f2)
    if [[ "$response" =~ ^2 ]]; then
        echo "$website is using HTTPS SSL"
    else
        echo "$website is NOT using HTTPS SSL"
    fi
}

# Call the function with a website as an argument
check_ssl "example.com"

In this example, the check_ssl function takes a website as an argument and uses the curl command to send a HEAD request to the website's HTTPS URL. The response is then parsed using the head and cut commands to extract the HTTP status code from the first line of the response.

If the status code starts with a "2" (indicating a successful response), the function outputs a message saying that the website is using HTTPS SSL. Otherwise, it outputs a message saying that the website is not using HTTPS SSL.

The function is called with the check_ssl "example.com" command, which passes the string "example.com" as an argument to the function. The script then uses the echo command to print the result.

When the script is executed, it will output a message indicating whether the website is using HTTPS SSL or not.

You can customize this function to suit your needs, such as by adding additional error handling or modifying the output message.


GENERAL
What is HTTPS SSL 2 main roles
What is the purpose encrypting traffic
What SSL termination means


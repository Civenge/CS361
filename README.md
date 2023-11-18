# CS361
# Requesting Data:
To get data from the microservice, first launch it, it will be listening for a message using sockets.  Make sure the port is configured as the same as the client.  Then launch the microservice, prior to when the request is made to it (typically this will be before the client is launched).  Next, send a JSON file to the microservice in 1024 byte chunks, like so:

![image](https://github.com/Civenge/CS361/assets/91363144/a2eb9883-5398-435c-9604-0d15e441440f)


# Receiving Data:
This will allow the microservice to process the data and send back a response with the finished product.  The response will also be in 1024 byte data, which will represent a file that the client can then convert into a .docx file containing a bar chart.  An example of how the data can be received from the microservice:

![image](https://github.com/Civenge/CS361/assets/91363144/8c844592-ebb7-4d5d-b130-27ecc8b678cd)



# UML Diagram:
![UML](https://github.com/Civenge/CS361/assets/91363144/2efdf76a-2c1d-4e08-812c-abb565246716)


# CS361
# Requesting Data:
To get data from the microservice, first launch it, it will be listening for a message using sockets.  Make sure the port is configured as the same as the client.  Then launch the microservice, prior to when the request is made to it (typically this will be before the client is launched).  Next, send a JSON file to the microservice in 1024 byte chunks, like so:
![image](https://github.com/Civenge/CS361/assets/91363144/3ae9792d-b3b0-45a2-adba-b29d9a7a1a74)


This will allow the microservice to process the data and send back a response with the finished product.  The response will also be in 1024 byte data, which will represent a file that the client can then convert into a .docx file containing a bar chart.

![UML](https://github.com/Civenge/CS361/assets/91363144/abf62c40-ce2a-440a-ab96-a1b723be2d2d)

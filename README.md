# CS361
# Requesting Data:
To get data from the microservice, first launch it, it will be listening for a message using sockets.  Make sure the port is configured as the same as the client.  Then launch the microservice, prior to when the request is made to it (typically this will be before the client is launched).  Next, send a JSON file to the microservice in 1024 byte chunks.  This will allow the microservice to process the data and send back a response with the finished product.  The response will also be in 1024 byte data, which will represent a file that the client can then convert into a .docx file containing a bar chart.

![Diagram]https://lucid.app/lucidchart/6bdc6010-1ec1-4b4f-b442-7531d703ec2b/edit?viewport_loc=283%2C1277%2C2219%2C1201%2C0_0&invitationId=inv_5e295412-f711-43ad-bac0-5da7e8fa22e4

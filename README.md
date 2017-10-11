# Java_word2vec


# Prerequisite: 

Download Google pre-trained model https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit


Put the downloaded file in ./model




# Usage:
Run word2vec_server.py. Let the server load the pre-trained model and wait for requests.

Call the java function wordSimGenerator, the arguments are two words in string.

The java function will call a python word2vec client. The python client will send the two words to word2vec_server through socket.

After the server calculates the similarity score for two words, it sends the message back to client, and then back to java function.

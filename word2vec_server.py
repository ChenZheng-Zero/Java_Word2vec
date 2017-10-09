import gensim
import socket


def run_word2vec_server(trained_model_path):
    # Load Google's pre-trained Word2Vec model.
    model = gensim.models.KeyedVectors.load_word2vec_format(trained_model_path, binary=True)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 10000)
    print("start up on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("wait for a connection")
        connection, client_address = sock.accept()
        try:
            print("connection from ", client_address)
            data = connection.recv(1024)
            print("the words received are ", data.decode('utf-8'))
            words = data.decode('utf-8').strip().split(", ")
            score = round(model.wv.similarity(words[0], words[1]), 4)
            print("send back similarity score", score)
            connection.send(str.encode(str(score)))
        finally:
            connection.close()


if __name__ == '__main__':
    run_word2vec_server(trained_model_path="./model/GoogleNews-vectors-negative300.bin")



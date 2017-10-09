import socket
import sys


def run_word2vec_client(word1, word2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 10000)
    # print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    try:
        message = word1 + ", " + word2
        # print('sending "%s"' % message)
        sock.sendall(str.encode(message))
        similarity_score = float(sock.recv(1024))
        # print("get similarity score %f" % similarity_score)
    finally:
        # print('closing socket')
        sock.close()
    return similarity_score


if __name__ == '__main__':
    score = run_word2vec_client(sys.argv[1], sys.argv[2])
    print(score)
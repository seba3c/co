# -*- coding: utf-8 -*-


def get_hostname():
    import socket
    return socket.gethostname()


if __name__ == '__main__':
    print(get_hostname())

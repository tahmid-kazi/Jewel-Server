#!/usr/bin/env python3

import socket
import sys

from file_reader import FileReader

class Jewel:

    def __init__(self, port, file_path, file_reader):
        self.file_path = file_path
        self.file_reader = file_reader

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        cookies = None
        s.listen(5)

        while True:
            (client, address) = s.accept()
            data = client.recv(1024).decode('utf-8')
            if not data:
                break
            print('[CONN] Connection from IP: ', address, 'and port: ',str(port))
            #HTTP response parsing (tested and works)----------------------
            string_list = data.split(' ')
            request_method = string_list[0].strip()
            requested_file = string_list[1].strip()
            requested_file = requested_file.split('?')[0]
            print(request_method) #tested and works
            print(requested_file) #tested and works
            #--------------------------------------------------------------
            if (len(request_method)<=2):
                client.send("400 Bad Request\r\n\r\n".encode())
                print("[ERROR] ["+str(address)+":" + str(port)+"]: "+"400 Bad Request")
            else:
                if (request_method =="GET"):
                    file = file_reader.get(file_path+requested_file, cookies)
                    #print(file)
                    if not file:
                        print("[ERROR] ["+str(address)+":" + str(port)+"]: "+"404 File not Found")
                        client.send("404 File not Found\r\n\r\n".encode())
                    else:
                        client.send(file)
                elif (request_method =="HEAD"):
                    file2 = file_reader.head(filepath+requested_file, cookies)
                    client.send(file2)
                else:
                    print("[ERROR] ["+str(address)+":" + str(port)+"]: "+"501: Method Unimplemented")
                    client.send("[ERROR] Error 501: Method Unimplemented\r\n\r\n".encode())
            client.close()

if __name__ == "__main__":
    port = int(sys.argv[1])
    file_path = sys.argv[2]

    FR = FileReader()

    J = Jewel(port, file_path, FR)

import os

class FileReader:

    def __init__(self):
        pass

    def get(self, filepath, cookies):
        header_response = 'HTTP/1.1 200 OK\r\n'.encode('utf-8')
        if os.path.exists(filepath):
            if (not os.path.isfile(filepath)):
                data = os.listdir(filepath)
                #return ("<html><body><h1>"+ str(data) +"</h1></body></html>").encode('utf-8')
            else:
                file = open(filepath,'rb') # open file , r => read , b => byte format
                response = file.read()
                file.close()
                header_response += self.head(filepath, cookies)
                final_response = header_response + '\r\n'.encode('utf-8') #final response = header response and actual data
                final_response += response + '\r\n\r\n'.encode('utf-8') #this is the main file being served up
                return final_response
                #return bytes(header,'utf-8') + bytes(file_size +" ",'utf-8') + response
        else:
            return '[ERROR] HTTP/1.1 404 Not Found\r\n'.encode('utf-8')

    def head(self, filepath, cookies):
        header='' #adding to this string later
        if (os.path.exists(filepath)):
            file_info = os.stat(filepath)
            size = file_info.st_size
            mimetype=''
            #mimetype = filepath[len(filepath): len(filepath)-3: 1]
            if(filepath.endswith('.jpg') or filepath.endswith('.jpeg')):
                mimetype = 'image/jpg'
            elif(filepath.endswith('.png')):
                mimetype = 'image/png'
            elif(filepath.endswith('.gif')):
                mimetype = 'image/gif'
            elif(filepath.endswith('.css')):
                mimetype = 'text/css'
            elif(filepath.endswith('.html')):
                mimetype = 'text/html'
            elif(filepath.endswith('.txt')):
                mimetype = 'text/txt'
            else:
                mimetype = 'unsupported file type! (for now)'
            header += 'Server: tk3kb\r\n'
            header += 'Content-Type: '+str(mimetype)+'\r\n'
            header += 'Content Length(bytes): '+str(size)+'\r\n'
            return header.encode('utf-8')

        else:
            return '[ERROR] HTTP/1.1 404 Not Found\r\n'.encode('utf-8')

#testing code
#p1 = FileReader()
#value = p1.head("www/imgs/picture5.jpg", "cookie")
#print(value)
#get_request = p1.get("www", "cookie")
#print(get_request)
#get_request2 = p1.get("www/imgs/picture5.jpg", "cookie")
#print(get_request2)

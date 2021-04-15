import socket

class SocketPgm:
    #Setting the default port as 80 (http)
    #also accept port from user...
    def __init__(self,port=80):
        self.port=port
    def conn(self,host):
        try:
            #creating socket object with IPv4 and TCP protocol...
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #returns the IP adress
            hostIp=socket.gethostbyname(host)
        except:
            print("error resolving the Host")
        
        try:
            sock.settimeout(3)
            sock.connect((hostIp,self.port))
            print("connection successful {} ({})".format(host,hostIp))
        except:
            print("Connection failed")

def main():
    hostInp=input("Enter target Address to connect : ")
    portInp=input("Enter port to connect,otherwise enter P for default port 80: ")
    portInp=portInp.upper()
    if portInp!="P":
        s=SocketPgm(int(portInp))
    else:
        s=SocketPgm()
    s.conn(hostInp)

if __name__ == '__main__':
	main()   
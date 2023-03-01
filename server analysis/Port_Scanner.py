import socket

ip_input = input('IP를 입력하세요: ')
ports = [21, 22, 80, 443, 3389, 8080, 1433, 1521, 3306, 5432]
open_ports = []
banners = []

for port in ports:
    try:
        s = socket.socket()
        print("Attempting to connect to " + ip_input + " : " + str(port))
        s.connect((ip_input, port))
        
        # 포트가 열려있다면, 응답받은 배너 표시
        banner = s.recv(1024)
        if banner:
            print("Port " + str(port) + " Open : " + str(banner))
        elif banner == b'':
            print("Port " + str(port) + " Open")
        open_ports.append(port)
        banners.append(banner)
        s.close()
    except: pass
    
print('\n<result>')

for n in range(len(open_ports)):
    print("Port " + str(open_ports[n]) + " : ", end ='')
    try:
        str_text = banners[n].decode('utf-8')
        print(str_text)
    except: pass

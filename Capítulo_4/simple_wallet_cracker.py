import subprocess
import sys

def tryCracking(words):
    # Testing if bitcoin-cli is in the system
    p = subprocess.Popen(['bitcoin-cli', '-h'], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
    # Grabbing the output
    out, err = p.communicate()
    if err != "":
        print "bitcoin-cli is not ready in this system. Verify the Bitcoin installation and try again."
        sys.exit()

    # Performing tests...
    for i, word in enumerate(words):
        print "Trying " + str(i+1) + "/" + str(len(words)) + ": " + word
        
        print "\t> bitcoin-cli walletpassphrase \"" + word  + "\" 10"
        p = subprocess.Popen(['bitcoin-cli', 'walletpassphrase', word, '10'], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
        
        # Grabbing the output
        out, err = p.communicate()
        if err == "":
            print "PASSWORD FOUND! " + word
            break

def showUsage():
    print "Usage:   python wallet_cracker.py <dict_file>"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "The program needs exactly one parameter."
        showUsage()
        sys.exit()
    words = open(sys.argv[1]).read().splitlines()
    # Launching the process...
    tryCracking(words)   
     

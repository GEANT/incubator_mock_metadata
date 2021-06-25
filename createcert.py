import os
for i in range(300000):
    os.system('openssl req -nodes -sha256 -x509 -key idp.key -out idp.crt -days 3650 -subj "/"')
    os.system("sed '1d;$d' idp.crt | xargs |sed 's/ //g'  >> data/certs300000.txt")

import os
import random
import fileinput

for i in range(10):
    
    # import random
    choicefile=open("names.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    choice=random.choice(linelist)

    choicefile=open("urls.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    urlchoice=random.choice(linelist)

    choicefile=open("corps.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    etairiachoice=random.choice(linelist)
    
    choicefile=open("certs300000.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    sertifikatochoice=random.choice(linelist)

    choicefile=open("emails.txt","r")
    linelist=[]
    for line in choicefile:
        linelist.append(line)
    taxydromiochoice=random.choice(linelist)

    # import fileinput

    if i%2==0:
        with fileinput.FileInput("fakemetasp", inplace=False, backup='.bak') as file:
            for line in file:
                line = line.replace("dwseonoma", choice)
                line = line.replace("testurl", urlchoice)
                line = line.replace("etairia", etairiachoice)
                line = line.replace("taxydromio", taxydromiochoice)
                line = line.replace("sertifikato", sertifikatochoice)

                f =open ("newdata10.xml", "a")
                f.write(line)
                #f.close
    else:
        with fileinput.FileInput("fakemeta", inplace=False, backup='.bak') as file:
            for line in file:
                line = line.replace("dwseonoma", choice)
                line = line.replace("testurl", urlchoice)
                line = line.replace("etairia", etairiachoice)
                line = line.replace("taxydromio", taxydromiochoice)
                line = line.replace("sertifikato", sertifikatochoice)

                #f =open ("newdata100.xml", "a")
                f.write(line)
                #f.close

        

   
    
    

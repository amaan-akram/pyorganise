

import os #Used for path's and creating dirs
import shutil #Used for moving file to new dir

path = os.getcwd()  #current path 
USER = "amaan"  ##CHANGE THIS TO YOUR SYS SUSER NAME
DESKTOP = "/home/"+USER+"/Desktop/" 
HOME = "/home" 


for file in os.listdir(DESKTOP):    #itterate through list of files 

    ##Simple Txt file, use this as template for other file types
    if file.endswith(".txt"):                             #if file type ends in .???                   
        if os.path.exists(DESKTOP + "/txt"):                    #and if folder ??? exists
            shutil.move(DESKTOP + file, DESKTOP + "/txt"            #Move file to folder
        else:                                                    #Else if folder doesnt exist create it
            try:
                os.mkdir(DESKTOP +"/txt")
            except OSError:
                print("Error")
            else:
                print("txt dir made")
            
            shutil.move(DESKTOP + file, DESKTOP + "/txt")        #Then move file to folder after creating :)


    #Image Files
    if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".svg") or file.endswith(".svg"):
        if os.path.exists(DESKTOP + "/img"):
            shutil.move(DESKTOP + file, DESKTOP + "/img")
        else:
            try:
                os.mkdir(DESKTOP +"/img")
            except OSError:
                print("Error")
            else:
                print("img dir made")
            
            shutil.move(DESKTOP + file, DESKTOP + "/img")




    if file.endswith(".js"):
        if os.path.exists(DESKTOP + "/javascript"):
            shutil.move(DESKTOP + file, DESKTOP + "/javascript")
        else:
            try:
                os.mkdir(DESKTOP +"/javascript")
            except OSError:
                print("Error")
            else:
                print("javascript dir made")
            
            shutil.move(DESKTOP + file, DESKTOP + "/javascript")

    #Javascript files
     if file.endswith(".js"):
        if os.path.exists(DESKTOP + "/javascript"):
            shutil.move(DESKTOP + file, DESKTOP + "/javascript")
        else:
            try:
                os.mkdir(DESKTOP +"/javascript")
            except OSError:
                print("Error")
            else:
                print("javascript dir made")
            
            shutil.move(DESKTOP + file, DESKTOP + "/javascript")


    #Go files
    if file.endswith(".go"):
        if os.path.exists(DESKTOP + "/go"):
            shutil.move(DESKTOP + file, DESKTOP + "/go")
        else:
            try:
                os.mkdir(DESKTOP +"/go")
            except OSError:
                print("Error")
            else:
                print("go dir made")
            
            shutil.move(DESKTOP + file, DESKTOP + "/go")
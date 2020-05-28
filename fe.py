#coding: utf8
#File Integrity Checking System v0.1.0-alpha
#LSHT Inc.
"""
File list:
zimo.py
LICENSE
README.md
testing.py
fic.log
"""
import os, json, time
def fic():
    files = ["zimo.py", "README.md", "LICENSE", "testing.py"]
    missing_files = []
    if os.path.isfile("fic.log") == True:
        with open("fic.log", 'a') as fic_log:
            fic_log.write(str(time.time()) + "-scan-missingfile-")
    elif os.path.isfile("fic.log") == False:
        with open("fic.log", 'a+') as fic_log:
            fic_log.write(str(time.time()) + "-scan-missingfile-")
    for file in files:
        file_exists = os.path.isfile(file)
        if file_exists == True:
           pass
        elif file_exists == False:
            print("cannot find file " +
            file +
            ". Please reinstall zimo.")
            missing_files.append(file)
            with open("fic.log", 'a') as fic_log:
                fic_log.write(file)


    
#os.path.isfile("test-data")

fic()
pause = input("pause.")
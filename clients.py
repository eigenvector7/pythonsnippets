#! /usr/bin/env python3

import sys
import re

print(sys.version_info)
print(__name__)

fnP = re.compile(r'^([a-z]+)(\s[a-z]+)?$',re.IGNORECASE) # Pattern for first name
lnP = re.compile(r'^[a-z]+$',re.IGNORECASE) # Pattern for last name
clientsD = dict()



def retrieveecord(stuId):

    fn = ""
    ln = ""

    if not stuId in clientsD.keys(): #  check if student with this ID is already available. Otherwise Add new
        print("Please enter the Firstname")
        fn = input()    # This is safe only in python3. Use input_raw for 2.x
        if fn is "":
            print("No firstname  - using default firstname unknown FNU")
            fn = "FNU"

        fnm = fnP.search(fn)
        if not fnm:
            print("first name format doesn't match - try again")

        print("Please enter the Lastname")
        ln = input()
        if ln is "":
            print("No lastname  - using default lastname unknown LNU")
            ln = "LNU"
        lnm = lnP.search(ln)
        if not fnm:
            print("first name format doesn't match - try again")

    return clientsD.setdefault(stuId, (fn, ln))

if __name__ == "__main__":
    print("Please enter the studentID")
    mystuId = input()
    while (mystuId):
        sRecord = retrieveecord(mystuId)
        print(sRecord)
        print("Please enter the next studentID")
        mystuId = input()
    print(clientsD)
    print("OK BYE")






# *] Command Line Arguments :-

#-> Using sys.argv :-
'''
import sys

n = len(sys.argv)
print('Size of sys.argv is ',n)

print('\nName of python script :',sys.argv[0])

print('\nArguments Passed :',end = " ")
for i in range(1,n):
    print(sys.argv[i],end = " ")

sum=0
for i in range(1,n):
    sum += int(sys.argv[i])
print('\nResult :',sum)
'''

#-> Using getopt.getopt() module :-

'''
import sys, getopt

argumentList = sys.argv[1:]
options = "hmo:"
long_options = ["help","my_file","Output="]

try:
    arguments,values = getopt.getopt(argumentList,options,long_options)
    for currentArgument,currentValue in arguments:
        if currentArgument in ("-h","--help"):
            print("Display Help")
        elif currentArgument in ("-m","--my_file"):
            print("Display file_name",sys.argv[0])
        elif currentArgument in ("-o","--Output"):
            print(("Enabling special output mode (%s)") % (currentValue))
except getopt.error as err:
     print(str(err))
'''

#-> Using argparse module :- 


import argparse
'''
#simple program...

parser1 = argparse.ArgumentParser()
parser1.parse_args()

#Adding description to the help message...

message = "Adding Description"
parser2 = argparse.ArgumentParser(description = message)
parser2.parse_args()

#Defining optional value...

parser3 = argparse.ArgumentParser()
parser3.add_argument("-o","--Output",help = "Show Output")
args = parser3.parse_args()
if args.Output:
    print("Displaying Output as : %s" % args.Output)
'''

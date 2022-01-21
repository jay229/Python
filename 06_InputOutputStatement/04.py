# Command Line Arguments
from sys import argv
# print("The Number of CLA :",len(argv))
# print("The list of CLAs :",argv)
# print("Command Line Arguments one by one:")
# for i in argv:
#     print(i)


# Sum of  Command Line Arguments:
sum=0
argvs=argv[1:]
for i in argvs:
    n=int(i)
    sum=sum+n
print(sum)
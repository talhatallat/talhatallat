# f = open("test-file1.txt", "w")
# f.write("Line-1 :This is the content to put in testfile2\n")
# f.write("Line-2 :This is the content to put in testfile2")
# f = open("test-file1.txt", "a")
# for i in range(1, 1001):
#     f.write(str(i)+" line 1 \n")    

# for i in range(1001, 1101):
#    f.write(str(i)+" line 2 \n")    

# f = open("test-file1.txt", "r")
# # print(f.read())
# # print(f.read(25))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# try :
#     with open("test-file-1.txt", "r") as f:
#         print("in File")
#         print(f.read())
# except Exception as e:
#     print(e)

import os 
os.remove("test-file1.txt")



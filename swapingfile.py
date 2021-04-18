def swapfiledata():

sample1 =input("enter one file name")

sample2 =input("enter other file name")

a=open(sample1,r):
data1=a.read()

b=open(sample2,r):
data2=b.read()

a=open(sample1,w):
a.write(data2)

b=open(sample2,w):
b.write(data1)

swapfiledata()
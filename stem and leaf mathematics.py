print("this is code that helps in organazing data in maths using",
      "a system called ordered stem and leaf plot")

n = int(input("no. of tens: "))
a = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],}


for i in range(0, n):
    tens = input("tens: ")
    x = int(input("no. of ones dec: "))
    for v in range(0, x):
        y = float(input('ones dec: '))
        a[tens].append(y)
        a[tens].sort()
        
    

print(a)


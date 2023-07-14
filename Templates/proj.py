import csv  
# Open file 

with open("D:\\Downloads\\cleaned.csv") as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
    l=[]
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        l.append(row)
# print(l[0])

for i in range(1,len(l)):
  name = 'D:\\Downloads\\tweet_files\\' + l[i][0] + '.txt'
  line1 = l[i][1]
  li="\n"
  line2= l[i][2]
  f1 = open(name, 'w')
  f1.write(line1)
  f1.write(li)
  f1.write(line2)
  f1.close()
import csv 
          
#make csv file and insert data
f=csv.open("student.csv",'w',newline="")
writer=csv.writer(f)
header=['sid','sname','scity','scontact']
writer.writerow(header)

rows=[[1,'vidhi','bardoli',74854521020],[2,'vruti','kamrej',7485209652],
      [3,'kishan','vyara',8745962020],[4,'Radha','bardoli',8963200745],
      [5,'ram','surat',7485203691]]
writer.writerows(rows)

for i in range(5):
    sid=int(input("Enter Student id:"))
    sname=input("Enter Student name:")
    city=input("Enter Student city:")
    contact=input("Enter Student contact:")
    row=[sid,sname,city,contact]
    writer.writerow(row)

#read records from csv file
f=open("student.csv",'r',newline="")
    
read=csv.reader(f)
head=next(read)
print("================Students Details==================") 
print(f"{head[0]}\t{head[1]}\t{head[2]}\t{head[3]}")
for r in read:
    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\n")

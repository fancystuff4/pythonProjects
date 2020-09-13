#table

table_row = ""

for i in range(1,11):
  for j in range(1, 11):
   table_row += (str(j)+"*"+str(i)+"="+str(i*j)+"\t")
  print(table_row)
  table_row = ""
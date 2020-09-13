#car numberplat according to the odd or even day
nu_plats = ['AP9091' , 'AP8082', 'AP7073' , 'AP6064' , 'AP5055' , 'AP2026']

odd_day = ['mon','wen','fri' ]
even_day=['tue','thus','satur']
pass_list=[]

day=input('type a day : ')

for plates in nu_plats:
  last_nu=int(plates[-1])
  if day in odd_day and last_nu % 2 != 0 :
    pass_list.append(plates)
  elif day in even_day and last_nu % 2 == 0 :
    pass_list.append(plates)
  elif day == "sun":
    pass_list.append(plates)
print(*sorted(pass_list) , sep = '\n')
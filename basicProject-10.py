# patients info 
def print_queue(*a_list, **a_dict):
  for person in a_list:
    for patient , info in a_dict.items():
      if person == patient :
        print(person+" :")
        for key, value in info.items():
          print(key +"="+ str(value))
        print()

patient_name=['harsh','javeed','salman','raj']
patient_info={'harsh':{'age':25, 'weigth':65},
              'raj':{'age':34, 'weigth':64},
              'salman':{'age':55, 'weigth':60}
              }

print('these are the patients in waiting list')
print_queue(*patient_name,**patient_info)
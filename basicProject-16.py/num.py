def add_elements(num_list, start_nu, end_nu):
  return sum(num_list[start_nu:start_nu+end_nu])

def get_mean(num_list, start_nu, end_nu):
  temp_list=(num_list[start_nu:start_nu+end_nu])
  total = 0 
  for i in temp_list:
    total+=i
  return total/len(temp_list)

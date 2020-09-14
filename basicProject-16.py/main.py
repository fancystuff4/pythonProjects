import text as ol
import num as hn

my_num_list=[2,3,5,2,4,5,1,7]
my_name_list=['amy', 'gloria', 'tim', 'ken', 'stephen', 'patrick', 'tim']

ol.delete_name(my_name_list,'tim')
print(my_name_list)

ol.add_name(my_name_list,"lily",2)
print(my_name_list)

my = hn.add_elements(my_num_list, 1, 5)
print(my)

ym = hn.get_mean(my_num_list, 1 ,5)
print(ym)
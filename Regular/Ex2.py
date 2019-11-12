#!/usr/bin/python3


import re


accesions='xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp'

accesions_list=accesions.split()

print(accesions_list)

for acc in accesions_list:
	print(acc)


list_to_store_outputs=[]
contain_e_or_d=[]
another_list=[]
d_e_both_letters_any_order=[]

for acc in accesions_list:
	if re.search(r'5', acc):
		list_to_store_outputs.append('contain the number 5:' + acc) 
	if re.search(r'[de]', acc): #de is used when d and e are adjacent
		contain_e_or_d.append(acc)
	if re.search(r'd.*e', acc) and re.search(r'e', acc): #contain d and e not adajcent
		another_list.append(acc)
	if re.search(r'd.e', acc):
		d_e_single_letter_between_them.append(acc)
	if re.search(r'd', acc) and re.search(r'e', acc): #contain both letters e and e in any order
		d_e_both_letters_any_order.append(acc)

print(list_to_store_outputs)
print(contain_e_or_d)
print(another_list)
print(d_e_both_letters_any_order)







# using get in  dict 

dic = {"class":10,"name":"tanish","roll no":60}
print(dic.get("class")) #gives the value of 'class' this is equivalent to ---

# print(dic['class'])

# some other features
# if the key is not present in dict it will return 'none'

print(dic.get('not in the dict')) # None

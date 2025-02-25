"""10. Write a function that merges two dictionaries into one."""
def merge(dict1,dict2):
    new_dict=dict1.copy()
    new_dict.update(dict2)
    return print(new_dict)

d1={'a':1,'b':2}
d2={'b':3,'c':4}
merge(d1,d2)
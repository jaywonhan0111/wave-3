def reverseLookup(dictionary, value):
    finding_value_keys = []
    for key,val in dictionary.items(): 
        if val == value:
            finding_value_keys.append(key)
    return finding_value_keys 

if __name__ == '__main__':

    lookup_dict = {"key1":12,"key2":25, "key3":12}
    
    multiple_key_case = reverseLookup(lookup_dict,12)
    single_key_case = reverseLookup(lookup_dict,25)
    no_key_case = reverseLookup(lookup_dict,33)

    print("multiple key case: ", multiple_key_case)
    print("single key case: ", single_key_case)
    print("no key case: ", no_key_case)
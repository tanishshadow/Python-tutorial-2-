def vowel_counter(string):
    """returns the number of vowels present in a string"""
    string=set(string)
    vow=['a','e','i','o','u']
    l=[v for v in string if v in vow]
    return len(l)


if __name__=='__main__':
    print(vowel_counter("geeksforgeeks"))

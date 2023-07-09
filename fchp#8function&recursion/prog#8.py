def remove(string , word):
    new_Str = string.replace(word , "")
    return new_Str.strip()

txt = "     this is preetam       "
n = remove(txt , "preetam")
print(n)

    

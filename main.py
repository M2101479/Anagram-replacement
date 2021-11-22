

from collections import Counter
 
def check(s1, s2):
   
    
    if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 
s1 = "python"
s2 = "typhon"
check(s1, s2)
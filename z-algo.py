def z_algo(s):
    n=len(s)
    l=r=k=0
    #l start of z box
    #r end of z box
    #k element in z box
    z=[0]*len(s)
    for i in range(1,len(s)):
        if i>r:
            #current pos outside z box
            l=r=i
            #naive check
            while r<len(s) and s[r]==s[r-l]:
                r+=1
            z[i]=r-l
            r-=1
            #z-box till last match = l-r (r+1 first miss match)
        else:
            #current pos in z box
            k=i-l
            if z[k]<r-i+1:
                #match length at z[k] is inside z-box
                z[i]=z[k]
            else:
                #match length at z[k] is = or > z-box(outside)
                l=i
                while r<len(s) and s[r]==s[r-l]:
                    r+=1
                #increase size of z-box by checking outside
                z[k]=r-l
                r-=1
    print(z)
    return z
def z_algorithm_search(text, pattern):
    concatenated = pattern + "$" + text
    z = z_algo(concatenated)
    
    
    pattern_length = len(pattern)
    occurrences = []
    for i in range(len(z)):
        if z[i] == pattern_length:
            occurrences.append(i - pattern_length - 1)
    return occurrences

print(z_algorithm_search("abcdeabcefabc","abc"))

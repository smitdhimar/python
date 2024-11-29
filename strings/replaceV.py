# write a function to replace the occurances of 3 consecutive vowels with _
def isVowel(c):
    return c=='A' or c=='E' or c=='I' or c=='O' or c=='U'        
def replaceV(str):
    ans=""
    i=0
    while(i < len(str)-2):
        if(isVowel(str[i]) and isVowel(str[i+1]) and isVowel(str[i+2])):
            ans+="_";
            i+=2
        else:
            ans+=str[i];
        i+=1;
    return ans;

print("for string AAAhelloEIOworldAIE");
print(replaceV("AAAhelloEIOworldAIE"))
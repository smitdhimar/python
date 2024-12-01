str="Birla vishvakarma mahavidyala";
newstr=" "+str;
def acronym(newstr):
    ans="";
    for i in range(0,len(newstr)):
        if(newstr[i]==' '):
            ans+=newstr[i+1].upper();
    return ans;

print(acronym(newstr))
s=input("enter a sentence:")
def count(s):
    upper_count=0
    lower_count=0
    for i in s:
        if i>='a' and i<='z':
            lower_count+=1
        elif i>='A' and i<='Z':
            upper_count+=1
        else:
            continue
    print("No. of uppercase characters:",upper_count)
    print("No. of lowercase characters:",lower_count)
count(s)
    



fhand = open("C:\\Users\\Administrator\\Desktop\\bootcamp\\Chapter8\\mails.txt")

for line in fhand:
    
    line = line.rstrip()
    
    if not line.startswith('From '):
        
        continue
    
    words = line.split()

    for word in words:
        
        adr = list()
        
        if word.endswith("com>"):
            
            adr.append(word)
            
        elif word.endswith("kr>"):
           
            adr.append(word)
            
        else:
            
            continue
        
        print(adr)



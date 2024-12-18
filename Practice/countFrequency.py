def countFrequency(str):
    count ={}
    words =str.split()
    
    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] =1
    return count
print(countFrequency("Hello python developer, are you enjoying in python internship."))
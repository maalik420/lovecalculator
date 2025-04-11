def calculate_love_score(name1, name2):
    count1 = 0
    count2 = 0
    name1_list = list(name1.lower())
    name2_list = list(name2.lower())
    name_list = name1_list + name2_list
    
    for letter1 in name_list:
        if letter1 == 't':
            count1 += 1
        elif letter1 == 'r':
            count1 += 1
        elif letter1 == 'u':
            count1 += 1
        elif letter1 == 'e' :
            count1 += 1
        
    for letter2 in name_list:
        if letter2 == 'l':
            count2 += 1
        elif letter2 == 'o':
            count2 += 1
        elif letter2 == 'v':
            count2 += 1
        elif letter2 == 'e':
            count2 += 1
            
    love_score = (count1 * 10) + count2 
    print(love_score)
        
calculate_love_score('Shahrukh', 'Gauri')

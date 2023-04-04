def romanToInt(s):
    roman_dic = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    spc_roman_dic = {'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}
    two_index_list = []
    sum=0
    for i,char in enumerate(s):
        if i != len(s)-1 and s[i]+s[i+1] in spc_roman_dic.keys():
            sum = sum + spc_roman_dic[s[i]+s[i+1]]
            two_index_list.append(i)
            two_index_list.append(i+1)
        elif i not in two_index_list:
            sum = sum + roman_dic[s[i]]   
    return sum

print(romanToInt("MCDLXXVI"))

    # if len(s)%2 == 0:    
    #     for i,char in enumerate(s):
    #         if i%2==0:
    #             two_char_list.append(s[i]+s[i+1])
    # else:
    #     two_char_list.append(s[0])
    #     for i,char in enumerate(s):
    #         if i%2!=0:
    #             two_char_list.append(s[i]+s[i+1])
    # for i in two_char_list:
    #     if i in spc_roman_dic.keys():
    #         sum = sum + spc_roman_dic[i]
    #     else:
    #         for char in i:
    #             sum = sum + roman_dic[char]
    # return sum


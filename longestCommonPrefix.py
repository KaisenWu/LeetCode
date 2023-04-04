# def longestCommonPrefix(strs):
    # if(len(strs) == 1):
    #     prefix = strs[0]
    # elif(len(strs) == 2):
    #     prefix = ""
    #     if len(strs[0]) <= len(strs[1]):
    #         for i,char in enumerate(strs[0]):
    #             if char == strs[1][i]:
    #                 prefix = prefix + char
    #             else:
    #                 break
    #     else:
    #         for i,char in enumerate(strs[1]):
    #             if char == strs[0][i]:
    #                 prefix = prefix + char
    #             else:
    #                 break
    # else:
    #     prefix = ""
    #     if len(strs[0]) <= len(strs[1]):
    #         for i,char in enumerate(strs[0]):
    #             if char == strs[1][i]:
    #                 prefix = prefix + char
    #             else:
    #                 break
    #     else:
    #         for i,char in enumerate(strs[1]):
    #             if char == strs[0][i]:
    #                 prefix = prefix + char
    #             else:
    #                 break
    #     for i in range(2,len(strs)):
    #         cmp_str = ""
    #         if len(prefix) <= len(strs[i]):
    #             for j,char in enumerate(prefix):
    #                 if char == strs[i][j]:
    #                     cmp_str = cmp_str + char
    #                 else:
    #                     break
    #             prefix = cmp_str
    #         else:
    #             for j,char in enumerate(strs[i]):
    #                 if char == prefix[j]:
    #                     cmp_str = cmp_str + char
    #                 else:
    #                     break
    #             prefix = cmp_str
    # return prefix

def longestCommonPrefix(strs):
    prefix = ""
    for i in range(len(strs[0])):
        cnt=0
        for j in range(1,len(strs)):
            if i>=len(strs[j]) or strs[0][i] != strs[j][i]:
                break
            cnt += 1
        if cnt == len(strs)-1:
            prefix += strs[0][i]
        else:
            break
    return prefix



print(longestCommonPrefix(["cir","car"]))
# ["flower","flow","flight"]
# ["dog","racecar","car"]
        
def all_uniq_sub(s):

    if not s:
        return None

    start = 0
    end = 1

    longest_str = s[0]
    my_list = []
    temp_str = longest_str
    my_list.append(longest_str)
    while end < len(s):
        if s[end] not in temp_str:
            temp_str = temp_str + s[end]
            end += 1
        else:
            if temp_str > longest_str:
                longest_str = temp_str
                temp_str = s[end]
                start = end
                end += 1

    if len(temp_str) > len(longest_str):
        return temp_str
    else:
        return longest_str

s = 'abacbdadbc'
print all_uniq_sub(s)
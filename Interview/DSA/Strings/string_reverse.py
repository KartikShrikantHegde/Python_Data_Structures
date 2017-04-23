def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

#
# def my_reverse(s):
#     i = 0
#     j = len(s) - 1
#
#     for ch in s:
#
#     while i < j:
#         s[i],s[j] = s[j], s[i]
#         i += 1
#         j -= 1
#
#     return s

print reverse("Hello")
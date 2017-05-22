# # def  find_sum_and_avg(ints):
# #     if not ints:
# #         return 0,0
# #     sum = 0
# #     avg = 0
# #     count = 0
# #     for i in range(0,len(ints),2):
# #         sum = sum + ints[i]
# #         count = count + 1
# #     avg = sum / count
# #     return sum,avg
# #
# #
# #
# # print find_sum_and_avg(ints=[1,2])
#
#
#
#
# # def remove_n_duplicates(n, int_array):
# #     from collections import Counter
# #     for k, v in Counter(int_array).items():
# #         if v == n:
# #             while v != 0:
# #                 int_array.remove(k)
# #                 v -= 1
# #
# #     return sorted(int_array)
# #
# # print remove_n_duplicates(n=3,int_array=[4,4,4,3,2,1,1])
#
#
# # def isPossiblePath(a,b,p,q,N):
# #     # (A,B) Horizontal end-to-end check
# #     if abs(a[1] - b[1]) == N-1:
# #         if p[0] < a[0] < q[0] or p[0] > a[0] > q[0] or p[0] < b[0] < q[0] or p[0] > b[0] > q[0]:
# #             return False
# #     # (A,B) Vertical end-to-end check
# #     elif abs(a[0] - b[0]) == N-1:
# #         if p[1] < a[1] < q[1] or p[1] > a[1] > q[1] or p[1] < b[1] < q[1] or p[1] > b[1] > q[1]:
# #             return False
# #
# #     # (P,Q) Horizontal end-to-end check
# #     if abs(p[1] - q[1]) == N-1:
# #         if a[0] < p[0] < b[0] or a[0] > p[0] > b[0] or a[0] < q[0] < b[0] or a[0] > q[0] > b[0]:
# #             return False
# #     # (P,Q) Vertical end-to-end check
# #     elif abs(p[0] - q[0]) == N-1:
# #         if a[1] < p[1] < b[1] or a[1] > p[1] > b[1] or a[1] < q[1] < b[1] or a[1] > q[1] > b[1]:
# #             return False
# #
# #     return True
# #
# #
# #
# # def main():
# #
# #     if _name_ == '_main_':
# #         a = (1,0)
# #         b = (1,4)
# #         q = (0,2)
# #         p = (4,2)
# #         N = 5
# #         print (isPossiblePath(a,b,p,q,N))
#
#
# # def  get_second_most_freq(the_list):
# #     from collections import Counter
# #     x = Counter(the_list)
# #     print x.most_common(2)[1]
# #     second_most_common_value, its_frequency =  x.most_common(2)[1]
# #     return second_most_common_value
# #
# #
# # print get_second_most_freq(the_list=[0,1,1,2,3,2,2,2,2])
#
#
# # def  find_two_closest_and_sum(int_list, target_num):
# #     least_dif = 0
# #     x = sorted(int_list)
# #     my_list = []
# #     for i in range(0,len(int_list)):
# #
# #
# #
# # print find_two_closest_and_sum(int_list=[21,6,27,18],target_num=15)
#
#
# import sys
# def find_closese_sum(int_list, target_num):
#     start = 0
#     end = len(int_list) - 1
#     result = sys.maxint
#     result_tuple = None
#     while start < end:
#         if int_list[start] + int_list[end] == target_num:
#             return
#         elif int_list[start] + int_list[end] > target_num:
#             if abs(int_list[start] + int_list[end] - target_num) < result:
#                 result = abs(int_list[start] + int_list[end] - target_num)
#                 result_tuple = (int_list[start], int_list[end])
#             end -= 1
#         else:
#             if abs(int_list[start] + int_list[end] - target_num) < result:
#                 result = abs(int_list[start] + int_list[end] - target_num)
#                 result_tuple = (int_list[start], int_list[end])
#             start += 1
#
#     return int(sum(result_tuple))
#
# if __name__ == "__main__":
#     int_list = [21,6,27,18]
#
#     target_num = 15
#
#     int_list = sorted(int_list)
#     print find_closese_sum(int_list, target_num)


# def find_two_closest_and_sum(int_list, target_num):
#     import sys
#     import math
#     n = len(int_list)
#
#     l = 0
#     r = n - 1
#     diff = sys.maxint
#
#     while (r > l):
#         res_l = 0
#         res_r = 0
#         if math.fabs((int_list[l] + int_list[r] - target_num) < diff):
#             res_l = l
#             res_r = r
#             diff = math.fabs(int_list[l] + int_list[r] - target_num)
#
#         if (int_list[l] + int_list[r]) > target_num:
#             r -= 1
#         else:
#             l += 1
#
#     return int_list[l] + int_list[r]
#
# print find_two_closest_and_sum(int_list=[21,6,27,18],target_num=15)

# print set([4, 4, 4])


# def validate_pin(pin):
#     # return true or false
#     my_no = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     if len(pin) == 4 or len(pin) == 6:
#         for ch in pin:
#             if ch in my_no:
#                 continue
#             else:
#                 return False
#     else:
#         return False
#
#     return True
#
# print validate_pin("1234")

# def solution(E,L):
#     entry = E.split(":")
#     exit = L.split(":")
#     entry = float('.'.join(entry))
#     exit = float('.'.join(exit))
#     diff = exit - entry
#     diff = str(diff)
#     diff = diff.split(".")
#     first_part = int(diff[0])
#     second_part = int(diff[1])
#     total = 2
#     if first_part < 1:
#         total += 3
#     elif first_part >= 1 and first_part < 2 and second_part == 0:
#         total += 3
#     elif first_part >= 1 and first_part < 2 and second_part > 0:
#         total += 7
#     elif first_part >= 2 and second_part == 0:
#         total += 3 + ((first_part - 1)* 4)
#     else:
#         total += 3 + ((first_part - 1)* 4) + 4
#
#     return total
#
#
# E = "10:00"
# L = "15:21"
# print solution(E,L)

def solution(A, B, M, X, Y):
    # write your code in Python 2.7

    if not A:
        return 0
    current_sum = 0
    a = []
    counter_a = 0
    counter_m = 0
    ele = 0

    while counter_a < len(A):
        max_people = 0
        for i in range(len(A)):
            if counter_a >= len(A):
                break

            current_sum += A[counter_a]
            if current_sum < 200 and max_people < X:
                counter_a += 1
                max_people += 1
            else:
                current_sum = 0
                break

        for counter_b in range(counter_a):
            if counter_m >= len(B):
                break
            if B[counter_m] not in a:
                ele += 1
                a.append(B[counter_m])
            counter_m += 1

        a = []
        ele += 1

    return ele


# A = [60,80,40]
# B = [2,3,5]
# M = 5
# X = 2
# Y = 200

A = [40,40,100,80,20]
B = [3,3,2,2,3]
M = 3
X = 5
Y = 200

print solution(A,B,M,X,Y)
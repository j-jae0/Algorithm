def solution(num_list):
    even = sum([n for i, n in enumerate(num_list) if i%2==0])
    odd = sum([n for i, n in enumerate(num_list) if i%2!=0])
    return even if even >= odd else odd
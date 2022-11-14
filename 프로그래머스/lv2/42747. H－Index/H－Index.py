def solution(citations):

    for i , c in enumerate(sorted(citations, reverse=True)):
        if i >= c:
            return i
        
    return len(citations)
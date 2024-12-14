def solution(sequence, k):
    result = [0,0]
    start, end = 1, 1
    for i in range(1,len(sequence)):
        sequence[i] = sequence[i] + sequence[i-1]
    sequence.insert(0,0)
    short_len=1000001
    
    while start<=end:
        if(1 <= start and i < len(sequence) and 1 <= end and end < len(sequence)):
            Sum = sequence[end] - sequence[start-1]
            if Sum > k:
                start += 1
            elif Sum < k:
      	        end += 1
            else:
                if(short_len>end-start):
                    short_len=end-start
                    result[0]=start-1
                    result[1]=end-1
                end+=1
        
        else:
            break
            
    return result
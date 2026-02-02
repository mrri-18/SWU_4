def solution(arr):
    answer = [0]*2

    def compress(r, c, n):
            num=arr[r][c]
            for i in range(r,r+n):
                for j in range(c,c+n):
                    if arr[i][j]!=num:
                        compress(r,c,n//2) #영역 나누기, 현재 위치에서 나누는 것 (x)
                        compress(r,c+n//2,n//2)
                        compress(r+n//2,c,n//2)
                        compress(r+n//2,c+n//2,n//2)
                        return 
            answer[num]+=1

    compress(0, 0, len(arr))
    return answer
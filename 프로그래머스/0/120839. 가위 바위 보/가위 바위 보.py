def solution(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    rsp=list(rsp)
    for i in range(len(rsp)):
        rsp[i]=d[rsp[i]]
        
    return ''.join(rsp)
        
        
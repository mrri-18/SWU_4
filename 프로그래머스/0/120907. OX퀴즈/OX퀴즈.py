def solution(quiz):
    result=[]
    for i in quiz:
        tmp=i.split()
        if (tmp[1]=='+' and int(tmp[0])+int(tmp[2])==int(tmp[4])) or tmp[1]=='-' and int(tmp[0])-int(tmp[2])==int(tmp[4]):
            result.append('O')
        else:
            result.append('X')
    return result
            
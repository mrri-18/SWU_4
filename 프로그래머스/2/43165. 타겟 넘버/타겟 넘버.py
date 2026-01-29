def solution(numbers, target):
    calc=[(0,0)]
    count=0
    while calc:
        num, index=calc.pop()
        if index<len(numbers):
            calc.append((num+numbers[index], index+1))
            calc.append((num-numbers[index], index+1))
        else:
            if num==target:
                count+=1
    return count
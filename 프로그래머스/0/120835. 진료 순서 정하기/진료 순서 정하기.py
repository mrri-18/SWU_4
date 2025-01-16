def solution(emergency):
    sorted_list = sorted(emergency,reverse=True)
    sorted_dict={sorted_list.index(i)+1:i for i in emergency}
    
    return list(sorted_dict.keys())
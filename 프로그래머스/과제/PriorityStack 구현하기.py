
class PriorityStack:
    def init(self):
        self.stack = []
        self.prior = []

    def push(self, data, is_priority=False):
        if is_priority == False: 
            self.stack.append(data)
        else:
            self.stack.append(data)
            self.prior.append(len(self.stack) - 1)

    def pop(self):
        if len(self.stack) == 0:
            return None
        if len(self.prior) > 0 and self.prior[-1] + 1 == len(self.stack): #최근 삽입된 스택이 우선순위 스택인 경우
            self.prior.pop()
        return self.stack.pop()
    
    def pop_priority(self):
        if len(self.prior) == 0:
            return None
        idx = self.prior.pop()
        del self.stack[idx + 1:]
        return self.stack.pop()

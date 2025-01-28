class Calculator:
    def __init__(self):
        self.result = 0

    def _add(self, a, b):
        self.result = a + b
        return self.result
    
    def _sub(self, a, b):
        self.result = a - b
        return self.result
    
    def _mul(self, a, b):
        self.result = a * b
        return self.result
    
    def _div(self, a, b):
        if b == 0:
            raise ValueError("Division by 0 NOT supported")
        self.result = a / b
        return self.result
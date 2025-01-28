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
        self.result = a / b
        return self.result
class Clock:
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
    
    def __str__(self):
        h = str(self.h)
        if len(h) == 1:
            h = "0" + h
        m = str(self.m)
        if len(m) == 1:
            m = "0" + m
        s = str(self.s)
        if len(s) == 1:
            s = "0" + s
        
        res = h + ":" + m + ":" + s
        return res
    
    def tick(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
                if self.h == 24:
                    self.h = 0
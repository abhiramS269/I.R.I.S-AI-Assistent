from threading import Thread

class Missing:
    def __init__(self,inp:list,func:list) -> None:
        self.func=func
        
        self.input=inp
        self.TmpVal=None
    
    def run(self,funcs,inp):
        self.TmpVal=funcs(inp)

    def Start(self):
        for indx,fun in enumerate(self.func):
            Thread(target=self.run,args=[fun,self.input[indx]]).start()
        while 1:
            if self.TmpVal!=None:
                return self.TmpVal

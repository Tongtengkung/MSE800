class Singleton:                    
 
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
           
        return cls._instance
       
 
a = Singleton()
b = Singleton()
 
print(id(a), id(b))
from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    

    @process.register(int)
    @process.register(float)
    def process_float(data) -> float:
        return data * 2
    
    @process.register(str)
    def process_str(data)-> str:
        return data.upper()
    
    @process.register(list)
    def process_list(data)-> list:
        return sorted(data)
    
    @process.register(tuple)
    def process_tuple(data)-> tuple:
        return tuple(sorted(data))

p = Processor()
print(p.process(4))

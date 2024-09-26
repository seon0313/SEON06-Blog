from module.API import API

def getApis():
    modules: dict = {}
    
    modules['test'] = API()

    return modules
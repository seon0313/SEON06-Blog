import json

class API:
    def __init__(self) -> None:
        self.api_name: str = 'Test'
        self.version: str = '1.0'
        self.user: API_User = API_User('seon0313', 'seon06.dev@gmail.com', '', 17)
    
    def run(self, args: dict) -> dict:
        return args
    
    def getInfo(self) -> str:
        return {'name': self.api_name, 'version': self.version, 'author': self.user.returnJson()}

class API_User:
    def __init__(self, name: str, email: str, number: str, age: int) -> None:
        self.name: str = name
        self.email: str = email
        self.number: str = number
        self.age: int = age
    
    def returnJson(self) -> dict:
        return {'name': self.name, 'email': self.email, 'number': self.number, 'age': self.age}
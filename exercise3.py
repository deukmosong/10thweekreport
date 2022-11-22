class BankAccount:
    
    def __init__(self,name,accountnum):
        self.__name=name
        self.__account_num=accountnum
        self.__balance=0
    def __str__(self):
        return self.__name+'님의 계좌'+self.__account_num +'의 잔고는 '+ str(self.__balance) +'원입니다'
    def get_name(self):
        return self.__name
    def get_accountnum(self):
        return self.__account_num
    def get_balance(self):
        return self.__balance
    def deposit(self,money):
        self.__balance+=money
    def withdraw(self,money):
        if self.__balance-money<0:
            print('계좌 잔고는',self.__balance,'원으로 인출요구 금액',money,'보다 작습니다')
        else :
            self.__balance-=money
        
account1=BankAccount('홍길동','1234-0001')
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)
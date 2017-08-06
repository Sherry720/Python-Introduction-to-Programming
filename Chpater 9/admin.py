from user import User
class Admin(User):
    def _int_(self,first_name,last_name,age,heart):
        super()._init_(first_name,last_name,age,heart)
        self.privileages = []   # 254行得放类的下面
    def show_privileages(self):
        for privileage in self.privileages:
            print("Admin can :" +
                  "\n-" +
                  privileage
                  )

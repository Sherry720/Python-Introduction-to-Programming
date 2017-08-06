class User():
    def __init__(self,first_name,last_name,age,heart):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.heart = heart
       self.login_attempts = 0
    def increase_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("The full name is:\n" +
            "-" +
            self.first_name.title() +
            " " + 
            self.last_name.title() +
            "." 
            )
        exs = [self.age,self.heart]
        for i in exs[:]:
            print("The " +
                  self.first_name.title() +
                  " " +
                  self.last_name.title() +
                  " is:\n" +
                  i
                  ) 
    def great_user(self):
        print("Hello," +
              self.first_name.title() +
                  " " +
                  self.last_name.title()
                  )




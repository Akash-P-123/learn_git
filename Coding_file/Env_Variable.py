# In Terminal If we save a Env Var such as export password = "123" we can use the password without mention in the screen by env variable
import os
print(os.getenv("password"))
#Here the password is a name of the env 

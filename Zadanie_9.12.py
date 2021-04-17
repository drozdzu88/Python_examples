from user import User 
from user_a import Privileges, Admin

user_1 = Admin('jan', 'kowalski', 'jkow', 'male', 40)
user_1.describe_user()
user_1.privileges.show_privileges()
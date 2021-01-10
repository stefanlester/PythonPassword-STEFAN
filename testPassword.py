import unittest
from Password import passwordTester as Password
from User import User

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.password = '123_x&5s'.encode()

    def test_user(self):
        User.set_name(self, name = "Stefan")
        response = User.get_name(self)
        self.assertTrue(response, "Stefan")

    def test_hash_password_hash_check(self):
        hashed_pwd = Password.hash_password(self.password)
        self.assertTrue(Password.hash_check(self.password, hashed_pwd), (True))


if __name__ == '__main__':
    unittest.main()
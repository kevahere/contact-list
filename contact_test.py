import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    """
    defines test cases for the contact class behaviours
    """
    def setUp(self):
        self.new_contact = Contact("Kevin","Ahere","0712345678","kevahere@gmail.com")


    def test_init(self):
        self.assertEqual(self.new_contact.first_name,"Kevin")
        self.assertEqual(self.new_contact.last_name, "Ahere")
        self.assertEqual(self.new_contact.number, "0712345678")
        self.assertEqual(self.new_contact.email, "kevahere@gmail.com")

if __name__== '__main__':
    unittest.main()
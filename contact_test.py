import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    """
    defines test cases for the contact class behaviours
    """
    def setUp(self):
        self.new_contact = Contact("Kevin","Ahere","0712345678","kevahere@gmail.com")

    def tearDown(self):
        """
        teardown that does clean up after each test case has run
        :return:
        """
        Contact.contact_list=[]

    def test_init(self):
        self.assertEqual(self.new_contact.first_name,"Kevin")
        self.assertEqual(self.new_contact.last_name, "Ahere")
        self.assertEqual(self.new_contact.number, "0712345678")
        self.assertEqual(self.new_contact.email, "kevahere@gmail.com")


    def test_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","User","123456","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "123456", "test@user.com")
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "123456", "test@user.com")
        test_contact.save_contact()
        found_contact = Contact.find_by_number("123456")
        self.assertEqual(found_contact.email,test_contact.email)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "User", "123456", "test@user.com")
        test_contact.save_contact()

        contact_exists = Contact.contact_exists("123456")
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        """
        Returns a list of all added contacts
        :return:
        """
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)




if __name__== '__main__':
    unittest.main()
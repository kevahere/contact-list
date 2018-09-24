class Contact:
    """
    Class that generates new class of contact
    """
    contact_list=[]

    def __init__(self,first_name,last_name,number,email):

        #removed docstring
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def save_contact(self):
        """
        Saves new contacts
        :return:
        """
        Contact.contact_list.append(self)

    def delete_contact(self):
        """
        Deleting contacts
        :return:
        """
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        """
        takes in a number and returns a  contact matching that number
        :param number:
        :return:
        """
        for contact in cls.contact_list:
            if contact.number == number:
                return contact

    @classmethod
    def contact_exists(cls,number):
        for contact in cls.contact_list:
            if contact.number == number:
                return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        :return:
        '''
        return cls.contact_list

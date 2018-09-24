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



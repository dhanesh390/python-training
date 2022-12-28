class Users:

    def __init__(self, user_id, user_name, contact_number, email_id, password, role):
        self.user_id = user_id
        self.user_name = user_name
        self.contact_number = contact_number
        self.email_id = email_id
        self.__password = password
        self.__role = role

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role


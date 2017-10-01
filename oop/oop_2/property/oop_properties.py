'''
property is the pythonic mechanism to 
implementing encapsulation and the interface
 to interact with private attributes of an object
 '''

class Email:

     #property
    def __init__(self, address):
         self._email = address #a private attribute

    def _set_email(self, value):
        if '@' not in value:
            print("not a valid mail address")
        else:
            self._email = value
    
    def _get_email(self):
        return self._email
    
    def _del_email(self):
        print("erasing mail...")
        del self._email

    #these interface provide the public attribut email
    email  = property(_get_email, _set_email, _del_email,
    "this property contains the email")
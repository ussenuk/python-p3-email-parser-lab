# your code goes here!
# given a string of email adresses parses that string into an array

import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        # split on the comma separation
        target_string = self.email_addresses
        myre = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(myre, target_string):
            target_string = re.findall(myre, target_string)
            # print(target_string)

            joint_target_string = ' '.join(target_string)

            print(joint_target_string)

            email_list = re.split(r"\,|\s", joint_target_string)
            unique_email = set(email_list)

            # transform the dict to list
            unique_list_email = list(unique_email)

        

            sorted_unique_email= sorted(unique_list_email)


            return sorted_unique_email



parser = EmailAddressParser("talk@talk.com,john.jones@flatironschool.com,alexa@amazon.com")   
parser.parse()

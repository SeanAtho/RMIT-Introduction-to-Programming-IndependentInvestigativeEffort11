class PasswordManager:
    def __init__(self,password_filename):
        #List is used to store all passwords. Possible Alternative names
        #could be “all_passwords”.
        self.__passwords=[]
        self.__password_filename=password_filename
        #Variable is created with a null value to store passwords object file.
        pf=None
        #Below code block will open a file object via the file name, in the event
        #an error occurs then the file is saved as blank.
        try:
            pf=open(self.__password_filename)
        except:
            self.save_to_file()
        #Below code block the file lines are read if they aren't a empty string.
        #All the lines into a a field by a comma with one field for each of the atrributes.
        if(pf!=None):
            #Variable is created and used to read a line from the file as specified
            #by the user.
            line = pf.readline()
            while(line !=""):
                fields = line.strip().split(",")
                self.add_password(fields[0], fields[1], fields[2])
                line = pf.readline()
            pf.close()

    #The below methods purpose is to check the length of the list.
    def get_password_count(self):
        return len(self.__passwords)

    #A instance method is created to add logins to the password manager. This is done by passing the arguments
    #for each of the object attributes and then having them appended to the list through invoking the class.
    def add_password(self,site,username,password):
        password_permit=False
        try:
            self.__passwords.append(Password(site,username,password))
            password_permit=True
        except:
            password_permit=False
        return password_permit
    
    #When password lengths and record positions dont match the input from the user the below code block and method will
    #iterate only once if the record positions is less than the total length of the list, with the record in question returned.
    def get_password(self,site,username,password):
        located_password=None
        len_passwords=self.get_password_count()
        i=0
        while(i<len_passwords and self.__passwords[i].is_equals(site,username,password) == False):
            i+=1
        if (i < len_passwords):
            located_password=self.__passwords[i]
        return located_password

    def edit_password(self,site,username,password,new_password):
        completed = False
        password_selected_change = self.get_password(site,username,password)
        if (password_selected_change !=None):
            password_selected_change.password = new_password
            completed = True
        return completed

    #The method removes the sensitive credentials from the password list. However, the username, site,
    #and password must be correct for the successful removal of the data.
    def remove_password(self,site,username,password): 
        completed = False
        password_for_removal = self.get_password(site,username,password)
        if(password_for_removal!=None):
           del password_for_removal

    #Method saves all data and changes made during "add_password" method and "remove_password" method to .csv file.
    def save_to_file(self):
        pf=open(self.__password_filename,"w")
        pf.write(str(self))
        pf.close()

    #Method displays passwords contained within .csv file upon launch of application by user.
    def __str__(self):
        len_passwords=self.get_password_count() 
        summary=""
        i=0
        while(i<len_passwords):
            summary+= str(self.__password[i])+"\n"
            i+=1
        return summary 
            
class Password():
    #Below code block initialises the password attributes and makes them private.
    def __init__(self,site,username,password):
        self.__site=None
        if(len(site>=2)):
            self.__site=site
        else:
            raise ValueError("Site or application name must be at least 2 characters in length. ")
        
        self.__username=None
        if(len(username>=4)):
            self.__username=username
        else:
            raise ValueError("Username must be at least 4 characters in length. ")

        self.__password=None
        if(len(password>=8)):
            self.__password=password
        else:
            raise ValueError("Password must be at least 8 characters in length. ")

    #Initialises the mutator and accessor methods for the site, username, and password attributes preventing them
    #from being changed and altered.
    #Mutator method has been created to check for password minimum length.
    @property
    def site(self):
        return self.__site

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        if(len(value)>=8):
            self.__password = value
        else:
            raise ValueError("Could not be added. Password must be at least 8 characters in length. ")
        self.__password=password

    #Instance method for removal of data in csv file.
    def is_equals(self,site,username,password):
        outcome=False
        if (self__site==site and self.__username==username and self.__password==password):
            outcome=True
        return outcome

    #Instance method to return summary of data.
    def __str__(self):
        summary=self.__site+","
        summary+=self.__username+","
        summary+=self.__password
        return summary

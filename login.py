import sys
from loger import file_logger
import pandas as pd
import hashlib
import csv
from colorama import Fore


class User:
    def __init__(self, username, password, role):
        """

        """
        self.password = password
        self.username = username
        self.role = role

def register():
    """
    This method is written to register user on site
    Sign up and save in CSV file

    :return:
    """
    try:
        file_path = "account.csv"
        def_account = pd.read_csv(file_path)
        username = input("enter your username")
        password = input("enter your password")
        lst_username = list(def_account["username"])
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        lst_password = list(def_account["password"])
        if username in lst_username and hash_password in lst_password:
            print(Fore.WHITE+"You have already signed up")
            sys.exit()
        else:
            obj_user = User(username, hash_password, role='role')
            row_account = [[obj_user.username, obj_user.password]]
            with open(file_path, 'a', newline='') as csv_account:
                csv_writer = csv.writer(csv_account)
                # writing the data row
                csv_writer.writerows(row_account)
                def_account.replace(to_replace=def_account['username'].values, value=-1, inplace=True)
        print(Fore.RED+"                            #################Registration successfully completed##################\n")
        file_logger.info("register")
    except Exception:
        print("There has been a problem in your registration process please re-try")


def log_in():
    """
    This method is stored for the logging of the
     user and the admin that has already been registered and the
     user half and their forefront are stored in our file.
    :return:
    """
    i = 0
    b = 0
    while i < 3:
        file_path = "account.csv"
        def_account = pd.read_csv(file_path)
        lst_username = list(def_account["username"])
        while b < 3:
            try:
                username = input("enter your username")
                if username in lst_username:
                    print(Fore.GREEN+"                       *********************************valid username**********************************************\n")
                    b = 3
                else:
                    print(Fore.RED+"The username entered is wrong again")
                    b += 1
            except Exception:
                print(Fore.RED+"The username entered is wrong again")
                b += 1
        try:
            password = input(Fore.YELLOW+"enter your password")
            hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
            if def_account.iloc[def_account.index[def_account['username'] == username].tolist()[0], 1] == hash_password:
                print(Fore.CYAN+"                     ****************************************HELLO", username,"*****************************************\n")
                file_logger.info("login ok")
                i = 3
            else:
                print(Fore.RED+"The password entered is wrong again")
                i += 1
        except Exception:
            print(Fore.RED+"The password entered is wrong again")
            i += 1

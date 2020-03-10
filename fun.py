import local
import os

#Funkcja sprawdza hasło i login użytkownika, ustawia który to użytkownik w pliku user.txt
#w pliku zapis wygląda tak:
'''
login
hasło
identyfikator użytkownika
typ użytkownika
login 2
hasło 2
identyfikator użytkownika 2
typ użytkownika 2
...
'''
def log():
    plik = open("logins and passwords.txt", "r").read()
    lines = plik.split("\n")
    login = input("Podaj login: ")
    password = input("Podaj haslo: ")
    user = 0

    for i in range(len(lines)):
        if (login == lines[i]):
            i += 1
            if(password == lines[i]):
                i+=1
                print("zalogowano na", lines[i])
                i += 1
                user = lines[i]
                user_ = open("user.txt", "w")
                user_.write(user)
                user_.close()
                user = 1


    if (user == 0):
        print("nieprawidłowy login lub hasło")
        log()

#Funkcja zwraca typ użytkownika
#możliwe wyniki: student , teacher , admin
def user_type():
    plik = open("user.txt", "r").read()
    return (plik)

#Funkcja zapisuje login, hasło, imię i nazwisko nowego ucznia do pliku logins and passwords.txt a także jego godność do lokalnej tablicy w pliku local.py
def add_student():
    logowanie = open("logins and passwords.txt", "a")
    name = input("Podaj imię i nazwisko ucznia: ")
    login = input("Podaj login dla ucznia: ")
    password = input("Podaj haslo dla ucznia: ")


    #logins and passwords
    logowanie.write(login)
    logowanie.write("\n")
    logowanie.write(password)
    logowanie.write("\n")
    logowanie.write(name)
    logowanie.write("\n")
    logowanie.write("student")
    logowanie.write("\n")
    logowanie.write("\n")
    logowanie.close()


    #local
    source = open("local.py").readlines()
    goal = open("local.py", "w")
    for i in source:
        goal.write(i.replace("]", " "))
    goal.close()
    source = open("local.py", "a")
    source.write("\n")
    source.write(" ")
    source.write("'")
    source.write(name)
    source.write("'")
    source.write(",")
    source.write("]")
    source.close()


    #folder
    def folder():
        class_ = int(input("Podaj numer klasy (1 - 3): "))
        if (class_ == 1):
            klasa1_dir = '/klasy/1'

            try:
                path4 = os.path.join(klasa1_dir, name)
                os.mkdir(path4)
            except OSError:
                print("Błąd przy tworzeniu podfolderu ucznia")
            else:
                pass

        elif (class_ == 2):
            klasa2_dir = '/klasy/2'

            try:
                path5 = os.path.join(klasa2_dir, name)
                os.mkdir(path5)
            except OSError:
                print("Błąd przy tworzeniu podfolderu ucznia")
            else:
                pass

        elif (class_ == 3):
            klasa3_dir = '/klasy/3'

            try:
                path6 = os.path.join(klasa3_dir, name)
                os.mkdir(path6)
            except OSError:
                print("Błąd przy tworzeniu podfolderu ucznia")
            else:
                pass

        else:
            print ("Nieprawidłowy numer klasy")
            folder()
    folder()

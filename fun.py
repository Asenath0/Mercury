import local

#Funkcja sprawdza hasło i login użytkownika, ustawia który to użytkownik w pliku user.txt
#w pliku zapis wygląda tak:
'''
(login)
(hasło)
(identyfikator użytkownika)
(login 2)
(hasło 2)
(identyfikator użytkownika 2)
'''
def log():
    plik = open("logins and passwords.txt", "r").read()
    lines = plik.split("\n")
    login = str(input("Podaj login: "))
    password = str(input("Podaj haslo: "))

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


    if (user == 0):
        print("nieprawidłowy login lub hasło")
        log()

#Funkcja zwraca typ użytkownika
#możliwe wyniki: student , teacher , admin
def user_type():
    plik = open("user.txt", "r").read()
    pliks = plik.split("\n")
    for i in pliks:
        return (i)

#Funkcja zapisuje login, hasło, imię i nazwisko nowego ucznia do pliku logins and passwords.txt a także jego godność do lokalnej tablicy w pliku local.py
def add_student():
    logowanie = open("logins and passwords.txt", "a")
    name = str(input("Podaj imię i nazwisko ucznia: "))
    login = str(input("Podaj login dla ucznia: "))
    password = str(input("Podaj haslo dla ucznia: "))

    logowanie.write(login)
    logowanie.write("\n")
    logowanie.write(password)
    logowanie.write("\n")
    logowanie.write(name)
    logowanie.write("\n")
    logowanie.write("student")
    logowanie.write("\n")
    logowanie.close()

    source = open("local.py").readlines()
    goal = open("local.py", "w")
    for i in source:
        goal.write(i.replace("]", " ,"))
    goal.close()
    source = open("local.py", "a")
    source.write("'")
    source.write(name)
    source.write("'")
    source.write("\n")
    source.write("]")



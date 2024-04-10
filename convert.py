def int2hex(num):
    hex = format(int(num), 'x')
    return hex

def int2bin(num):
    bin = format(int(num), 'b')
    return bin




def display_menu2():
    print("Jakie przeliczenie:")
    print("1. dwójkowy")
    print("2. szesnastkowy")
    print("3. nowa liczba")
    print("4. Wyjście")
    print()

def main():
    
        
    
    
            
            while True:
                try:
                    num = input('Podaj numer do konwersji z zakresu (0-255):')
                    if not num:
                        raise ValueError("Nie podano numeru")
                    num = int(num)
                    if num < 0 or num > 255:
                        raise ValueError("Numer poza zakresem (0-255)")
                    break  
                except ValueError as e:
                    print(e)  
            while True:
                display_menu2()
                choice2 = input("Wybierz opcję: ") 
                if choice2 == "1":
                    bin = int2bin(num)
                    print(bin)
                elif choice2 == "2":
                    hex = int2hex(num)
                    print(hex)
                elif choice2 == "3":
                    while True:
                        try:
                            num = input('Podaj numer do konwersji:  z zakresu (0-255)')
                            if not num:
                                raise ValueError("Nie podano numeru.")
                            num = int(num)
                            if num < 0 or num > 255:
                                raise ValueError("Numer poza zakresem (0-255)")
                            break  
                        except ValueError as e:
                            print(e)  
                elif choice2 == "4":
                    print("Do widzenia!")
                    break
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")
        


main()
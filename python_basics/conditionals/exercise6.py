weather = input("What's the weather like today? ")

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'snowy':
        print("It's gonna be cold.")
    case _:
        print("Let's stay inside.")
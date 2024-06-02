def greet(iso_code):
    match iso_code:
        case 'en':
            return('Hi!')
        case 'fr':
            return('Salut!')
        case 'pt':
            return('Olá!')
        case 'es':
            return('Hola!')
        case 'de':
            return('Hallo!')
        case 'sv':
            return('Hej!')
        case 'af':
            return('Haai!')

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('es'))         # Hola!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
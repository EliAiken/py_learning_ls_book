# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True
print('Butter' in cats)             # False; must match list/tuple element exactly
                                    # 'Butter' is not an element in the tuple above
print('Butter' in cats[3])          # True
print('cheddar' in cats)            # False
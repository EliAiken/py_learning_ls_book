sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")


# Will print $3.99 because sale is True, but the function states `not sale`
# making it a false statement and thus 3.99 will print
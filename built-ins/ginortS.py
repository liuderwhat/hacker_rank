string = input()

alpha = [c for c in string if c.isalpha()]
digit = [c for c in string if c.isdigit()]
al_low = [c for c in alpha if c.islower()]
al_upp = [c for c in alpha if c.isupper()]
digit_even = [c for c in digit if not(int(c) % 2)]
digit_odd = [c for c in digit if int(c) % 2]

al_low_j = ''.join(sorted(al_low))
al_upp_j = ''.join(sorted(al_upp))
digit_even_j = ''.join(sorted(digit_even))
digit_odd_j = ''.join(sorted(digit_odd))

print(al_low_j + al_upp_j + digit_odd_j +digit_even_j )

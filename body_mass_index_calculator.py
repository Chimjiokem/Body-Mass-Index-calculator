name = input('Enter your name: ')
weight = int(input(f'Your  weight in kilograms is: '))
if weight <= 0:
    print('Error! Invalid value entered!')
height = float(input(f'Your  height in meters is: '))
if height <= 0:
    print('Error! Invalid value entered!')

body_mass_index = weight/height**2
if body_mass_index < 18.5:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nYou are underweight')
elif body_mass_index >= 18.5 and body_mass_index < 25:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nYou have a normal weight')
elif body_mass_index >= 25 and body_mass_index < 30:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nYou are overweight')
elif body_mass_index >= 30:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nSorry, you are obese')

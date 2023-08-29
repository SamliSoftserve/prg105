# data
small_onion_base = 1/6
bell_pepper_base = 1/6
tbsp_garlic_powder_base = 2/6
tbsp_butter_base = 3/6
tsp_salt_base = 1/6
tsp_pepper_base = 1/6
cans_tomato_sauce_base = 2/6
box_spaghetti_noodles_base = 1/6
lb_hamburger_meat_base = 1/6
servings_base = 6/6

print('Number of ingredients will change based on servings.')
quantity = int(input('How many servings do you want? '))
print('For ' + str(quantity) + ' servings, you will need: ')
print('Small onion (chopped): ' + format(quantity * small_onion_base, ",1.f"))
print('Bell pepper (chopped): ' + format(quantity * bell_pepper_base, "1,.f"))
print(format(quantity * tbsp_garlic_powder_base, ",1.f") + 'tbsp garlic powder')
print(format(quantity * tbsp_butter_base, ",1.f") + 'tbsp butter')
print(format(quantity * tsp_salt_base, ",1.f") + 'tsp salt')
print(format(quantity * tsp_pepper_base), ",1.f" + 'tsp pepper')
print(format(quantity * cans_tomato_sauce_base, ",1.f") + '(15 oz) cans of tomato sauce')
print(format(quantity * box_spaghetti_noodles_base, ",1.f") + 'lbs hamburger meat')

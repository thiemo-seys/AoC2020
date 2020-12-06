f = open("C:/Users/thiemoT480/Desktop/advent_of_code2020/data/day2/passwords.txt", "r")
values = f.readlines()
values = [value.rstrip('\n') for value in values]

#Part 1
valid = 0
for value in values:
    policy, password = value.split(':')
    amounts, letter = policy.split(' ')
    min_ammount, max_amount = amounts.split('-')
    #change amounts to ints
    min_ammount = int(min_ammount)
    max_amount = int(max_amount)
    amount = password.count(letter)
    if amount >= min_ammount and amount <= max_amount:
        valid += 1

print(f'taks 1 amount valid: {valid}')


#Part2
valid2 = 0
for value in values:
    print(f'value: {value}')
    policy, password = value.split(':')
    print(f'password:{password}')
    amounts, letter = policy.split(' ')
    min_pos, max_pos = amounts.split('-')
    #change amounts to ints, normally we should add +1 here to account for indexing from 1 instead of indexing from 0
    #but because there is an empty space in front of the password, we can ignore that
    min_pos = int(min_pos)
    max_pos = int(max_pos)
    if (password[min_pos] == letter) ^ (password[max_pos] == letter):
        print(f'password: {password} letter: {letter} min: {min_pos} max: {max_pos}')
        print(letter)
        print(password[min_pos] == letter)
        print(password[max_pos] == letter)
        valid2 += 1


print(f'taks 1 amount valid: {valid2}')


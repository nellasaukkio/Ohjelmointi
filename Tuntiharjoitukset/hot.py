from random import randint # generoi satunnaisia kokonaislukuja
user = input('K\u0332ruuna vai kL\u0332aava? ').upper()
if  user and user[0] in  ('K', 'L'):
    machine = randint(0, 1) # 0=kruuna, 1=klaava
    if user[0] == 'K' and machine == 0 or user[0]=='L' and machine==1:
        print('Klaava' if machine else 'Kruuna', ' - voitto!')
    else:
        print('Klaava' if machine else 'Kruuna', ' - hävisit!')

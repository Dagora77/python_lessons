

def create_record(name, telephone, address):
    """Create recorde"""
    record = {
        'name'   : name,
        'phone'  : telephone,
        'adress' : address
    }
    return record

user1 = create_record('Vasya', '+380 777 77 77', 'Tonosy')
user2 = create_record('Pizda', "333", 'Avenu')

print(user1)
print(user2)

def give_award(medal, *persons): # * many persons
    """Give Medals to person"""
    for person in persons:
        print('Tovarish ' + person.title() + ' awarded ' + medal)

give_award("za Berlin", 'Vasya', 'Petya')
give_award("za London", 'Petya', 'Valik', 'Sergey')







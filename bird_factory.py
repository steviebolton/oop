from birds.bird import Bird, Seabird, Fowl

my_bird = Bird('robin', 'chirp' )
print(my_bird.get_description())

my_sea_going_bird = Seabird('Gull', 'skraaak!', 2)
print(my_sea_going_bird.call)
print(my_sea_going_bird.kind)
print(my_sea_going_bird.diving_depth)
print(my_sea_going_bird.get_description())

my_fowl_bird = Fowl('duck', 'kwakkwak', 'landfowl')
print(my_fowl_bird.call)
print(my_fowl_bird.get_description())
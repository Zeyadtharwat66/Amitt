def tower_builder(n_floors):
    count = (n_floors*2)-1
    tower=[]
    n=n_floors
    while n_floors>0:
        spaces = ' ' * (n-n_floors)
        tower.append(spaces+'*'*count+spaces)
        count-=2
        n_floors-=1
    return tower[::-1]
print(tower_builder(3))
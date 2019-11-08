def available_fruits( FRUITS ):
    print()
    print( f"Fruit(s) on tree(s) : {FRUITS}" )

def my_basket( basket_inventory ):
    print()
    print( f"Fruit(s) in my BASKET : {basket_inventory}" )

with open( 'stdin.txt' ) as f:
    exec( f'FRUITS = [{f.read().strip()}]' )

FRUITS = sorted( FRUITS ) if type(FRUITS) == list else []

BASKET = []
max_basket_inventory = len(FRUITS)

while len(FRUITS) and len(BASKET) <= max_basket_inventory:
    available_fruits(FRUITS)

    for fruit in range( len(FRUITS) ):
        picked_fruit = FRUITS[fruit]

        if len(BASKET) == 0:
            BASKET.append(picked_fruit)
            FRUITS = [ FRUITS[f] for f in range( len( FRUITS ) ) if f != fruit ]
            break
            
        elif len(BASKET) == 1 and BASKET[0] != picked_fruit:
            BASKET.append(picked_fruit)
            FRUITS = [ FRUITS[f] for f in range( len( FRUITS ) ) if f != fruit ]
            break

        elif len(BASKET) > 1 and BASKET[-1] != picked_fruit:
            BASKET.append(picked_fruit)
            FRUITS = [ FRUITS[f] for f in range( len( FRUITS ) ) if f != fruit ]
            break

        elif len(BASKET) > 1 and BASKET[0] != picked_fruit:
            BASKET = [ picked_fruit ] + BASKET
            FRUITS = [ FRUITS[f] for f in range( len( FRUITS ) ) if f != fruit ]
            break

    my_basket(BASKET)

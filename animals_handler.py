from swimming import Goldfish, Trout, Flounder, Drum, Snook
from slithering import Kingsnake, Corn, CottonMouth, Racer, DiamondBack
from walking import Pig, Llama, Caracal, Platypus, Camel

frank = Kingsnake("Frank", "King snake", "Mice")
# print(frank)
joe = CottonMouth("Joe", "Cotton mouth", "Mice")
# print(joe.name + " the " + joe.species)
stripe = Corn("Stripe", "Corn snake", "Mice")
print(stripe.feed())
bo = Racer("Bo", "Black racing snake", "Mice")
# print(bo.name)
sam = DiamondBack("Sam", "Diamondback", "Mice")
# print(sam.species)



rod = Goldfish("Rod", "Goldfish", "Fish flakes")
# print(rod)
scout = Trout("Scout", "River trout", "Shrimp")
# print(scout)
flo = Flounder("Flo", "Flounder", "Shrimp")
# print(flo)
red = Drum("Red", "Red drum", "Shrimp")
# print(red)
stripe = Snook("Stripe", "Snook", "Shrimp")
# print(stripe)



po = Pig("Po", "Pot belly pig", "morning", "Pig chow")
# print(f'{po.name} the {po.species} is available to be pet during the {po.shift} shift.')
carl = Llama("Carl", "Grey Llama", "midday", "Llama chow")
# print(carl.feed())
babs = Caracal("Babs", "Caracal", "afternoon", "Camel chow")
# print(babs)
perry = Platypus("Perry", "Secret agent platypus", "morning", "Platypus chow")
# print(perry)
sally = Camel("Sally", "Camel", "midday", "Camel chow")
# print(sally)

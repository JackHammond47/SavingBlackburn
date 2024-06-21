import math
from datetime import datetime
import random

def main():
    now = datetime.now()
    current_date = now.strftime('%d')
    current_day = now.strftime('%A')
    current_time = now.strftime('%H:%M')
    print('Welcome to Saving Blackburn, an adventure game.')
    print(f'It is currently {current_day} the {current_date} at {current_time}.')
    print()
    print('This is a game based in text. The program will print out the story as it unfolds.')
    print('The program will ask you for inputs and you can type out your answers.')
    print('For yes or no questions you can type "y" or "yes" for yes and "no" or "n" for no.')
    print('Other questions will have their options in quotation marks.')
    print()
    start_game = input('Would you like to start a new game? ')
    if start_game.lower() == 'yes' or start_game == 'y':
        print()
        player_name = input('Enter the name of your character: ')
        player_name = player_name.capitalize()
        print(f'Welcome {player_name}!')
        print('The world you are about to enter is a mystical place full of monsters and \
magic. People typical fight as warriors, thieves or mages.')
        class_choice = input('Please enter your class("warrior", "thief", "mage" or type "?" \
for class descriptions): ')
        while class_choice.lower() != 'warrior' and class_choice.lower() != 'thief' and \
class_choice.lower() != 'mage':
            print()
            if class_choice == '?':
                print('Warriors are physical fighters with great health and little to no stealth or magical abilites.')
                print('Thieves are sneaky assassins and rogues, they excel at stealth with decent health and occasional gifts with magic.')
                print('Mages are experts in the arcane arts, and they make up for the pitiful health and okay stealth with raw magic power.')
            class_choice = input('Please enter your class("warrior", "thief", "mage" or "?" \
for class descriptions): ')
        player_data = class_picker(class_choice)
        player_inventory = ['Common Clothes', 10, 'None']
        max_health = player_data[1]
        shop_dict = {
            'sword_basic' : ['Basic Sword', 2],
            'sword_magic' : ['Magic Sword', 7],
            'dagger' : ['Fine Dagger', 3],
            'bow' : ['Bow & Arrows', 4],
            'staff_sparking' : ['Staff of Sparking', 2],
            'staff_fire' : ['Fire Staff', 6],
            'armor_leather' : ['Leather Armor', 3],
            'armor_chain' : ['Chain Armor', 5],
            'hat' : ['Wizard Hat', 4],
            'shield' : ['Shield', 3],
            'potion': ['Potion', 2,],
            'oil' : ['Oil Flask', 2],
            'rope' : ['Coil of Rope', 1],
            'torch' : ['Torch', 1],
        }
        quest = False
        print()
        print(f'A {class_choice.capitalize()}, great choice!')
        if player_data[0] == 'Warrior':
            print('Warriors are mighty knights with the best health of any class.')
            print('You should check out your stats.')
        elif player_data[0] == 'Thief':
            print('Thieves are masters of shadow with the best stealth of any class.')
            print('You should check out your stats.')
        elif player_data[0] == 'Mage':
            print('Mages are powerful sorcerers with the best mana of any class.')
            print('You should check out your stats.')
        info_tutorial = input('You can type "info" at anytime to see your player\'s stats. Try it now: ')
        while info_tutorial.lower() != 'info':
            print()
            info_tutorial = input('Please type "info" to see your player\'s information: ')
        print_player_data(player_data, max_health)
        print()
        print('Good job!')
        print('Some information about your stats...')
        print('Health: Is your lifeforce, if it reaches 0, you\'ll die. You can refill your health with potions.')
        print('Stealth: Your ability to hide from enemies.')
        print('Mana: Your skill in casting spells.')
        print('The highest stat numbers for starting characters is usually around 15, but don\'t worry! Numbers that high are really rare.')
        print('Try testing out different classes or playing again to see what you get!')
        print()
        next_line = input('Type "next" to continue: ')
        while next_line.lower() != 'next':
            if next_line.lower() == 'info':
                print_player_data(player_data, max_health)
            print()
            next_line = input('Type "next" to continue: ')
        print()
        print('Likewise you can view the items your player has anytime by typing "bag".')
        print('Right now you don\'t have much, players start with a bag to hold their items, a set of common clothes and 10 gold pieces.')
        bag_tutorial = input('Try typing "bag" now to view your inventory: ')
        while bag_tutorial.lower() != 'bag':
            if bag_tutorial.lower() == 'info':
                print_player_data(player_data, max_health)
            print()
            bag_tutorial = input('Please type "bag" to see your player\'s inventory: ')
        print_player_inventory(player_inventory)
        print()
        print('Good job!')
        print('You can purchase new equipment at any store, however a word of caution.')
        print('You can only wear 1 piece of apparel and can only wield 1 weapon.')
        print('If you purchase clothing or weapons, your new purchase will replace your old item.')
        print('However, you can carry as many miscellenaous items as you\'d like.')
        print()
        next_line = input('Type "next" to continue: ')
        while next_line.lower() != 'next':
            if next_line.lower() == 'info':
                print_player_data(player_data, max_health)
            elif next_line.lower() == 'bag':
                print_player_inventory(player_inventory)
            print()
            next_line = input('Type "next" to continue: ')
        print()
        print('This game will ask for choices, directions, or combat moves. Just a reminder, you play by typing out your choices.')
        print('At any time you can also type "info" to open stats or "bag" to open inventory.')
        print('This concludes the tutorial section. Good luck.')
        print()
        start = input('Please type "start" to start game: ')
        while start.lower() != 'start':
            if start.lower() == 'info':
                print_player_data(player_data, max_health)
            elif start.lower() == 'bag':
                print_player_inventory(player_inventory)
            print()
            start = input('Please type "start" to start game: ')
        print()
        print()
        print(f'Welcome to Blackburn, {player_name}.')
        print('Blackburn is a quiet farming village in the countryside.')
        print('You\'ve been traveling for a while on your search for adventure and Blackburn is a good a place as any to stop.')
        print('Medieval towns are always having trouble lately, perhaps you can help with something.')
        print()
        print('The town is mostly farmers houses, however the town square has a few useful locations for travelers.')
        print('In the center of the square is the village\'s well.') 
        print('You see a general store on the left, a tavern on the right, and the town hall straight ahead.')
        print()
        building_choice = input('Where would you like to go (type "shop", "tavern", or "hall")? ')
        while building_choice.lower() != 'shop' and building_choice.lower() != 'tavern' and building_choice.lower() != 'hall' and building_choice.lower() != 'well':
            if building_choice.lower() == 'info':
                print_player_data(player_data, max_health)
            elif building_choice.lower() == 'bag':
                print_player_inventory(player_inventory)
            print()
            building_choice = input('Where would you like to go (type "shop", "tavern", or "hall")? ')
        print()
        while building_choice.lower() != 'well':
            if building_choice.lower() == 'shop':
                print('You decide to visit the general store.')
                print('As you swing the door open an old man with few teeth shouts "Welcome In! Feel free to ask about anything you like."')
                shop_choice = input('Would you like to browse the items, leave, or talk to the shopkeeper (type "browse", "leave", or "talk")? ')
                while shop_choice.lower() != 'browse' and shop_choice.lower() != 'leave' and shop_choice.lower() != 'talk':
                    if shop_choice.lower() == 'info':
                        print_player_data(player_data, max_health)
                    elif shop_choice.lower() == 'bag':
                        print_player_inventory(player_inventory)
                    print()
                    shop_choice = input('Would you like to browse the items, leave, or talk to the shopkeeper (type "browse", "leave", or "talk")? ')
                print()
                if shop_choice.lower() == 'browse':
                    print('You start looking around the shop and see the following items and prices.')
                    print('[Item, Cost in Gold Pieces]')
                    index = 0
                    for item in shop_dict.values():
                        if index == 0:
                            print('----Weapons----')
                        elif index == 6:
                            print('----Apparel----')
                        elif index == 9:
                            print('----Miscellaneous----')
                        print(item)
                        index += 1
                    print()
                    start_buying = input('Would you like to make a purchase?(type "yes" or "no") ')
                    keep_buying = 'yes'
                    if start_buying.lower() == 'yes' or start_buying.lower() == 'y':
                        while keep_buying == 'yes' or keep_buying == 'y':
                            print()
                            print("Excellent. To purchase an item type the name EXACTLY.")
                            purchase = input('Type the name of the item or "cancel" to cancel: ')
                            while purchase.lower() != 'cancel':
                                item_purchased = get_key_from_value(shop_dict, purchase)
                                while item_purchased == None:
                                    purchase = input('Please type the name exactly as shown.')
                                    item_purchased = get_key_from_value(shop_dict, purchase)
                                player_inventory = make_purchase(player_inventory, shop_dict, item_purchased)
                                break
                            if purchase.lower() == 'cancel':
                                print('You decide to wait to purchase something, perhaps you\'ll come back later.')
                            else:
                                print('Good purchase. Your inventory is now...')
                                print_player_inventory(player_inventory)
                            keep_buying = input('Would you like to make another purchase? ')
                    else:
                        print('You decide to wait to purchase something, perhaps you\'ll come back later.')
                elif shop_choice.lower() == 'leave':
                    print('You decide to leave and go somewhere else first.')
                    print('You apologize to the shopkeep and walk back out the door.')
                elif shop_choice.lower() == 'talk':
                    print('You decide to talk to the shopkeeper.')
                    print('You say "Hello" and he asks if you want to hear about prices or the talk around town?')
                    shop_choice_talk = input('Type "prices" or "news": ')
                    while shop_choice_talk.lower() != 'prices' and shop_choice_talk.lower() != 'news':
                        if shop_choice_talk.lower() == 'info':
                            print_player_data(player_data, max_health)
                        elif shop_choice_talk.lower() == 'bag':
                            print_player_inventory(player_inventory)
                        print()
                        shop_choice_talk = input('Type "prices" or "news": ')
                    if shop_choice_talk.lower() == 'prices':
                        print('The shopkeeper tells you about the following items he has for sale and their prices.')
                        print('[Item, Cost in Gold Pieces]')
                        for item in shop_dict.values():
                            print(item)
                        start_buying = input('Would you like to make a purchase?(type "yes" or "no") ')
                        keep_buying = 'yes'
                        if start_buying.lower() == 'yes' or start_buying.lower() == 'y':
                            while keep_buying == 'yes' or keep_buying == 'y':
                                print("Excellent. To purchase an item type the name EXACTLY.")
                                purchase = input('Type the name of the item or "cancel" to cancel: ')
                                while purchase.lower() != 'cancel':
                                    item_purchased = get_key_from_value(shop_dict, purchase)
                                    while item_purchased == None:
                                        purchase = input('Please type the name exactly as shown.')
                                        item_purchased = get_key_from_value(shop_dict, purchase)
                                    player_inventory = make_purchase(player_inventory, shop_dict, item_purchased)
                                    break
                                if purchase.lower() == 'cancel':
                                    print('You decide to wait to purchase something, perhaps you\'ll come back later.')
                                else:
                                    print('Good purchase. Your inventory is now...')
                                    print_player_inventory(player_inventory)
                                keep_buying = input('Would you like to make another purchase? ')
                        else:
                            print('You decide to wait to purchase something, perhaps you\'ll come back later.')
                    elif shop_choice_talk.lower() == 'news':
                        print_news()
                        prices = input('Would you like to browse our items? ')
                        while prices.lower() != 'y' and prices.lower() != 'yes' and prices.lower() != 'n' and prices.lower() != 'no':
                            if prices.lower() == 'info':
                                print_player_data(player_data, max_health)
                            elif prices.lower() == 'bag':
                                print_player_inventory(player_inventory)
                            print()
                            prices = input('Would you like to browse our items? ')
                        if prices.lower() == 'y' or prices.lower() == 'yes':
                            print('[Item, Cost in Gold Pieces]')
                        for item in shop_dict.values():
                            print(item)
                        start_buying = input('Would you like to make a purchase? (type "yes" or "no") ')
                        keep_buying = 'yes'
                        if start_buying.lower() == 'yes' or start_buying.lower() == 'y':
                            while keep_buying == 'yes' or keep_buying == 'y':
                                print("Excellent. To purchase an item type the name EXACTLY.")
                                purchase = input('Type the name of the item or "cancel" to cancel: ')
                                while purchase.lower() != 'cancel':
                                    item_purchased = get_key_from_value(shop_dict, purchase)
                                    while item_purchased == None:
                                        purchase = input('Please type the name exactly as shown.')
                                        item_purchased = get_key_from_value(shop_dict, purchase)
                                    player_inventory = make_purchase(player_inventory, shop_dict, item_purchased)
                                    break
                                if purchase.lower() == 'cancel':
                                    print('You decide to wait to purchase something, perhaps you\'ll come back later.')
                                else:
                                    print('Good purchase. Your inventory is now...')
                                    print_player_inventory(player_inventory)
                                keep_buying = input('Would you like to make another purchase? ')
                        else:
                            print('You decide to wait to purchase something, perhaps you\'ll come back later.')
            elif building_choice.lower() == 'tavern':
                print('You walk into the tavern and see a burly man wiping down tables.')
                print('He looks up at you and shouts, "What can I do you for? You want a drink or the news?"')
                tavern_choice = input('Type "news" or "drink": ')
                while tavern_choice.lower() != 'news' and tavern_choice.lower() != 'drink':
                    if tavern_choice.lower() == 'info':
                        print_player_data(player_data, max_health)
                    elif tavern_choice.lower() == 'bag':
                        print_player_inventory(player_inventory)
                    print()
                    tavern_choice = input('Type "news" or "drink": ')
                if tavern_choice.lower() == 'news':
                    print_news()
                    print('Sorry news is all I got now, no drinks with the water being poisoned.')
                    print('You thank him and step outside.')
                elif tavern_choice.lower() == 'drink':
                    print('Sorry no more drinks right now.')
                    print_news()
                    print('With the poisoned well we\'re all out of drinks.')
                    print('You thank him and step outside.')
            elif building_choice.lower() == 'hall':
                print('A short man with a fancy coat looks up at you from a wobbly old throne.')
                print('He brushes down his comb-over and waddles over to you, "Adventurer, we need your help!"')
                print('He explains that the water from the well in the middle of town has been posioned and he needs \
you to go down and investigate.')
                print('"It may be dangerous, but if you help us I shall reward you handsomely!"')
                print('And with that he ushers you out the door and locks it.')
                quest = True
            print()
            if not quest:
                building_choice = input('Where would you like to go now(type "shop", "tavern", or "hall")? ')
            elif quest:
                building_choice = input('Where would you like to go now(type "shop", "tavern", or "well")? ')
        print()
        print('You stare down the dark hole.')
        if 'Coil of Rope' in player_inventory:
            print('You tie the rope off and slide down the rope into the blackness below.')
            print('There is a ring of cobblestone surrounding the watery pit at the bottom of the well that you stand on.')
        else:
            print('You jump down and barely catch yourself on a ring of cobblestone surrounding the watery pit at the bottom of the well.')
        print('Ahead of you is a tunnel leading forward, its dark but a putrid smell is coming from further ahead.')
        if 'Torch' in player_inventory:
            enter_choice = input('Would you like to sneak ahead or light a torch (type "sneak" or "torch")? ')
            enter_choice = enter_choice.lower()
        else:
            enter_choice = input('Would you like to "sneak" or "charge" ahead? ')
            enter_choice = enter_choice.lower()
        while enter_choice != 'sneak' and enter_choice != 'charge' and enter_choice != 'torch':
            if enter_choice.lower() == 'info':
                print_player_data(player_data, max_health)
            elif enter_choice.lower() == 'bag':
                print_player_inventory(player_inventory)
            print()
            if 'Torch' in player_inventory:
                enter_choice = input('Would you like to sneak ahead or light a torch (type "sneak" or "torch")? ')
                enter_choice = enter_choice.lower()
            else:
                enter_choice = input('Would you like to "sneak" or "charge" ahead? ')
                enter_choice = enter_choice.lower()
        hidden = False
        dark = True
        ogre_health = random.randint(40,55)
        max_ogre_health = ogre_health
        print()
        if enter_choice == 'sneak':
            hidden = True
            print('You creep forward down the earthen tunnel, carefully placing every step.')
            print('Suddenly you hear munching from up ahead, squinting through the darkness you see a hulking mass \
grabbing and eating some rotting animal corpses.')
            sneak_attack = input('Too late to turn back now, (type "attack" to attack): ')
            sneak_attack = sneak_attack.lower()
            while sneak_attack != 'attack':
                if sneak_attack == 'info':
                    print_player_data(player_data, max_health)
                elif sneak_attack == 'bag':
                    print_player_inventory(player_inventory)
                print()
                sneak_attack = input('Too late to turn back now, (type "attack" to attack): ')
                sneak_attack = sneak_attack.lower()
            print()
            ogre_health = attack(player_inventory, player_data, ogre_health, hidden)
            hidden = False
        elif enter_choice == 'charge':
            print(f'You hold your {player_inventory[2]} tight, marching down the dank and muddy tunnel.')
            print('Suddenly you hear a deep and gutteral growl as a hulking mass drops the animal corpse it was eating and roars at you.')
            charge_attack = input('Too late to turn back now, (type "attack" to attack): ')
            charge_attack = charge_attack.lower()
            while charge_attack != 'attack':
                if charge_attack == 'info':
                    print_player_data(player_data, max_health)
                elif charge_attack == 'bag':
                    print_player_inventory(player_inventory)
                print()
                charge_attack = input('Too late to turn back now, (type "attack" to attack): ')
                charge_attack = charge_attack.lower()
            print()
            ogre_health = attack(player_inventory, player_data, ogre_health, hidden)
        elif enter_choice == 'torch':
            dark = False
            if not dark:
                hidden = True
            print('You march down the muddy tunnel, torch in hand when you hear a grunt ahead.')
            print('You gasp as a giant Ogre hissses at the light and covers his meaty eyes.')
            print('The creature cleary has made its way to the well through a crude tunnel and there are animal \
corpses littering the floor of its makeshift lair.')
            torch_attack = input('The Ogre won\'t stay stunned for long, (type "attack" to attack)? ')
            torch_attack = torch_attack.lower()
            while torch_attack != 'attack':
                if torch_attack == 'info':
                    print_player_data(player_data, max_health)
                elif torch_attack == 'bag':
                    print_player_inventory(player_inventory)
                print()
                torch_attack = input('Too late to turn back now, (type "attack" to attack): ')
                torch_attack = torch_attack.lower()
            print()
            ogre_health = attack(player_inventory, player_data, ogre_health, hidden)
            hidden = False
        print('You have angered the ogre that dug its way to the town\'s well, prepare to fight for your life.')
        game_over = False
        while ogre_health > 0 and not game_over:
            while player_data[1] > 0 and ogre_health > 0:
                print()
                print('In combat you can choose between using an item from your bag, attacking, or attempting to hide.')
                print('And of course you check your current bag and stats with "bag" or "info".')
                battle_choice = input('Type "item", "attack", "hide", "info", or "bag": ')
                battle_choice = battle_choice.lower()
                while battle_choice != 'attack' and battle_choice != 'hide' and battle_choice != 'item':
                    if battle_choice == 'info':
                        print_player_data(player_data, max_health)
                    elif battle_choice == 'bag':
                        print_player_inventory(player_inventory)
                    print()
                    battle_choice = input('Type "item", "attack", "hide", "info", or "bag": ')
                    battle_choice = battle_choice.lower()
                print()
                if battle_choice == 'attack':
                    ogre_health = attack(player_inventory, player_data, ogre_health, hidden)
                    hidden = False
                elif battle_choice == 'item':
                    item_success = use_item(player_inventory, player_data, ogre_health, max_health)
                    while item_success[0] == 'None':
                        item_success[0] = 'Continue'
                        print('In combat you can choose between using an item from your bag, attacking, or attempting to hide.')
                        print('And of course you check your current bag and stats with "bag" or "info".')
                        battle_choice = input('Type "item", "attack", "hide", "info", or "bag": ')
                        battle_choice = battle_choice.lower()
                        while battle_choice != 'attack' and battle_choice != 'hide' and battle_choice != 'item':
                            if battle_choice == 'info':
                                print_player_data(player_data, max_health)
                            elif battle_choice == 'bag':
                                print_player_inventory(player_inventory)
                            print()
                            battle_choice = input('Type "item", "attack", "hide", "info", or "bag": ')
                            battle_choice = battle_choice.lower()
                        print()
                        if battle_choice == 'attack':
                            ogre_health = attack(player_inventory, player_data, ogre_health, hidden)
                            hidden = False
                        elif battle_choice == 'item':
                            item_success = use_item(player_inventory, player_data, ogre_health, max_health)
                        elif battle_choice == 'hide':
                            hidden = hide(player_data, hidden)
                        print()
                    if item_success[0] == 'potion':
                        player_data[1] = item_success[1]
                    elif item_success[0] == 'oil':
                        ogre_health = item_success[1]
                elif battle_choice == 'hide':
                    hidden = hide(player_data, hidden)
                print()
                if not hidden:
                    player_data[1] = ogre_attack(player_inventory, player_data)
                    print('The ogre heaves his massive fist at you.')
                    print(f'Your health is {player_data[1]}/{max_health}.')
                print(f' The Ogre\'s health is {ogre_health}/{max_ogre_health}')
            print()
            if player_data[1] <= 0:
                game_over = True
                print('GAME OVER')
                print(f'{player_name} has died, restart to play again.')
        if ogre_health < 0:
            print("You killed the Ogre! ")
            print(f'Congratulations {player_name}. The Ogre lies dead at your feet and you saved the town.')
            print('The mayor brings you 100 gold pieces for you help and the townspeople close up the tunnel contaminating their water.')
            print('Restart to play agin.')
    else:
        print('Okay, please come back soon!')

def class_picker(class_choice):
    player_data = []
    if class_choice.lower() == 'warrior':
        player_class_name = 'Warrior'
        player_health = random.randint(10,15)
        player_stealth = random.randint(2,6)
        player_mana = random.randint(0,4)
    elif class_choice.lower() == 'thief':
        player_class_name = 'Thief'
        player_health = random.randint(7,10)
        player_stealth = random.randint(8,13)
        player_mana = random.randint(1,6)
    elif class_choice.lower() == 'mage':
        player_class_name = 'Mage'
        player_health = random.randint(5,8)
        player_stealth = random.randint(3,7)
        player_mana = random.randint(9,14)
    player_data = [player_class_name, player_health, player_stealth, player_mana]
    return player_data

def make_purchase(player_inventory, shop_dict, item_purchased):
    name_cost = shop_dict[item_purchased]
    item_name = name_cost[0]
    item_cost = name_cost[1]
    if item_purchased == 'sword_basic' or item_purchased == 'sword_magic' or item_purchased == 'dagger' or\
item_purchased == 'bow' or item_purchased == 'staff_sparking' or item_purchased == 'staff_fire':
        player_inventory[2] = item_name
        player_inventory[1] = player_inventory[1] - item_cost
    elif item_purchased == 'armor_leather' or item_purchased == 'armor_chain' or item_purchased == 'hat':
        player_inventory[0] = item_name
        player_inventory[1] = player_inventory[1] - item_cost
    else:
        player_inventory.append(item_name)
        player_inventory[1] = player_inventory[1] - item_cost
    return player_inventory

def attack(player_inventory, player_data, ogre_health, hidden):
    damage = 0
    clothing = player_inventory[0]
    hat_bonus = 0
    if clothing == 'Wizard Hat':
        hat_bonus = 4
    if hidden:
        chance_miss = random.randint(1,8)
    else:
        chance_miss = random.randint(1,5)
    if chance_miss == 1:
        print('Oh no! Your attack barely misses...')
    else:
        if player_inventory[2] == 'None':
            print('You charge forward with bare fists and punch the ogre\'s thick hide, it doesn\'t seem very effective...')
            damage = random.randint(0,1)
            ogre_health -= damage
        elif player_inventory[2] == 'Basic Sword':
            print('You slice him with your trusty old blade, the cut looks deep.')
            if hidden:
                damage = random.randint(5,7)
            else:
                damage = random.randint(2,4)
            ogre_health -= damage
        elif player_inventory[2] == 'Magic Sword':
            print('Your sword glows with arcane energy, you swing at the ogre and he roars in pain.')
            if hidden:
                damage = random.randint(10,12)
            else:
                damage = random.randint(7,9)
            ogre_health -= damage
        elif player_inventory[2] == 'Fine Dagger':
            if hidden:
                print('Jumping from the darkness you plung the dagger deep into his joints, he howls in pain.')
                damage = random.randint(13,15)
            else:
                print('You run forward and cut him with the small dagger, it would probably be more effective to attack him from the shadows.')
                damage = random.randint(3,5)
            ogre_health -= damage
        elif player_inventory[2] == 'Bow & Arrows':
            print('You nock an arrow and send it flying towards the huge monster, the head lodges into its hide as he roars in pain.')
            if hidden:
                damage = random.randint(11,13)
            else:
                damage = random.randint(6,8)
            ogre_health -= damage
        elif player_inventory[2] == 'Staff of Sparking':
            print('You send a shower of small sparks towards the terrifying beast, its not very powerful but the burns seem to hurt him.')
            if hidden:
                damage = random.randint(2,4) + player_data[3] + hat_bonus
            else:
                damage = random.randint(0,2) + player_data[3] + hat_bonus
            ogre_health -= damage
        elif player_inventory[2] == 'Fire Staff':
            print('You send a fiery ball towards the beast, he howls in rage as the flame burns through his hide.')
            if hidden:
                damage = random.randint(6,8) + player_data[3] + hat_bonus
            else:
                damage = random.randint(4,6) + player_data[3] + hat_bonus
            ogre_health -= damage
    return ogre_health

def use_item(player_inventory, player_data, ogre_health, max_health):
    player_health = player_data[1]
    item_success = ['None', 0]
    if 'Potion' in player_inventory and 'Oil Flask' in player_inventory:
        choice = input('Would you like to use a Potion or an Oil Flask? (type "oil", "potion", or "cancel") ')
        choice = choice.lower()
        while choice != 'potion' and choice != 'oil' and choice != 'cancel':
            if choice == 'info':
                print_player_data(player_data, max_health)
            elif choice == 'bag':
                print_player_inventory(player_inventory)
            print()
            choice = input('Would you like to use a Potion or an Oil Flask? (type "oil", "potion", or "cancel") ')
            choice = choice.lower()
        if choice == 'potion':
            health_gained = random.randint(6,10)
            player_health += health_gained
            if player_health > max_health:
                player_health = max_health
            print('You drink the reddish potion and you feel as your wounds close.')
            print(f'Your health is now {player_health}/{max_health}.')
            item_success = ['potion', player_health]
        elif choice == 'oil':
            damage = random.randint(8,20)
            ogre_health -= damage
            print('You throw the Flask of Oil at the monster, the glass breaks on its hide and the igniting chemicals go off.')
            print('Flame engulfs the ogre and he roars in searing pain.')
            item_success = ['oil', ogre_health]
    elif 'Potion' in player_inventory:
        choice = input('Would you like to drink a potion? ')
        choice = choice.lower()
        while choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n':
            if choice == 'info':
                print_player_data(player_data, max_health)
            elif choice == 'bag':
                print_player_inventory(player_inventory)
            print()
            choice = input('Would you like to drink a potion? ')
            choice = choice.lower()
        if choice == 'yes' or choice == 'y':
            health_gained = random.randint(6,10)
            player_health += health_gained
            if player_health > max_health:
                player_health = max_health
            print('You drink the reddish potion and you feel as your wounds close.')
            print(f'Your health is now {player_health}/{max_health}.')
            item_success = ['potion', player_health]
    elif 'Oil Flask' in player_inventory:
        choice = input('Would you like to throw your Oil Flask? ')
        choice = choice.lower()
        while choice != 'yes' and choice != 'y' and choice != 'no' and choice != 'n':
            if choice == 'info':
                print_player_data(player_data, max_health)
            elif choice == 'bag':
                print_player_inventory(player_inventory)
            print()
            choice = input('Would you like to drink a potion? ')
            choice = choice.lower()
        if choice == 'yes' or choice == 'y':
            damage = random.randint(8,20)
            ogre_health -= damage
            print('You throw the Flask of Oil at the monster, the glass breaks on its hide and the igniting chemicals go off.')
            print('Flame engulfs the Ogre and he roars in searing pain.')
            item_success = ['oil', ogre_health]
    else:
        print('Sorry, you have no usable items. Purchase Oil Flask or Potions from the store.')
    return item_success


def hide(player_data, hidden):
    stealth = player_data[2]
    ogre_perception = random.randint(0,15)
    success = True
    print('With the various debris, carcasses, and tunnels, you hope to get out of the Ogre\'s line of sight.')
    if not hidden:
        if stealth >= ogre_perception:
            print('You dash away from the monster and successfully hide from the Ogre, he sniffs the air looking for you.')
        else:
            print('You try to run behind some of the obstacles but the Ogre sees exactly where you go.')
            success = False
    else:
        print('You are already hidden.')
    return success

def ogre_attack(player_inventory, player_data):
    armor_bonus = 0
    if 'Shield' in player_inventory:
        armor_bonus += 2
    if 'Leather Armor' in player_inventory:
        armor_bonus += 2
    if 'Chain Armor' in player_inventory:
        armor_bonus += 4
    damage = random.randint(1,10)
    damage -= armor_bonus
    if damage < 0:
        damage = 0
    player_health = player_data[1] - damage
    return player_health

def get_key_from_value(dict, value):
    key = None
    for keys, items in dict.items():
        if value == items[0]:
            key = keys
    return key

def print_player_data(player_data, max_health):
    print()
    print(f'Your stats are [Class: {player_data[0]}, Health: {player_data[1]}/{max_health}, Stealth: {player_data[2]}, Mana: {player_data[3]}]')

def print_player_inventory(player_inventory):
    print()
    print(f'Your equipment is [Apparel: {player_inventory[0]}, {player_inventory[1]} Gold Pieces, Weapon: {player_inventory[2]}, Misc: ', end = '')
    for index, item in enumerate(player_inventory):
        if index > 2:
            print(item, end=' ')
    print(']')

def print_news():
    print('He looks at you all serious and says, ')
    print('"Well the water from the well has been making people pretty sick.')
    print('Apparently the Mayor is willing to reward anyone who ventures down there to figure out why.')
    print('If you want to find out more you can ask about it at the town hall."')

if __name__ == "__main__":
    main()

#make it so cant purchase if money is <= 0
    #can use player_data[1] < shop_dict[item cost]
#remove potions when used


using System;

class Program
{
    
    static void Attack(Player player, Creature creature)
    {
        Random random = new();
        int STEALTH_BONUS = 5;
        //can change stealth bonus for balanced gameplay
        var weaponStats = player.Inventory.GetWeaponStats();
        int damage = weaponStats.Item1;
        int category = weaponStats.Item2;
        if (category == 2)
            creature.CreatureHP -= damage + player.CharacterClass.Mana;
        else if (category == 1)
            if (player.Hidden)
            {
                creature.CreatureHP -= damage + STEALTH_BONUS;
                int lostStealth = random.Next(0, 100);
                if (lostStealth <= 49)
                    player.Hidden = false;
            }
            else
                creature.CreatureHP -= damage;
        else
            creature.CreatureHP -= damage;
        player.CharacterClass.Health -= creature.CreatureDamage;
    }
    public static void Main(string[] args)
    {
        Console.WriteLine("Welcome to Saving Blackburn, a roguelike adventure game.");
        Console.WriteLine("");
        Console.WriteLine("The kingdom of Blackburn has been afflicted with a terrible curse.");
        Console.WriteLine("Someone has to enter a dangerous magical cave and destroy the evil artifact inside or the kingdom will be destroyed.");
        Console.WriteLine("The king has promised half the kingdom to whoever destroys the artifact and many have died trying, will you succeed?");
        Console.WriteLine("");
        Console.WriteLine("");
        Console.Write("What is your character's name: ");
        string name = Console.ReadLine() ?? "Unnamed Hero";
        
        int classChoice = 0;
        bool success = false;
        while (!success)
        {
            Console.WriteLine("");
            Console.Write("What is your character's class (0 for warrior, 1 for thief, and 2 for mage): ");
            success = int.TryParse(Console.ReadLine(), out classChoice);
            if (!success)
                Console.WriteLine("Please type 0 for warrior, 1 for thief, or 2 for mage");
        }
        Player player = new(name, new CharacterClass(classChoice));
        //creates new player, then adds a basic wand for mages or shortsword for rogues and warriors
        if (classChoice == 2)
            player.Inventory.Items.Add(new Weapon(12));
        else
            player.Inventory.Items.Add(new Weapon(7));
        //shop
        //rooms
        bool victory = false;
        int roomChoice;
        while (!victory)
        {
            Console.WriteLine("");
            Console.WriteLine("You can view your current stats, inventory, or go to the next room.");
            Console.WriteLine("   1. Next room.");
            Console.WriteLine("   2. View current stats.");
            Console.WriteLine("   3. View inventory.");
            Console.WriteLine("   0. Quit.");
            Console.WriteLine("");
            Console.Write("Please enter a number 0-3 for your choice: ");
            if (int.TryParse(Console.ReadLine(), out roomChoice))
            {
                Console.WriteLine("");
                switch (roomChoice)
                {
                    case 0:
                        Console.WriteLine("");
                        Console.WriteLine("Exiting Game...");
                        victory = true;
                        break;
                    case 1:
                        Room room = new(player);
                        if (room.RoomType == 0 || room.RoomType == 3)
                        {
                            Console.WriteLine($"You walk into a room and youre not alone! You see a {room.Creatures[room.Creatures.Count - 1].CreatureName}");
                            foreach (Creature creature in room.Creatures)
                            {
                                while (creature.CreatureHP > 0 && player.CharacterClass.Health > 0)
                                {
                                    Console.WriteLine("");
                                    Console.WriteLine($"The {creature.CreatureName} has {creature.CreatureHP} health left.");
                                    Console.WriteLine("You both attack.");
                                    Attack(player, creature);
                                    Console.WriteLine("");
                                    Console.WriteLine($"You have {player.CharacterClass.Health} health left");
                                }
                                if (player.CharacterClass.Health <= 0)
                                {
                                    victory = true;
                                    Console.WriteLine("");
                                    Console.WriteLine("You were killed and another corpse is added to the tomb of horrors.");
                                    break;
                                }
                                else if (creature.CreatureHP <= 0)
                                {
                                    Console.WriteLine("");
                                    Console.WriteLine("Congrats, you killed the monster.");
                                    if (creature.CreatureID > 6)
                                    {
                                        Console.WriteLine($"You recieve a {creature.CreatureName} key");
                                        if (creature.CreatureID == 7)
                                            player.Inventory.Items.Add(new Key(4));
                                        else if (creature.CreatureID == 8)
                                            player.Inventory.Items.Add(new Key(5));
                                        else
                                            player.Inventory.Items.Add(new Key(6));
                                    }
                                }
                            }
                        }
                        else if (room.RoomType == 4)
                        {
                            room.Trader.MakePurchase();
                        }
                        else 
                            victory = room.Victory;
                        break;
                    case 2:
                    //view stats
                        player.CharacterClass.GetStats();
                        break;
                    case 3:
                    //view inventory
                        player.Inventory.GetInventory();
                        break;
                    default:
                        Console.Write("Invalid choice. Please enter a number 0-3: ");
                        break;
                }
            }
        }
    }
}

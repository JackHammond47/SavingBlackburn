class Trader
{
    public Player Player { get; set; }
    public int Gold { get; set; }
    public Trader(Player player)
    {
        Player = player;
        Gold = Player.Inventory.Gold;
    }
    public void MakePurchase()
    {
        Console.WriteLine("The next room is brimming with magical energy. ");
        Console.WriteLine("You see a strange old man with a large sack offering to trade.");
        Console.WriteLine("He can exchange your current armor or weapon, or sell keys.");
        Console.WriteLine("");
        Console.WriteLine("The choices are as follows: ");
        Console.WriteLine("   1. Purchase random piece of armor (10 gold).");
        Console.WriteLine("   2. Purchase random weapon (15 gold).");
        Console.WriteLine("   3. Purchase random key to the artifact door (25 gold).");
        Console.WriteLine("   0. Decline.");
        
        bool success = false;
        int tradeChoice = 0;
        while (!success)
        {
            Console.WriteLine("");
            Console.WriteLine($"Current wealth: {Gold} gold.");
            Console.Write("Please enter a number 0-3 for your choice: ");
            if (int.TryParse(Console.ReadLine(), out tradeChoice))
            {
                switch (tradeChoice)
                {
                    case 0:
                        Console.WriteLine("You declined the offer.");
                        success = true;
                        break;
                    case 1:
                        if (Gold >= 10)
                        {
                            Gold -= 10;
                            string newArmor = Player.Inventory.AddRandomArmor();
                            Console.WriteLine($"You bought {newArmor}");
                            success = true;
                        }
                        else
                        {
                            Console.WriteLine("You do not have enough gold for this purchase.");
                        }
                        break;
                    case 2:
                        if (Gold >= 15)
                        {
                            Gold -= 15;
                            string newWeapon = Player.Inventory.AddRandomWeapon();
                            Console.WriteLine($"You purchased a {newWeapon}.");
                            success = true;
                        }
                        else
                        {
                            Console.WriteLine("You do not have enough gold for this purchase.");
                        }
                        break;
                    case 3:
                        if (Gold >= 25)
                        {
                            Gold -= 25;
                            string newKey = Player.Inventory.AddRandomKey();
                            Console.WriteLine($"You bought a {newKey}. ");
                            success = true;
                        }
                        else
                        {
                            Console.WriteLine("You do not have enough gold for this purchase.");
                        }
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please enter a number 0-3.");
                        break;
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a number 0-3.");
            }
        }
        // Update the player's gold after purchase
        Player.Inventory.Gold = Gold;
        Console.WriteLine("He thanks you for your time and waves a blessing your way, you feel stronger.");
        Console.WriteLine("");
        Player.CharacterClass.Health += 10;
    }
}
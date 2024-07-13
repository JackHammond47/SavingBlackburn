class CharacterClass
{
    private int _classChoice;
    //0 = "warrior", 1 = "thief", 2 = "mage"
    public int Health {get; set;}
    public int Stealth {get; set;}
    public int Mana {get; set;}

    public int MaxHealth {get; set;}
    private int _high = 80;
    //High should be around 15, changed to 80 to win game
    private int _mid = 10;
    private int _low = 5;
    //can change high, mid, and low values based on preferences
    public CharacterClass(int classChoice)
    {
        _classChoice = classChoice;
        if (_classChoice == 0)
        {
            //warrior
            Health = _high;
            Stealth = _mid;
            Mana = _low;
            MaxHealth = Health;
        }
        else if (_classChoice == 1)
        {
            //thief
            //CHANGE HEALTH TO LOW WHEN BALANCED
            // Health = _low;
            Health = _high;
            Stealth = _high;
            Mana = _mid;
            MaxHealth = Health;
        }
        else 
        {
            //mage
            //CHANGE HEALTH TO MID WHEN BALANCED
            // Health = _mid;
            Health = _high;
            Stealth = _low;
            Mana = _high;
            MaxHealth = Health;
        }
    }
    public void GetStats()
    {
        Console.WriteLine("");
        Console.WriteLine("Current Stats:");
        Console.WriteLine($"  Health: {Health}/{MaxHealth}");
        Console.WriteLine($"  Stealth: {Stealth}");
        Console.WriteLine($"  Mana: {Mana}");
        Console.WriteLine("");
    }
}
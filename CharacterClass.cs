class CharacterClass
{
    private int _classChoice;
    //0 = "warrior", 1 = "thief", 2 = "mage"
    public int Health {get; set;}
    public int Stealth {get; set;}
    public int Mana {get; set;}
    private int _high = 15;
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
        }
        else if (_classChoice == 1)
        {
            //thief
            Health = _low;
            Stealth = _high;
            Mana = _mid;
        }
        else 
        {
            //mage
            Health = _mid;
            Stealth = _low;
            Mana = _high;
        }
    }
}
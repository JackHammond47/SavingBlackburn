class Weapon : Item
{
    public int WeaponID {get;set;}
    //7= shortsword, 8 = mace, 9 = longsword, 10 = dagger, 11 = bow&arrows, 12 = wand of sparking, 13 = fire staff, 14 = lightning orb
    public string WeaponName {get;set;}
    public int Damage {get;set;}
    public int Category {get;set;}
    //0 = basic (no bonus), 1 = stealth (add bonus if hidden), 2 = magic (add mana to damage)

    public Weapon(int itemID) : base(itemID)
    {
        WeaponID = itemID;
        if (WeaponID == 7)
        {
            WeaponName = "Shortsword";
            Damage = 3;
            Category = 0;
        }
        else if (WeaponID == 8)
        {
            WeaponName = "Mace";
            Damage = 5;
            Category = 0;
        }
        else if (WeaponID == 9)
        {
            WeaponName = "Longsword";
            Damage = 9;
            Category = 0;
        }
        else if (WeaponID == 10)
        {
            WeaponName = "Dagger";
            Damage = 2;
            Category = 1;
        }
        else if (WeaponID == 11)
        {
            WeaponName = "Bow and Arrows";
            Damage = 7;
            Category = 1;
        }
        else if (WeaponID == 12)
        {
            WeaponName = "Wand of Sparking";
            Damage = 2;
            Category = 2;
        }
        else if(WeaponID == 13)
        {
            WeaponName = "Fire Staff";
            Damage = 6;
            Category = 2;
        }
        else
        {
            WeaponName = "Lightning Orb";
            Damage = 9;
            Category = 2;
        }
    }
}
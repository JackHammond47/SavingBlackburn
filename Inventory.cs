class Inventory
{
    public HashSet<Item> Items {get; set;}
    //hashset instead of list for removing duplicates, like armor or boss keys
    public int Gold {get; set;}
    private int _startingGold = 10;
    //can change starting gold based on preference
    public Inventory()
    {
        Items = new();
        Items.Add(new Armor(0));
        Gold = _startingGold;
        //every character starts with common clothes and 10 gold
    }
    public (int, int) GetWeaponStats()
    {
        foreach (Item item in Items)
            if (item.ItemID >= 7 && item.ItemID <= 14)
                {
                    Weapon weapon = item as Weapon;
                    return(weapon.Damage, weapon.Category);
                }
        return (1, 0);
    }
    public string AddRandomArmor()
    {
        foreach(Item item in Items)
            if(item.ItemID >= 0 && item.ItemID <= 3)
                Items.Remove(item);
        Random random= new();
        int newArmorID = random.Next(0, 4);
        Armor newArmor = new Armor(newArmorID);
        Items.Add(newArmor);
        return newArmor.ArmorName;
    }
    public string AddRandomWeapon()
    {
        foreach(Item item in Items)
            if(item.ItemID >= 7 && item.ItemID <= 14)
                Items.Remove(item);
        Random random= new();
        int newWeaponID = random.Next(7, 14);
        Weapon newWeapon = new Weapon(newWeaponID);
        Items.Add(newWeapon);
        return newWeapon.WeaponName;
    }
    public string AddRandomKey()
    {
        Random random= new();
        int newKeyID = random.Next(4, 7);
        Key newKey = new Key(newKeyID);
        Items.Add(newKey);
        return newKey.KeyName;
    }
    public void GetInventory()
    {
        string armor = "Common Clothes";
        string weapon = "None";
        var keys = new List<string>(); 
        foreach(Item item in Items)
            if(item.ItemID >= 0 && item.ItemID <= 3)
                armor = (item as Armor).ArmorName;
            else if(item.ItemID >= 7 && item.ItemID <= 14)
                weapon = (item as Weapon).WeaponName;
            else
                keys.Add((item as Key).KeyName);
        Console.WriteLine("");
        Console.WriteLine("Current Inventory:");
        Console.WriteLine($"  Armor: {armor}");
        Console.WriteLine($"  Weapon: {weapon}");
        Console.WriteLine("  Keys: " + (keys.Count > 0 ? string.Join(", ", keys) : "None"));
        Console.WriteLine("");
    }
    //item codes: 0-3 armor, 4-6 keys, 7-14 weapons
    //NOT YET ADDED, 14+ MiscItem, ex. Shield, potion, oil flask, rope, , torch, etc.
}
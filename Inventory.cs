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
            if (item.ItemID >= 7 && item.ItemID <= 13)
                {
                    Weapon weapon = item as Weapon;
                    return(weapon.Damage, weapon.Category);
                }
        return (1, 0);
    }
}
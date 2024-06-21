class Armor : Item
{
    public int ArmorID {get;set;}
    //0 = "Common Clothes, 1 AP", 1 =  "Leather Armor, 3 AP", 2 = "Chain Mail, 5 AP", 3 = "Wizard Robes, 2 AP"
    public int AP {get;set;}
    public int ManaBonus {get;set;}
    public string ArmorName {get;set;}
    public Armor(int itemID) : base(itemID)
    {
        ArmorID = itemID;
        if (ArmorID == 0)
        {
            AP = 1;
            ManaBonus = 0;
            ArmorName = "Common Clothes";
        }
        else if (ArmorID == 1)
        {
            AP = 3;
            ManaBonus = 0;
            ArmorName = "Leather Armor";
        }
        else if (ArmorID == 2)
        {
            AP = 5;
            ManaBonus = 0;
            ArmorName = "Chain Mail";
        }
        else
        {
            AP = 2;
            ManaBonus = 4;
            ArmorName = "Wizard Robes";
        }
    }
}
public abstract class Item
{
    public int ItemID { get; set;}
    //0-3 armors, 4-6 keys, 7-13 weapons, 14+ Misc.
    public Item(int itemID)
    {
        ItemID = itemID;
    }
}
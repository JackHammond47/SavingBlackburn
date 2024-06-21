public class Key : Item
{
    public int KeyID { get; set;}
    //4 = dragonKey, 5 = beholderKey, 6 = mindflayerKey
    public Key(int keyID) : base(keyID)
    {
        KeyID = keyID;
    }
}
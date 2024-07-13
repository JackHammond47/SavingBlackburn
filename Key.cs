public class Key : Item
{
    public int KeyID { get; set;}
    //4 = dragonKey, 5 = beholderKey, 6 = mindflayerKey
    public string KeyName { get; set;}
    public Key(int keyID) : base(keyID)
    {
        KeyID = keyID;
        if (KeyID == 4)
            KeyName = "Dragon Key";
        else if (KeyID == 4)
            KeyName = "Beholder Key";
        else
            KeyName = "MindFlayer Key";
    }
}
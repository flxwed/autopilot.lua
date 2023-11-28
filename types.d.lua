-- Utility Types
type PortLike = number | {GUID: string}
type Iterator<K, V> = () -> (K, V)

-- Microcontroller Types
type EventConnection = {
    Unbind: (self: EventConnection) -> ()
}
type ScreenObject = {
    ChangeProperties: (self: ScreenObject, properties: {[string]: any}) -> (),
    AddChild: (self: ScreenObject, child: ScreenObject) -> (),
    Destroy: (self: ScreenObject) -> ()
}
type Cursor = {
    X: number,
    Y: number,
    Player: string,
    Pressed: boolean
}
type RegionInfo = {
    Name: string,
    Type: "Planet" | "Star",
    SubType: string,
    Color: Color3,
    TidallyLocked: boolean,
    Resources: {string},
    Gravity: number,
    Temperature: number,
    BeaconCount: number,
    HasRings: boolean
}
type RegionLog = {
    {
        Event: "HyperDrive" | "Aliens" | "Spawned" | "Death" | "ExitRegion" | "Poison" | "Irradiated" | "Suffocating" | "Freezing" | "Melting",
        Desc: string,
        TimeAgo: number
    }
}

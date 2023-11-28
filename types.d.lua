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
    Type: "Planet",
    SubType: nil,
    Name: string,
    TidallyLocked: boolean,
    HasRings: boolean,
    BeaconCount: number
} | {
    Type: "Planet",
    SubType: "Desert" | "Terra" | "EarthLike" | "Ocean" | "Tundra" | "Forest" | "Exotic" | "Barren" | "Gas",
    Name: string,
    Color: Color3,
    Resources: { string },
    Gravity: number,
    HasAtmosphere: boolean,
    TidallyLocked: boolean,
    HasRings: boolean,
    BeaconCount: number
} | {
    Type: "BlackHole",
    Name: string,
    Size: number,
    BeaconCount: number
} | {
    Type: "Star",
    SubType: "Red" | "Orange" | "Yellow" | "Blue" | "Neutron",
    Name: string,
    Size: number,
    BeaconCount: number
}
type RegionLog = {
    {
        Event: "HyperDrive" | "Aliens" | "Spawned" | "Death" | "ExitRegion" | "Poison" | "Irradiated" | "Suffocating" | "Freezing" | "Melting",
        Desc: string,
        TimeAgo: number
    }
}

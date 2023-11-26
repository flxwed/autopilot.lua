-- Microcontroller Globals
-- GetPartFromPort and GetPartsFromPort are generated via script
declare GetPort: (port: PortLike) -> Part
declare TriggerPort: (port: PortLike) -> Part

declare SandboxID: string
declare SandboxRunID: number

declare Beep: (pitch: number) -> ()
declare JSONDecode: (json: string) -> {[string]: any}
declare JSONEncode: (dataToEncode: {[string]: any}) -> string
declare Communicate: () -> ()

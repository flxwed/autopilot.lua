import os
import sys
import json

READONLY_PROPERTIES = [
    "ClassName",
    "Position",
    "CFrame",
    "GUID"
]

def _parse_list_dict(listdict: list) -> list[tuple]:
    data = []
    for entry in listdict:
        entry: dict = entry
        if len(entry.items()) != 1:
            raise Exception(f"Expected exactly one entry: {entry}")
        data.append(list(entry.items())[0])
    return data

class PartDefinitionsGenerator():
    def __init__(self, data: dict):
        self.data = data
        self.parts = {}
        self.default_part_name = None

    def _get_part(self, name: str) -> dict | None:
        part = self.data.get(name)
        if part == None:
            return None
        if not part.get("_generated", False):
            self._generate_and_store_part(part)
        return part

    def _generate_part(self, part: dict):
        code = []
        # Copy parent
        if "extends" in part:
            super_part = self._get_part(part["extends"])
            if super_part == None:
                raise Exception(f"Unknown part in extends clause: {part['extends']}")
            for key in ["methods", "properties", "events"]:
                if not key in part:
                    part.update({key: {}})
                part[key].update(super_part.get(key, {}))
        # Set as default part
        if part.get("default", False) == True:
            if self.default_part_name:
                raise Exception(f"{part['_name']} and {self.default_part_name} cannot both be the default part")
            self.default_part_name = part["_name"]
        # Methods
        for method_name, method in part.get("methods", {}).items():
            returns = method.get("returns", "()")
            arguments_code = []
            arguments_code.append(f"self: {part['_name']}")
            if method_name == "Configure":
                # Build Configure method
                configure_code = []
                for property_name, property_value in part.get("properties", {}).items():
                    if property_name in READONLY_PROPERTIES:
                        continue
                    configure_code.append(f"{property_name}: {property_value}?")
                arguments_code.append(f"properties: {{{', '.join(configure_code)}}}")
            else:
                for arg_name, arg_type in _parse_list_dict(method.get("arguments", [])):
                    arguments_code.append(f"{arg_name}: {arg_type}")
            code.append(f"{method_name}: ({', '.join(arguments_code)}) -> {returns}")
        # Properties
        for property_name, property_value in part.get("properties", {}).items():
            code.append(f"{property_name}: {property_value}")
        # Events
        i = -1
        event_code = ""
        for event_name, event in part.get("events", {}).items():
            i += 1
            event_arguments_code = []
            for arg_name, arg_type in _parse_list_dict(event):
                event_arguments_code.append(f"{arg_name}: {arg_type}")
            event_name = f"\"{event_name}\""
            if i == 0:
                event_code += f"Connect: ((self: {part['_name']}, event: {event_name}, callback: ({', '.join(event_arguments_code)}) -> ()) -> EventConnection)"
            else:
                event_code += f"\n        & ((self: {part['_name']}, event: {event_name}, callback: ({', '.join(event_arguments_code)}) -> ()) -> EventConnection)"
        # There cannot be 0 events
        if i == -1:
            raise Exception(f"{part['_name']} has no events? {part}")
        # Finish code
        code.append(event_code)
        code_sep = f",\n    "
        return f"type {part['_name']} = {{\n    {code_sep.join(code)}\n}}"

    def _generate_and_store_part(self, part: dict):
        if self.parts.get(part['_name']): return self.parts[part['_name']]
        generated_part = self._generate_part(part)
        self.parts[part['_name']] = generated_part
        return generated_part

    def generate(self):
        self.parts = {}
        for part_name, part in self.data.items():
            part.update({ "_name": part_name })
            self._generate_and_store_part(part)
        return f"\n".join(list(self.parts.values()))

def main():
    if len(sys.argv) < 2:
        print("Error: parts.json must be passed in as a command-line argument.")
        exit(1)
    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".d.lua"
    try:
        with open(input_file, 'r') as fr:
            parts = json.load(fr)
            part_definitions_generator = PartDefinitionsGenerator(parts)
            part_definitions = part_definitions_generator.generate()
            with open(output_file, 'w+') as fw:
                fw.write("--!nocheck\n" + part_definitions)
                print(f"{output_file} created successfully")
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Unable to parse JSON: {e.msg}")
        exit(1)
    except Exception as e:
        print(f"Error: Failed to generate.", end=" ")
        raise e

if __name__ == "__main__":
    main()

# autopilot.lua

Full code completion for [pilot.lua](https://github.com/iimurpyh/pilot-lua/wiki/) using JohnnyMorganz' Luau Language Server.

## Getting Started

To get started, follow these simple steps:

1. **Download the Definitions File:**
   - Head over to the [Releases](https://github.com/flxwed/autopilot.lua/releases) tab.
   - Download the latest version of the `pilot.d.lua` file.

3. **Install luau-lsp for VSCode:**
   - Install JohnnyMorganz's [luau-lsp](https://github.com/JohnnyMorganz/luau-lsp) extension for Visual Studio Code.

4. **Configure VSCode Settings:**
   - Place `pilot.d.lua` in your project directory.
   - Create a `.vscode` folder in your project directory.
   - Inside the `.vscode` folder, create a `settings.json` file.
   - Add the following properties to `settings.json`:

     ```json
     {
         "luau-lsp.sourcemap.enabled": false,
         "luau-lsp.types.roblox": true,
         "luau-lsp.types.definitionFiles": [
             "./pilot.d.lua"
         ]
     }
     ```

5. **Enjoy Full Code Completion:**
   - With the setup complete, you now have full code completion for `pilot.lua` in Visual Studio Code.

## Build Steps

If you want to build autopilot.lua from scratch, follow the steps below:

1. **Clone the Repository**
   - Clone the repository to your local machine

     ```
     git clone https://github.com/flxwed/autopilot.lua.git
     ```

2. **Generate Definitions via Script**
   - Open your cloned repository in your favorite code editor
   - Run `scripts/generateDefinitions.py` and pass the project directory as the first argument.
   - After the script finishes, the generated code can be found at `build/pilot.d.lua`.

     ```
     py scripts/generateDefinitions.py .
     > .\build\pilot.d.lua created successfully
     cat build/pilot.d.lua
     > type PortLike = number | {GUID: string}
       type Properties = {[string]: any}
       ...
     ```

## Contributions

We welcome contributions and bug reports. Feel free to fork the repository, make your changes, and submit a pull request. If you encounter any issues or have suggestions for improvement, please open an issue.

Happy coding with autopilot.lua!

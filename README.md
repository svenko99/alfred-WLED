# ✨ WLED Workflow for Alfred

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

WLED Alfred workflow enables you to effortlessly control your WLED lights right from your Alfred interface. With this workflow, you can toggle the lights on/off, change colors, switch effects, and choose presets with ease.

## Features

- **Toggle Lights**: Type `toggle` to turn the lights on/off.
- **Change Color**: Type `color <color_name> or <hex>` to change the color of your lights
- **Switch Effects**: Type `effects` to switch to a specific effect
- **Choose Preset**: Type `presets` to switch to a specific preset
- **Open WLED Web Interface**: Type `wled` to open the WLED web interface in your browser

## Installation

1. Download the workflow from the [⤓ GitHub repository](https://github.com/svenko99/alfred-WLED/releases/latest/download/WLED.alfredworkflow).
2. Double-click the downloaded file to install it in Alfred.
3. Put your WLED IP address in `Configure Workflow...` in Alfred (e.g. 192.168.1.23).

## Examples of usage

- Toggle the lights on/off: `toggle`
- Change color to green: `color green` (Workflow supports all [CSS color names](https://www.w3schools.com/tags/ref_colornames.asp).)
- Chnage color to purple using hex: `color #800080`
- Chnage color to blue using hex: `color #0000FF`
- Switch to "Chase" effect: `effects chase`
- Choose preset with name "Blue": `presets Blue`

![Effects](https://github.com/svenko99/alfred-WLED/blob/main/images/effects.png)
![Presets](https://github.com/svenko99/alfred-WLED/blob/main/images/presets.png)

## License

This project is licensed under the MIT License.

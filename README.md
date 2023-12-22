<p align="center">
  <img src="https://github.com/EchterAlsFake/Porn_Fetch/blob/V3.0/src/frontend/graphics/logo_transparent.png" alt="Porn Fetch Logo"/>
</p>

<h1 align="center">Porn Fetch - The Ultimate Open-Source PornHub Downloader</h1>

<p align="center">
  <a href="https://github.com/EchterAlsFake/Porn_Fetch/actions/workflows/python-app.yml"><img src="https://github.com/EchterAlsFake/Porn_Fetch/actions/workflows/python-app.yml/badge.svg" alt="Build Status"/></a>
  <a href="https://github.com/EchterAlsFake/Porn_Fetch/actions/workflows/android.yml"><img src="https://github.com/EchterAlsFake/Porn_Fetch/actions/workflows/android.yml/badge.svg" alt="Android Build"/></a>
  <a href="https://github.com/EchterAlsFake/Porn_Fetch/workflows/CodeQL"><img src="https://github.com/EchterAlsFake/Porn_Fetch/workflows/CodeQL/badge.svg" alt="CodeQL Analysis"/></a>
</p>

<p align="center">
  <a href=="https://github.com/EchterAlsFake/Porn_Fetch/releases/tag/3.0"><strong>Download Version 3.0 (BETA)</strong></a> ·
  <a href="https://github.com/EchterAlsFake/Porn_Fetch/releases/tag/2.9"><strong>Download Version 2.9</strong></a> ·
  <a href="https://github.com/EchterAlsFake/Porn_Fetch/blob/master/README/STATUS.md"><strong>Development Update V3.0</strong></a>
</p>

![Alt text](/relative/path/to/img.jpg?raw=true "Optional Title")

## 🚀 Quick Links
- [Features](#-features)
- [Supported Platforms](#-supported-platforms)
- [How to Build](#-building-from-source)
- [Android Version](#-android)
- [iOS Instructions](#-ios)
- [Translation](#-translating)
- [Useful Resources](#-useful-information)
- [Legal Disclaimer](#-legal-rights)
- [Acknowledgements](#-credits)
- [License Details](#-license)

## 🌟 Features
- Direct downloads from PornHub
- Selectable video quality
- Metadata retrieval
- Full channel/user/model download capabilities
- In-app search and download features
- Optional account login
- Download history management
- Multi-threaded downloading
- Dark mode and CLI support
- No ads or mandatory logins
- Cross-platform compatibility

## 🖥️ Supported Platforms
- Windows 10, 11 (backward compatibility untested)
- Linux (X11 / Wayland)
- macOS (via source build or Python)
- Android (recommended .apk)
- iOS (via iSH)
- ARM (native Python run)

## 🌐 Supported Websites
- [PornHub.com](https://github.com/Egsagon/PHUB)
- [HQPorner.com](https://github.com/EchterAlsFake/hqporner_api)

## 🔨 Building from Source
Easy-to-use build scripts are available for various platforms. Run these in your terminal:

### For Ubuntu, Windows, Arch Linux, Termux, iSH, Fedora, OpenSUSE:
```bash
wget -O - "https://raw.githubusercontent.com/EchterAlsFake/Porn_Fetch/master/src/scripts/install.sh" | bash
```
### For Termux:
```bash
wget -O - "https://raw.githubusercontent.com/EchterAlsFake/Porn_Fetch/master/src/scripts/install_termux.sh" | bash
```
### For Windows (Powershell as Admin)
```
# Enable script execution
Set-ExecutionPolicy RemoteSigned 
Set-ExecutionPolicy Bypass -Scope Process
Invoke-Expression (Invoke-WebRequest -Uri https://raw.githubusercontent.com/EchterAlsFake/Porn_Fetch/master/src/scripts/install_windows.ps1 -UseBasicParsing).Content
```
## 📱 Android
The Android version is in active development. For the latest build, download from [here](https://github.com/EchterAlsFake/Porn_Fetch/releases/tag/2.9).

### Building for Android
Use [this script](https://github.com/EchterAlsFake/Porn_Fetch/blob/master/src/scripts/build_android.sh) to build on Ubuntu 22.04.3.

## 🍏 iOS
### iSH
Run the CLI version of Porn Fetch via the 'iSH' app on iOS.

### Building for iOS
Kivy-based apps can be converted for iOS, but I need community assistance for testing and compiling. Contact me on Discord (echteralsfake | EchterAlsFake#7164) if you can help.

## 🌍 Translating
Currently available in:
- German (3.0)
- English

To contribute a translation, follow [this guide](https://github.com/EchterAlsFake/Porn_Fetch/blob/master/README/TRANSLATING.md).

## 🛠️ Useful Information
- [Roadmap](https://github.com/EchterAlsFake/Porn_Fetch/blob/master/README/ROADMAP.md)
- [Changelog](https://github.com/EchterAlsFake/Porn_Fetch/blob/master/README/CHANGELOG.md)
- [Development Status](https://github.com/EchterAlsFake/Porn_Fetch/blob/master/README/STATUS.md)

## ⚖️ Legal Rights
Important: Usage of Porn Fetch may not be in compliance with PornHub's terms of service. It is recommended to use a VPN for privacy.

## 👏 Credits
- API: [PHUB](https://github.com/Egsagon/PHUB)
- GUI: [Qt](https://qt.io) for Python
### See [Credits]()

## 📚 License
Licensed under [GPL 3](https://www.gnu.org/licenses/gpl-3.0.en.html).
 
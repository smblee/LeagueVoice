# LeagueVoice
Control League of Legends with your voice.

## Installation
### Dependencies
#### pip
1. pip is usually located in `C:\PythonX.X\Scripts\pip.exe`.
2. Spoonfeed version: open CMD and type following (for python 2.7.9 or higher) `C:\Python2.7\Scripts\pip.exe install [target]`
3. If pip does not exist, install it.

#### update pip, setuptools, wheel
1. `pip install --upgrade pip setuptools wheel`

#### Pocketsphinx
1. Install with pip. `pip install --upgrade pocketsphinx`

#### PyAudio
1. Install with pip. `pip install pyaudio`

#### PyInstaller [optional]
1. You need PyInstaller to build the app into `.exe`. Install it with `pip install pyinstaller`
2. You should now have `pyinstaller.exe` in `C:\Python2.7\Scripts\`.

## Build
1. You can build a standalone executable file using the following command `pyinstaller.exe --onefile LeagueVoice.py`
2. The file can be found in `/dist/LeagueVoice.exe`

## Want to contribute?
1. Fork it.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.
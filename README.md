# DumDum - a Music Player

steal inspiration from clementine and quodlibet - but streamlined

## Planned features:

version 1:

* python3.5 / qt5 / qml
* file browser
* music library (sqlite)
* queue
* gstreamer (support all its inputs)
* gapless (hope it's the default)
* pulseaudio output

version 1.5:

* tag editor / fixer(?)
* keyboard operation
* system tray
* system notifications
* cue support

version 2:

* get lyrics
* search library and lyrics

version 3:

* chromecast support
  * play just audio on chromecast audio
  * play visualisations on normal chromecast
  * or display lyrics
  * or just album art

version 4:

* add youtube/soundcloud/mixcloud links in queue

version 10:

* dlna output
* musicbrainz
* macOS/Windows support


## Quick Start

```
export PYTHONUSERBASE=$PWD/py-env
pip install --user -r requirements.txt
python -m dumdum
```

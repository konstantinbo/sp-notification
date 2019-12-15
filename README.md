# sp-notification
Two simple bash scripts to display a notification with metadata of the current playing Spotify song and show notifications after play/pause.

Best use would be binding them to 2 different global key shortcuts, I use &#8984; + S and Ctrl + Spacebar;

Needs the following [script](https://gist.github.com/wandernauta/6800547) and `libnotify-bin` package for `notify-send` (only for the sp-pause-notification script) to work.

Additionally it may be necessarry to install the `gir1.2-notify-0.7` package via `sudo apt-get install gir1.2-notify-0.7`

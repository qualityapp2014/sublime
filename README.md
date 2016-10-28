# sublime plugins repo

This is the repo to provide plugins for sublime. Copy the plugins .py file into sublime package folder. For example, this is one example plugin path for Sublime 3 on Mac OSX.

~/Library/Application Support/Sublime Text 3/Packages/User/RecentFileSwitcher.py

To configure key bindings to launch the plugin via short-cut, follow menu [Preferences] => [Key Bindings].

[
  { "keys": ["super+e"], "command": "recent_file_switcher" },
]

Or to verify the plugin, invoke directly in Sublime Python console. [View] => [Show Console].

window.run_command("recent_file_switcher")

# good luck and enjoy
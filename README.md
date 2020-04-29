# Installation

First copy the plugins .py file to Sublime package folder like `\~/Library/Application Support/Sublime Text 3/Packages/User/RecentFileSwitcher.py` on Mac OS.

Then open [Preferences] => [Key Bindings] to set short-cut keys to launch the plugin. The example below launches the recent file switcher by cmd+e.

```
[
  { "keys": ["super+e"], "command": "recent_file_switcher" },
]
```

To debug, manually launch the plugin in Sublime Python console. [View] => [Show Console].

```
window.run_command("recent_file_switcher")
```

# RecentFileSwitcher

This plugin creates a recent tab view and sort by the last updated timestamp. It allows fast jumps between multiple tabs like in IntelliJ.

- Show recent tabs in selection view
- Auto-save (undeleted file) after the lost of focus

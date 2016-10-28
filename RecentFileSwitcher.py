import sublime
import sublime_plugin
import os
import time

last_timestamp = 'recent_file_switcher_last_timestamp'

# generate quick view for open files based on timestamp and file name
# configure short-cut like { "keys": ["super+e"], "command": "recent_file_switcher" }
class RecentFileSwitcherCommand(sublime_plugin.WindowCommand):

  def run(self):
    self.open_views = []
    self.window = sublime.active_window()

    for view in self.window.views():
      file_name = view.file_name()
      if file_name:
        base_name = os.path.basename(file_name)
        dir_name = os.path.dirname(file_name)
      else:
        base_name = 'untitled'
        dir_name = 'untitled'

      self.open_views.append((view, view.settings().get(last_timestamp, 0), base_name, dir_name))

    # sort view based on last timestamp
    self.open_views.sort(key=lambda view: (-view[1], view[2], view[3]))
    self.open_views.pop(0)

    open_files = []
    for view in self.open_views:
      open_files.append(list(view[2:]))

    self.window.show_quick_panel(open_files, self.view_selected, False, -1)

  def view_selected(self, selected):
    if selected >= 0:
      self.window.focus_view(self.open_views[selected][0])

    return selected

# event listener to record activation time and auto-save after lost focus
class ViewEventListener(sublime_plugin.EventListener):

  def on_activated(self, view):
    view.settings().set(last_timestamp, time.time())

  def on_deactivated_async(self, view):
    if view.is_dirty() and view.file_name():
      view.run_command('save')

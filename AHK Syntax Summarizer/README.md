# AutoHotkey-Syntax-Summarizer
Compile lists of special AHK words for use in syntax-coloring schemes

## _Making a Syntax-Coloring Scheme for AutoHotkey?_
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _…compile lists of Special Words_

### Goal: usable lists
Scrub and compile multiple lists of AutoHotkey keywords to facilitate the creation of syntax-coloring schemes in editors and IDEs. The initial interest was to make a new scheme for EditPad Pro.

The goal was to get good results fast, not perfect results slowly. Perfection would be hard to reach as it isn't always clear which group a word should belong to. These calls are left up to the user.  

### Method: consolidate existing lists in Python
1. Paste unformatted strings of keywords into Python variables.  
2. Consolidate and output.

### How to Use
1. Either use the existing "TL;DR lists" (two formats)
2. Or use the crazy regex-optimized lists in the 'optimize regex' folder (read the warning)
3. Or run `consolidate_ahk_syntax.py`, after adding / modifying lists in `unformatted_lists.py` if needed. 

### Sources: multiple editors
The script uses existing lists from two IDEs:
1. [Scite4AHK](https://www.autohotkey.com/boards/viewtopic.php?f=61&t=62)
2. [Sublime Autohotkey](https://github.com/ahkscript/SublimeAutoHotkey)

Also considered:
1. Two sets from VSCode, but their source was the Sublime file.
2. AHK Studio, but found the file too confusing for this quick job.
3. Links on [this forum post](https://www.autohotkey.com/boards/viewtopic.php?f=74&t=47603), but found it too easy to get lost down the rabbit hole. 

### Discussion and Revision
1. This repo
2. [This forum post](https://www.autohotkey.com/boards/viewtopic.php?f=76&t=63715)


# Hope at least one of you finds this useful. Enjoy!

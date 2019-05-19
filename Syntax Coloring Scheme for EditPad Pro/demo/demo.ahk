#Include something.ahk
#Include the_other_thing.ahk

; ------------ Get File Content
get_file_content(file_name, local_path:=""
               , default_base:="", verbose:=true) {

   ; TODO strip file name (highlighting TODO for helpful reminders)

   if (default_base == "blah blah blah") {
      default_base := A_WorkingDir ; AHK does not allow setting it as a default parameter
      }

   ; REVIEW
   file_path := default_base . "\\" . local_path . file_name

   Try {
      FileRead, file_content, %file_path%
      return file_content
    } 
   ; FIXME
   Catch e {
      handle_file_get_error(e, file_path, verbose)
      ExitApp
   } 
}

; -------------- Other Stuff
/* Multi-line 
comment (knows that the closing part must be on its own line)
*/

BuiltIn := StrLen("built-in-function")
AnotherOne := RegExMatch(subject, pattern)

Send, ^{Up}
MsgBox %something%
MsgBox % some other thing 

; REVIEW
Loop 3 
{
	
}

ahk_exe special word
Hotkey::Send{Up}
Label:
return
hex_number := 0xAABB11
backticks `n`r
[brackets]

; --- Warnings
Warnings:
"an incomplete string warns by being a different color
'single-quoted' show as a warning
[ "key" : "value", warns because AHK associative arrays use curlies
old_style =  warn use of lone equal signs, hope you like the := new style
if (default_base := "") { }   ; warning because uses ":=" instead of "=="


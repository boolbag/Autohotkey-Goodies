#
# Flow Control
#

flow_scite = """break continue else exit exitapp gosub goto 
loop pause return settimer sleep suspend
static global local byref while until for class try catch throw finally"""

flow_sublime =   """if|else|return|loop|break|for|while|class|extends|catch|finally|throw|try|until|continue|critical|exit|exitapp|gosub|goto||not|or|and|is|in"""

#
# Built-Ins
#

built_ins_scite = """abs acos asc asin atan ceil chr cos dllcall exp fileexist floor getkeystate numget numput registercallback \
il_add il_create il_destroy instr islabel isfunc ln log lv_add lv_delete lv_deletecol \
lv_getcount lv_getnext lv_gettext lv_insert lv_insertcol lv_modify \
lv_modifycol lv_setimagelist mod onmessage round \
regexmatch regexreplace \
sb_seticon sb_setparts sb_settext sin sqrt strlen substr tan \
tv_add tv_delete tv_getchild tv_getcount tv_getnext tv_get tv_getparent \
tv_getprev tv_getselection tv_gettext tv_modify tv_setimagelist \
varsetcapacity winactive winexist \
trim ltrim rtrim fileopen strget strput \
object array isobject objinsert objremove objminindex objmaxindex objsetcapacity objgetcapacity \
objgetaddress objnewenum objaddref objrelease objhaskey objclone objbindmethod \
_newenum comobjcreate comobjget comobjconnect comobjerror \
comobjactive comobject comobjenwrap comobjunwrap comobjmissing comobjtype comobjvalue comobjarray \
comobjquery comobjflags func \
getkeyname getkeyvk getkeysc isbyref exception strsplit format \
onexit onclipboardchange \
objinsertat objpush objrawset objdelete objremoveat objpop objlength \
ord strreplace"""

built_ins_sublime = """abs|acos|asc|asin|atan|ceil|chr|cos|comobjcreate|comobjactive|comobjarray|comobjconnect|comobjenwrap|comobjerror|comobjflags|comobjget|comobjmissing|comobjparameter|comobjquery|comobjtype|comobjunwrap|comobjvalue|dllcall|exp|fileexist|fileopen|floor|format|func|getkeyname|getkeyvk|getkeysc|getkeystate|il_add|il_create|il_destroy|instr|isbyref|isfunc|islabel|isobject|ln|log|ltrim|lv_add|lv_delete|lv_deletecol|lv_getcount|lv_getnext|lv_gettext|lv_insert|lv_insertcol|lv_modifycol|lv_modify|lv_setimagelist|mod|onmessage|numget|numput|regexmatch|regexreplace|registercallback|round|rtrim|sb_seticon|sb_setparts|sb_settext|sin|sqrt|strget|strlen|strput|strsplit|strreplace|substr|tan|trim|tv_add|tv_delete|tv_getchild|tv_getcount|tv_getnext|tv_get|tv_getparent|tv_getprev|tv_getselection|tv_gettext|tv_modify|varsetcapacity|winactive|winexist"""

built_ins_sublime += """read|write|readline|writeline|readuint|readint|readint64|readshort|readushort|readchar|readuchar|readdouble|readfloat|writeuint|writeint|writeint64|writeshort|writeushort|writechar|writeuchar|writedouble|writefloat|rawread|rawwrite|seek|tell|close|insert|remove|minindex|maxindex|setcapacity|getcapacity|getaddress|newenum|haskey|clone|isoptional|__new|__call|__get|__set|__delete"""

built_ins_sublime += """length|ateof|encoding|__handle|name|isbuiltin|isvariadic|minparams|maxparams|position|pos"""

#
# Directives
#

directives_scite = """clipboardtimeout commentflag errorstdout escapechar \
hotkeyinterval hotkeymodifiertimeout hotstring if iftimeout ifwinactive ifwinexist include \
includeagain inputlevel installkeybdhook installmousehook keyhistory ltrim \
maxhotkeysperinterval maxmem maxthreads maxthreadsbuffer maxthreadsperhotkey menumaskkey \
noenv notrayicon persistent singleinstance usehook warn winactivateforce \
ifwinnotactive ifwinnotexist"""

directives_sublime = """allowsamelinecomments|clipboardtimeout|commentflag|errorstdout|escapechar|hotkeyinterval|hotkeymodifiertimeout|hotstring|iftimeout|ifwinactive|ifwinexist|ifwinnotactive|ifwinnotexist|if|inputlevel|installkeybdhook|installmousehook|keyhistory|ltrim|maxhotkeysperinterval|maxmem|maxthreadsbuffer|maxthreadsperhotkey|maxthreads|menumaskkey|noenv|notrayicon|persistent|singleinstance|usehook|warn|winactivateforce"""

#
# Commands
#

commands_scite = """autotrim blockinput clipwait control controlclick controlfocus \
controlget controlgetfocus controlgetpos controlgettext controlmove \
controlsend controlsendraw controlsettext coordmode critical detecthiddentext \
detecthiddenwindows drive driveget drivespacefree edit envadd \
envdiv envget envmult envset envsub envupdate fileappend filecopy \
filecopydir filecreatedir filecreateshortcut filedelete filegetattrib \
filegetshortcut filegetsize filegettime filegetversion fileinstall filemove \
filemovedir fileread filereadline filerecycle filerecycleempty fileremovedir \
fileselectfile fileselectfolder filesetattrib filesettime formattime \
getkeystate groupactivate groupadd groupclose groupdeactivate gui \
guicontrol guicontrolget hotkey \
imagesearch inidelete iniread iniwrite input inputbox keyhistory keywait \
listhotkeys listlines listvars menu mouseclick mouseclickdrag mousegetpos \
mousemove msgbox outputdebug pixelgetcolor pixelsearch \
postmessage process progress random regdelete regread regwrite reload \
run runas runwait \
send sendevent sendinput sendlevel sendmessage sendmode sendplay sendraw \
setbatchlines setcapslockstate setcontroldelay setdefaultmousespeed setenv setformat \
setkeydelay setmousedelay setnumlockstate setscrolllockstate \
setstorecapslockmode settitlematchmode setwindelay setworkingdir \
shutdown sort soundbeep soundget soundgetwavevolume soundplay soundset \
soundsetwavevolume splashimage splashtextoff splashtexton splitpath \
statusbargettext statusbarwait stringcasesense stringgetpos stringleft \
stringlen stringlower stringmid stringreplace stringright stringsplit \
stringtrimleft stringtrimright stringupper sysget thread tooltip \
transform traytip urldownloadtofile winactivate winactivatebottom winclose \
winget wingetactivestats wingetactivetitle wingetclass wingetpos wingettext \
wingettitle winhide winkill winmaximize winmenuselectitem winminimize \
winminimizeall winminimizeallundo winmove winrestore winset winsettitle \
winshow winwait winwaitactive winwaitclose winwaitnotactive fileencoding setregview"""


commands_scite += """\ifequal ifexist ifgreater ifgreaterorequal ifinstring \
ifless iflessorequal ifmsgbox ifnotequal ifnotexist ifnotinstring ifwinactive \
ifwinexist ifwinnotactive ifwinnotexist"""

commands_sublime = """autotrim|blockinput|click|clipwait|controlclick|controlfocus|controlget|controlgetfocus|controlgetpos|controlgettext|controlmove|controlsend|controlsendraw|controlsettext|control|coordmode|detecthiddentext|detecthiddenwindows|driveget|drivespacefree|drive|edit|envadd|envdiv|envget|envmult|envset|envsub|envupdate|fileappend|filecopydir|filecopy|filecreatedir|filecreateshortcut|filedelete|fileencoding|filegetattrib|filegetshortcut|filegetsize|filegettime|filegetversion|fileinstall|filemovedir|filemove|filereadline|fileread|filerecycleempty|filerecycle|fileremovedir|fileselectfile|fileselectfolder|filesetattrib|filesettime|formattime|getkeystate|groupactivate|groupadd|groupclose|groupdeactivate|guicontrol|guicontrolget|gui|hotkey|ifequal|ifexist|ifgreater|ifgreaterorequal|ifinstring|ifless|iflessorequal|ifmsgbox|ifnotequal|ifnotexist|ifnotinstring|ifwinactive|ifwinexist|ifwinnotactive|ifwinnotexist|imagesearch|inidelete|iniread|iniwrite|inputbox|input|keyhistory|keywait|listhotkeys|listlines|listvars|menu|mouseclickdrag|mouseclick|mousegetpos|mousemove|msgbox|onexit|outputdebug|pause|pixelgetcolor|pixelsearch|postmessage|process|progress|random|regdelete|regread|regwrite|reload|run|runas|runwait|sendevent|sendinput|sendlevel|sendmessage|sendmode|sendplay|sendraw|send|setbatchlines|setcapslockstate|setcontroldelay|setdefaultmousespeed|setenv|setformat|setkeydelay|setmousedelay|setnumlockstate|setscrolllockstate|setstorecapslockmode|setregview|settimer|settitlematchmode|setwindelay|setworkingdir|shutdown|sleep|sort|soundbeep|soundgetwavevolume|soundget|soundplay|soundsetwavevolume|soundset|splashimage|splashtextoff|splashtexton|splitpath|statusbargettext|statusbarwait|stringcasesense|stringgetpos|stringleft|stringlen|stringlower|stringmid|stringreplace|stringright|stringsplit|stringtrimleft|stringtrimright|stringupper|suspend|sysget|thread|tooltip|transform|traytip|urldownloadtofile|winactivatebottom|winactivate|winclose|wingetactivestats|wingetactivetitle|wingetclass|wingetpos|wingettext|wingettitle|winget|winhide|winkill|winmaximize|winmenuselectitem|winminimizeallundo|winminimizeall|winminimize|winmove|winrestore|winsettitle|winset|winshow|winwaitactive|winwaitclose|winwaitnotactive|winwait"""

#
# Variables
#

variables_scite = """a_ahkpath a_ahkversion a_appdata a_appdatacommon a_autotrim a_batchlines \
a_caretx a_carety a_computername a_controldelay a_cursor \
a_dd a_ddd a_dddd a_defaultmousespeed a_desktop a_desktopcommon \
a_detecthiddentext a_detecthiddenwindows a_endchar \
a_eventinfo a_exitreason a_formatfloat a_formatinteger a_gui a_guievent \
a_guicontrol a_guicontrolevent a_guiheight a_guiwidth a_guix a_guiy a_hour \
a_iconfile a_iconhidden a_iconnumber a_icontip a_index \
a_ipaddress1 a_ipaddress2 a_ipaddress3 a_ipaddress4 a_isadmin a_iscompiled \
a_issuspended a_keydelay a_language a_lasterror a_linefile a_linenumber \
a_loopfield a_loopfileattrib a_loopfiledir a_loopfileext a_loopfilefullpath \
a_loopfilelongpath a_loopfilename a_loopfileshortname a_loopfileshortpath \
a_loopfilesize a_loopfilesizekb a_loopfilesizemb a_loopfiletimeaccessed \
a_loopfiletimecreated a_loopfiletimemodified a_loopreadline a_loopregkey \
a_loopregname a_loopregsubkey a_loopregtimemodified a_loopregtype \
a_mday a_min a_mm a_mmm a_mmmm a_mon a_mousedelay a_msec a_mydocuments \
a_now a_nowutc a_numbatchlines a_ostype a_osversion a_priorhotkey \
a_programfiles a_programs a_programscommon a_screenheight a_screenwidth \
a_scriptdir a_scriptfullpath a_scriptname a_sec a_space a_startmenu \
a_startmenucommon a_startup a_startupcommon a_stringcasesense a_tab a_temp \
a_thishotkey a_thismenu a_thismenuitem a_thismenuitempos a_tickcount \
a_timeidle a_timeidlephysical a_timesincepriorhotkey a_timesincethishotkey \
a_titlematchmode a_titlematchmodespeed a_username a_wday a_windelay a_windir \
a_workingdir a_yday a_year a_yweek a_yyyy \
clipboard clipboardall comspec errorlevel programfiles \
true false a_thisfunc a_thislabel a_ispaused a_iscritical a_isunicode a_ptrsize \
a_scripthwnd a_priorkey a_is64bitos a_regview a_screendpi a_fileencoding
"""
variables_sublime = """a_ahkpath|a_ahkversion|a_appdata|a_appdatacommon|a_autotrim|a_batchlines|a_caretx|a_carety|a_computername|a_controldelay|a_cursor|a_dd|a_ddd|a_dddd|a_defaultmousespeed|a_desktop|a_desktopcommon|a_detecthiddentext|a_detecthiddenwindows|a_endchar|a_eventinfo|a_exitreason|a_fileencoding|a_formatfloat|a_formatinteger|a_gui|a_guievent|a_guicontrol|a_guicontrolevent|a_guiheight|a_guiwidth|a_guix|a_guiy|a_hour|a_iconfile|a_iconhidden|a_iconnumber|a_icontip|a_index|a_ipaddress1|a_ipaddress2|a_ipaddress3|a_ipaddress4|a_is64bitos|a_isadmin|a_iscompiled|a_iscritical|a_ispaused|a_issuspended|a_isunicode|a_keydelay|a_language|a_lasterror|a_linefile|a_linenumber|a_loopfield|a_loopfileattrib|a_loopfiledir|a_loopfileext|a_loopfilefullpath|a_loopfilelongpath|a_loopfilename|a_loopfileshortname|a_loopfileshortpath|a_loopfilesize|a_loopfilesizekb|a_loopfilesizemb|a_loopfiletimeaccessed|a_loopfiletimecreated|a_loopfiletimemodified|a_loopreadline|a_loopregkey|a_loopregname|a_loopregsubkey|a_loopregtimemodified|a_loopregtype|a_mday|a_min|a_mm|a_mmm|a_mmmm|a_mon|a_mousedelay|a_msec|a_mydocuments|a_now|a_nowutc|a_numbatchlines|a_ostype|a_osversion|a_priorhotkey|a_priorkey|a_programfiles|a_programs|a_programscommon|a_ptrsize|a_regview|a_screendpi|a_screenheight|a_screenwidth|a_scriptdir|a_scriptfullpath|a_scripthwnd|a_scriptname|a_sec|a_space|a_startmenu|a_startmenucommon|a_startup|a_startupcommon|a_stringcasesense|a_tab|a_temp|a_thisfunc|a_thishotkey|a_thislabel|a_thismenu|a_thismenuitem|a_thismenuitempos|a_tickcount|a_timeidle|a_timeidlephysical|a_timesincepriorhotkey|a_timesincethishotkey|a_titlematchmode|a_titlematchmodespeed|a_username|a_wday|a_windelay|a_windir|a_workingdir|a_yday|a_year|a_yweek|a_yyyy|clipboard|clipboardall|comspec|errorlevel|programfiles|true|false"""

#
# Keys
#

keys_scite = """shift lshift rshift alt lalt ralt control lcontrol rcontrol \
ctrl lctrl rctrl lwin rwin appskey \
altdown altup shiftdown shiftup ctrldown ctrlup \
lwindown lwinup rwindown rwinup \
lbutton rbutton mbutton wheelup wheeldown xbutton1 xbutton2 \
joy1 joy2 joy3 joy4 joy5 joy6 joy7 joy8 joy9 joy10 joy11 joy12 joy13 joy14 \
joy15 joy16 joy17 joy18 joy19 joy20 joy21 joy22 joy23 joy24 joy25 joy26 joy27 \
joy28 joy29 joy30 joy31 joy32 \
joyx joyy joyz joyr joyu joyv joypov joyname joybuttons joyaxes joyinfo \
space tab enter escape esc backspace bs delete del insert ins pgup pgdn \
home end up down left right \
printscreen ctrlbreak pause scrolllock capslock numlock \
numpad0 numpad1 numpad2 numpad3 numpad4 numpad5 numpad6 numpad7 numpad8 numpad9 \
numpadmult numpadadd numpadsub numpaddiv numpaddot numpaddel numpadins \
numpadclear numpadup numpaddown numpadleft numpadright numpadhome numpadend \
numpadpgup numpadpgdn numpadenter \
f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 \
f13 f14 f15 f16 f17 f18 f19 f20 f21 f22 f23 f24 \
browser_back browser_forward browser_refresh browser_stop browser_search \
browser_favorites browser_home volume_mute volume_down volume_up \
media_next media_prev media_stop media_play_pause \
launch_mail launch_media launch_app1 launch_app2 \
blind click raw wheelleft wheelright"""

keys_sublime = """shift|lshift|rshift|alt|lalt|ralt|control|lcontrol|rcontrol|ctrl|lctrl|rctrl|lwin|rwin|appskey|altdown|altup|shiftdown|shiftup|ctrldown|ctrlup|lwindown|lwinup|rwindown|rwinup|lbutton|rbutton|mbutton|wheelup|wheelleft|wheelright|wheeldown|xbutton1|xbutton2|joy1|joy2|joy3|joy4|joy5|joy6|joy7|joy8|joy9|joy10|joy11|joy12|joy13|joy14|joy15|joy16|joy17|joy18|joy19|joy20|joy21|joy22|joy23|joy24|joy25|joy26|joy27|joy28|joy29|joy30|joy31|joy32|joyx|joyy|joyz|joyr|joyu|joyv|joypov|joyname|joybuttons|joyaxes|joyinfo|space|tab|enter|escape|esc|backspace|bs|delete|del|insert|ins|pgup|pgdn|home|end|up|down|left|right|printscreen|ctrlbreak|pause|scrolllock|capslock|numlock|numpad0|numpad1|numpad2|numpad3|numpad4|numpad5|numpad6|numpad7|numpad8|numpad9|numpadmult|numpadadd|numpadsub|numpaddiv|numpaddot|numpaddel|numpadins|numpadclear|numpadup|numpaddown|numpadleft|numpadright|numpadhome|numpadend|numpadpgup|numpadpgdn|numpadenter|f1|f2|f3|f4|f5|f6|f7|f8|f9|f10|f11|f12|f13|f14|f15|f16|f17|f18|f19|f20|f21|f22|f23|f24|browser_back|browser_forward|browser_refresh|browser_stop|browser_search|browser_favorites|browser_home|volume_mute|volume_down|volume_up|media_next|media_prev|media_stop|media_play_pause|launch_mail|launch_media|launch_app1|launch_app2"""

#
# Keywords
#

keywords_scite = """ltrim rtrim join \
ahk_id ahk_pid ahk_class ahk_group ahk_exe \
processname processpath minmax controllist statuscd filesystem setlabel \
alwaysontop mainwindow nomainwindow useerrorlevel \
altsubmit hscroll vscroll imagelist wantctrla wantf2 vis visfirst \
wantreturn backgroundtrans \
minimizebox maximizebox sysmenu toolwindow exstyle \
check3 checkedgray readonly notab \
lastfound lastfoundexist \
alttab shiftalttab alttabmenu alttabandmenu alttabmenudismiss \
controllisthwnd hwnd \
deref pow bitnot bitand bitor bitxor bitshiftleft bitshiftright \
sendandmouse mousemove mousemoveoff \
hkey_local_machine hkey_users hkey_current_user hkey_classes_root \
hkey_current_config hklm hku hkcu hkcr hkcc \
reg_sz reg_expand_sz reg_multi_sz reg_dword reg_qword reg_binary \
reg_link reg_resource_list reg_full_resource_descriptor \
reg_resource_requirements_list reg_dword_big_endian \
regex \
pixel mouse screen relative rgb \
low belownormal normal abovenormal high realtime \
between contains in is integer float number digit xdigit \
integerfast floatfast \
alpha upper lower alnum time date \
not or and \
topmost top bottom transparent transcolor redraw region id idlast \
count list capacity eject lock unlock \
label serial type status \
seconds minutes hours days \
read parse \
logoff close error single shutdown menu exit reload \
tray add rename check uncheck togglecheck enable disable toggleenable default \
nodefault standard nostandard color delete deleteall icon noicon tip click \
show \
edit progress hotkey text picture pic groupbox button link \
checkbox radio dropdownlist ddl combobox statusbar treeview \
listbox listview datetime monthcal updown slider tab tab2 activex custom \
iconsmall tile report sortdesc nosort nosorthdr grid hdr autosize range \
xm ym ys xs xp yp dpiscale \
font resize owner submit nohide minimize maximize restore noactivate na \
cancel destroy center \
margin owndialogs guiescape guiclose guisize guicontextmenu guidropfiles \
tabstop section wrap border top bottom buttons \
expand first lines \
number uppercase lowercase limit password multi group background \
bold italic strike underline norm theme caption delimiter \
flash style checked \
password hidden left right center section move \
focus hide choose choosestring text pos enabled disabled visible \
notimers interrupt priority waitclose unicode tocodepage fromcodepage\
yes no ok cancel abort retry ignore force \
on off all send wanttab \
monitorcount monitorprimary monitorname \
monitorworkarea pid \
this base extends __get __set __call __delete __new new \
useunsetlocal useunsetglobal useenv localsameasglobal"""

keywords_sublime = """pixel|mouse|screen|relative|rgb|ltrim|rtrim|join|low|belownormal|normal|abovenormal|high|realtime|ahk_id|ahk_pid|ahk_class|ahk_group|between|containsinteger|float|integerfast|floatfast|number|digit|xdigit|alpha|upper|lower|alnum|time|date|alwaysontop|topmost|top|bottom|transparent|transcolor|redraw|region|id|idlast|processname|minmax|controllist|count|list|capacity|statuscd|eject|lock|unlock|label|filesystem|label|setlabel|serial|type|status|static|global|local|byref|seconds|minutes|hours|days|read|parse|logoff|close|error|single|tray|add|rename|check|uncheck|togglecheck|enable|disable|toggleenable|default|nodefault|standard|nostandard|color|delete|deleteall|icon|noicon|tip|click|show|mainwindow|nomainwindow|useerrorlevel|text|picture|pic|groupbox|button|checkbox|radio|dropdownlist|ddl|combobox|listbox|listview|datetime|monthcal|updown|slider|tab|tab2|statusbar|treeview|iconsmall|tile|report|sortdesc|nosort|nosorthdr|grid|hdr|autosize|range|xm|ym|ys|xs|xp|yp|font|resize|owner|submit|nohide|minimize|maximize|restore|noactivate|na|cancel|destroy|center|margin|maxsize|minsize|owndialogs|guiescape|guiclose|guisize|guicontextmenu|guidropfiles|tabstop|section|altsubmit|wrap|hscroll|vscroll|border|top|bottom|buttons|expand|first|imagelist|lines|wantctrla|wantf2|vis|visfirst|number|uppercase|lowercase|limit|password|multi|wantreturn|group|background|bold|italic|strike|underline|norm|backgroundtrans|theme|caption|delimiter|minimizebox|maximizebox|sysmenu|toolwindow|flash|style|exstyle|check3|checked|checkedgray|readonly|password|hidden|left|right|center|notab|section|move|focus|hide|choose|choosestring|text|pos|enabled|disabled|visible|lastfound|lastfoundexist|alttab|shiftalttab|alttabmenu|alttabandmenu|alttabmenudismiss|notimers|interrupt|priority|waitclose|blind|raw|unicode|deref|pow|bitnot|bitand|bitor|bitxor|bitshiftleft|bitshiftright|yes|no|ok|cancel|abort|retry|ignore|tryagain|on|off|all|hkey_local_machine|hkey_users|hkey_current_user|hkey_classes_root|hkey_current_config|hklm|hku|hkcu|hkcr|hkcc|reg_sz|reg_expand_sz|reg_multi_sz|reg_dword|reg_qword|reg_binary|reg_link|reg_resource_list|reg_full_resource_descriptor|reg_resource_requirements_list|reg_dword_big_endian|alwayson|alwaysoff|dpiscale|parent"""


import re
from unformatted_lists import *

splitter = re.compile('[|\s\\\]+')


def word_list_from_strings(*args):
    """Takes multiple raw (unformatted) strings of syntax tokens.
       Returns sorted list of unique words."""
    big_list = sum((splitter.split(l) for l in args), [])
    token_list = list(set(t for t in big_list))
    token_list.sort()
    return token_list


flow_control_words = word_list_from_strings(flow_scite, flow_sublime)
directive_words = word_list_from_strings(directives_scite, directives_sublime)
built_in_words = word_list_from_strings(built_ins_scite, built_ins_sublime)
command_words = word_list_from_strings(commands_scite, commands_sublime)
variables_words = word_list_from_strings(variables_scite, variables_sublime)
keywords_words = word_list_from_strings(keywords_scite, keywords_sublime)
keys_words = word_list_from_strings(keys_scite, keys_sublime)

language = {"Flow Control": flow_control_words,
            "Directives": directive_words,
            "Built-Ins": built_in_words,
            "Commands": command_words,
            "Variables": variables_words,
            "Keywords": keywords_words,
            "Keys": keys_words}

print("###\n### Autohotkey Words ###\n###")
print("\n#\n# Format #1: regex-ready lists (separated by the pipe character)\n#")

for k in language:
    print("\n\n## " + k + " ##")
    print("|".join(language[k]))

print("\n\n#\n# Format #2: long lists\n#")

for k in language:
    print("\n\n## " + k + " ##")
    print("\n".join(language[k]))


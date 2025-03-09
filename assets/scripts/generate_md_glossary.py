"""
Creates a glossary of terms relevant to the
Genetic Evolution Tournament in Markdown from
the glossaries of several books and online
resources. Terms were pulled from sources and
passed to ChatGPT o3-mini-high to convert into
dictionaries. The initial letter in each term
word was capitalized.
"""

# %% LIBRARIES IMPORTED

import json 

# %% READ IN GLOSSARY FILE

with open("glossary.json", "r") as f:
    glossary = json.load(f)
print(glossary)

# %%

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

import itertools as it
import json

# %% READ IN GLOSSARY FILE

with open("glossary.json") as f:
    glossary = json.load(f)
terms_and_defs = [glossary[k]["terms"] for k in glossary]
terms_unsorted = [d.keys() for d in terms_and_defs]
terms_sorted = list(it.chain.from_iterable(terms_unsorted))

# %% CLEAN TERMS


def generate_markdown(
    dict_list: list[dict[str, str]], output_filename: str = "output.md"
):
    # all unique keys from all dictionaries
    unique_keys = set()
    for d in dict_list:
        unique_keys.update(d.keys())
    # sort keys alphabetically (case-insensitive)
    sorted_keys = sorted(unique_keys, key=lambda x: x.lower())
    # collect unique values for each key
    key_values = {key: set() for key in sorted_keys}
    for d in dict_list:
        for key, value in d.items():
            # convert value to string for consistent formatting
            key_values[key].add(str(value))
    # write the markdown file
    with open(output_filename, "w") as md_file:
        for key in sorted_keys:
            # write the key in bold
            md_file.write(f"**{key}**\n")
            # sort the values alphabetically (case-insensitive)
            # and write each as a list item
            md_file.write("\n")
            for value in sorted(key_values[key], key=lambda x: x.lower()):
                md_file.write(f"- {value}\n")
            md_file.write("\n")
    print(f"Markdown file '{output_filename}' has been created.")


generate_markdown(dict_list=terms_and_defs, output_filename="glossary.md")


# %% TODOS

# Make unique terms case insensitive
# Make outputted terms capitalized
# Use Re to remove (ACRONYMS)
# Add attribution to source

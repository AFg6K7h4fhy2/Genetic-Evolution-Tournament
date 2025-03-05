"""
Generates skeleton question files for the
five GET groups so the author does not have
manually create them.
"""

# %% LIBRARY IMPORTS

import glob
import os

# %% BASELINE QUESTION CONTENT

baseline_question_content = """
#

## Background Information

## Resolution Criteria

### Fine Print
"""

# %% GENERATE QUESTION FILES

target_dir = "../../website/"
dirs_to_make = ["q_ELSI", "q_TACA", "q_RPD", "q_ADS", "q_HISE"]
current_dir = os.getcwd()

for d in dirs_to_make:
    target_q_dir = os.path.join(target_dir, d)
    # check if the directory exists, if not
    # create it
    if not os.path.exists(target_q_dir):
        os.makedirs(target_q_dir)
    # range of questions to make
    q_range = list(range(1, 30 + 1))
    q_files = [
        f"{d}_0{elt}.qmd" if elt <= 9 else f"{d}_{elt}.qmd" for elt in q_range
    ]
    q_files_full = [f"{target_q_dir}/{q_file}" for q_file in q_files]
    # get all files in the target question dir
    existing_q_files = glob.glob(f"{target_q_dir}/*.qmd")
    not_yet_created_q_files = [
        q_f for q_f in q_files_full if q_f not in existing_q_files
    ]
    for q_f in not_yet_created_q_files:
        # create the not yet existing file
        with open(q_f, "w") as f:
            f.write(baseline_question_content)
        print(f"Created: {q_f}")


# %%

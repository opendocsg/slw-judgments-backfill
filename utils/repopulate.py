import re
from typing import Text, Dict

import Levenshtein


def isCapitalized(word: Text) -> bool:
    """Checks if word starts with a capital letter.
    Return True if yes, False otherwise."""
    return word[0].isupper()


def infer_case_number(start_id_of_known_case_num: int,
                      end_id_of_known_case_num: int,
                      document: Text) -> Text:
    """Assume case number starts with [dddd] (e.g. [1980], [2017]),
    is following by only number or capitalized words,
    and ends with a number (e.g. [1980] SGHC 1).

    `start_id_of_known_case_num` is the index of the open square bracket ([)
    and `end_id_of_known_case_num` is the index of the close square bracket (]).

    Given `start_id_of_known_case_num` and `end_id_of_known_case_num`,
    look through `document` and extract the entire case number.

    Return the entire case number as Text.
    """
    char_after_case_number = document[end_id_of_known_case_num: (end_id_of_known_case_num + 100)]
    case_number = [document[start_id_of_known_case_num: end_id_of_known_case_num]]

    # Case numbers should have numbers of capitalized words only
    for word in char_after_case_number.split():
        if word.isdigit() or isCapitalized(word):
            case_number.append(word)
        elif (word[-1] == ',' or word[-1] == '.') and word[:-1].isdigit():
            case_number.append(word[:-1])
            break
        else:
            break
    case_number = ' '.join(case_number)

    # Case number has to end with numbers
    if not case_number[-1].isdigit():
        case_number = ''

    return case_number


def get_text_with_min_levenshtein_dist(target_text: Text, document: Text) -> Text:
    """
    Search within `document` to find a string of text with same number of words and the
    smallest Levenshtein distance from `target_text`.
    """
    all_levenshtein_distances = []
    document_word_list = document.split()
    num_target_words = len(target_text.split())

    for i in range((len(document_word_list) - num_target_words + 1)):
        comparison_text = ' '.join(document_word_list[i: (i + num_target_words)])
        distance = Levenshtein.distance(comparison_text, target_text)
        all_levenshtein_distances.append(distance)

    min_dist_i = all_levenshtein_distances.index(min(all_levenshtein_distances))
    min_dist_text = ' '.join(document_word_list[min_dist_i: (min_dist_i + num_target_words)])

    return min_dist_text


def fuzzy_find_text_in_document(text: Text,
                                document: Text) -> int:
    """Search for `text` within `document`.
    If exact match of `text` cannot be found within `document`,
    shorten `text` from left until an exact match is found.

    Return index in `document` where `text` ends."""
    while True:
        if document.find(text) == -1:
            text = text[1:]
        else:
            break

    return document.index(text) + len(text)


def repopulate(old_md: Text, new_md: Text) -> Dict:
    """Add missing case numbers that are present in `new_md` but not in `old_md`.
    Return a dictionary of case numbers added, and repopulated markdown file"""

    # Find all occurrences of (dddd) and [dddd]
    _iter = re.finditer(r"(\[|\()\d{4}(\]|\))", new_md)

    old_repopulated_md = ''
    case_numbers_added = []
    prev_o_id_add_case_num = 0
    for i in _iter:
        # Extract all occurrences of full case numbers from `new_md`
        case_number = infer_case_number(start_id_of_known_case_num=i.span()[0],
                                        end_id_of_known_case_num=i.span()[1],
                                        document=new_md)
        if len(case_number) == 0:
            continue

        # If case number is already in `old_num`, skip case number
        if old_md.find(case_number) != -1 or old_md.replace("\\[", "[").replace("\\]", "]").replace('\xa0', ' ').find(
                case_number) != -1:
            continue

        case_numbers_added.append(case_number)

        # Find 100 characters before start of case number
        char_before_case_number = new_md[max(0, i.span()[0] - 100):i.span()[0]]

        # Get index location in `old_md` to add case number
        if old_md.find(char_before_case_number) != -1:
            o_id_add_case_num = old_md.index(char_before_case_number) + len(char_before_case_number)
        else:
            # If exact match doesn't exist, use Levenshtein distance to find most similar text
            fuzzy_md_char_before_case_number = get_text_with_min_levenshtein_dist(target_text=char_before_case_number,
                                                                                  document=old_md)
            # Crudely make sure that we are not repopulating case number into an html tag
            if fuzzy_md_char_before_case_number.split()[-1][0] == '<':
                fuzzy_md_char_before_case_number = ' '.join(fuzzy_md_char_before_case_number.split()[:-1])

            o_id_add_case_num = fuzzy_find_text_in_document(text=fuzzy_md_char_before_case_number,
                                                            document=old_md)

        # Add full case number to old_md
        if len(old_repopulated_md) == 0:
            old_repopulated_md += old_md[:o_id_add_case_num] + ' ' + case_number + ' '
        else:
            old_repopulated_md += old_md[prev_o_id_add_case_num:o_id_add_case_num] + ' ' + case_number + ' '

        prev_o_id_add_case_num = o_id_add_case_num

    # Add remaining text from `old_md` to `old_repopulated_md`
    old_repopulated_md += ' ' + old_md[prev_o_id_add_case_num:]

    return {'case_numbers': case_numbers_added,
            'repopulated_md': old_repopulated_md}

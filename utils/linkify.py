"""Add hyperlink to each legal citation found in legal documents"""

import re
from functools import partial


def extract_citations(document, pattern):
    """Finds regex `pattern` in `document`.
    Returns start and end index of citation."""

    _iter = re.finditer(pattern, document)
    return {i.span() for i in _iter}


# Neutral citations should start with a blank space( ), square bracket([), round bracket((), newline(\n), # asterisk(*), or underscore(_),
# followed by 4 digits in square brackets, a blank space,
# text "SGCA", "SGHC" or "SGDC", a blank space, and end with any number of digits
extract_neutral_citations = partial(extract_citations, pattern=r"(?<= |\[|\(|\n|\*|\_)\[\d{4}\] (SGCA|SGHC|SGDC) \d+")

# Reported citations should start with a blank space( ), square bracket([), round bracket((), newline(\n), asterisk(*), or underscore(_),
# followed by 4 digits in square brackets, a blank space,
# any number of digits, text "SLR" or "SLR(R)", a blank space, and end with any number of digits
extract_reported_citations = partial(extract_citations,
                                     pattern=r"(?<= |\[|\(|\n|\*|\_)\[\d{4}\] \d+ (SLR|SLR\(R\)) \d+")

# Citations which start with a forward slash(/) are part of a url
# (e.g. https://www.website.sg/documents/[2010] SGCA 11)
extract_filename_neutral_citations = partial(extract_citations, pattern=r"(?<=\/)\[\d{4}\] (SGCA|SGHC|SGDC) \d+")
extract_filename_reported_citations = partial(extract_citations, pattern=r"(?<=\/)\[\d{4}\] \d+ (SLR|SLR\(R\)) \d+")

# Citations which have already been identified and linked will be wrapped by square brackets
# and superceded by a round open bracket(()
# e.g. [[2010] SGCA 11]("https://www.open.gov.sg")
extract_linked_neutral_citations = partial(extract_citations, pattern=r"(?<=\[)\[\d{4}\] (SGCA|SGHC|SGDC) \d+(?=\]\()")
extract_linked_reported_citations = partial(extract_citations,
                                            pattern=r"(?<=\[)\[\d{4}\] \d+ (SLR|SLR\(R\)) \d+(?=\]\()")

# Citations without restrictions on what preceeds it
extract_all_neutral_citations = partial(extract_citations, pattern=r"\[\d{4}\] (SGCA|SGHC|SGDC) \d+")
extract_all_reported_citations = partial(extract_citations, pattern=r"\[\d{4}\] \d+ (SLR|SLR\(R\)) \d+")


def linkify_legal_doc(file_path, overwrite=False, debug=False):
    """Add hyperlink to each legal citation found in legal documents.
    Set overwrite to True to overwrite document in file.
    Set debug mode to True to print legal citations found in each document.
    """
    with open(file_path, 'r+') as f:
        # 1. Read file
        report = f.read()

        # 2. Identify citations
        neutral_citations_indexes = extract_neutral_citations(document=report)
        reported_citations_indexes = extract_reported_citations(document=report)

        # Remove citations that are part of a file name
        filename_neutral_citations_indexes = extract_filename_neutral_citations(document=report)
        filename_reported_citations_indexes = extract_filename_reported_citations(document=report)

        # Remove citations that are already linked
        linked_neutral_citations_indexes = extract_linked_neutral_citations(document=report)
        linked_reported_citations_indexes = extract_linked_reported_citations(document=report)

        citations_indexes = (neutral_citations_indexes
                             .union(reported_citations_indexes)
                             .difference(filename_neutral_citations_indexes)
                             .difference(filename_reported_citations_indexes)
                             .difference(linked_neutral_citations_indexes)
                             .difference(linked_reported_citations_indexes))
        citations_indexes = sorted(citations_indexes, key=lambda _id: _id[1])

        # Perform a check: Check that all possible citations less citations that are part of a filename returns the same results as above
        all_neutral_citations_indexes = extract_all_neutral_citations(document=report)
        all_reported_citations_indexes = extract_all_reported_citations(document=report)
        check_citations_indexes = (all_neutral_citations_indexes
                                   .union(all_reported_citations_indexes)
                                   .difference(filename_neutral_citations_indexes)
                                   .difference(filename_reported_citations_indexes)
                                   .difference(linked_neutral_citations_indexes)
                                   .difference(linked_reported_citations_indexes))
        check_citations_indexes = sorted(check_citations_indexes, key=lambda _id: _id[1])
        if (check_citations_indexes != citations_indexes): print('WARNING: Citation discrepancy in', file_path)

        if debug:
            for i in set(check_citations_indexes).difference(set(citations_indexes)): print(report[i[0]:i[1]])

        # 3. Convert citations to hyperlinks
        current_index = 0
        report_with_hyperlinks = ''
        for index in citations_indexes:
            report_with_hyperlinks += (report[current_index:index[0]]
                                       + '<span style=\"background-color: #FAC0C0\">['
                                       + report[index[0]: index[1]]
                                       + ']' + '("https://www.open.gov.sg")</span>')
            current_index = index[1]
        report_with_hyperlinks += report[current_index:]

        # 4. Replace files
        if overwrite:
            f.seek(0)
            f.truncate()
            f.write(report_with_hyperlinks)

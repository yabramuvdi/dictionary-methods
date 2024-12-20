import pandas as pd
import re

class Dictionary:
    """
    Handles a dictionary search of terms in strings with flexibility using regular expressions.

    Attributes:
        terms (list of str): Terms from the dictionary.
        part_of_word (list of bool): Whether each term is searched as part of a longer word.
        ignore_case (bool): Whether to ignore case in searches.
        flexible_multi_word (bool): Whether to allow flexible separators in multi-word terms.
        search_type (str): Search behavior ('all' for all matches, 'first' for the first match).
        return_matches (bool): Whether to return the matched terms.
    """

    def __init__(self, 
                 terms, 
                 part_of_word=None,
                 ignore_case=True, 
                 flexible_multi_word=True, 
                 search_type="all", 
                 return_matches=True):
        """
        Initialize the Dictionary object.

        Args:
            terms (list of str): List of terms to include in the dictionary.
            part_of_word (list of bool, optional): Whether each term is a part of a word.
                Defaults to all False if not provided.
            ignore_case (bool, optional): Whether to ignore case in searches. Defaults to True.
            flexible_multi_word (bool, optional): Allow flexible separators in multi-word terms.
                Defaults to True.
            search_type (str, optional): Type of search ('all' or 'first'). Defaults to "all".
            return_matches (bool, optional): Whether to return matches. Defaults to True.
        """
        if not terms or not isinstance(terms, list):
            raise ValueError("Terms must be a non-empty list of strings.")

        self.terms = terms
        self.part_of_word = part_of_word or [False] * len(terms)
        self.ignore_case = ignore_case
        self.flexible_multi_word = flexible_multi_word
        self.search_type = search_type
        self.return_matches = return_matches
        self.dictionary_info = self.build_dictionary_info()
        self.dict_regex = self.gen_dict_regex()

    def build_dictionary_info(self):
        """
        Builds a DataFrame with term metadata for regex generation.

        Returns:
            pd.DataFrame: DataFrame with term details.
        """
        df = pd.DataFrame({
            'terms': self.terms,
            'part_of_word': self.part_of_word
        })
        df['is_single_word'] = df['terms'].apply(lambda x: len(x.split()) == 1)
        df['length_order'] = df['terms'].apply(len)
        return df.sort_values(by='length_order', ascending=False).reset_index(drop=True)

    def gen_multiple_word_regex(self, term):
        """
        Generates a regex for multi-word terms allowing flexible separators.

        Args:
            term (str): The term to create the regex for.

        Returns:
            str: Regex for the multi-word term.
        """
        components = term.split(" ")
        term_regex = r"\b" if not self.part_of_word else ""
        for i, comp in enumerate(components):
            separator = r"[-\s]+" if self.flexible_multi_word else " "
            term_regex += comp + (separator if i < len(components) - 1 else r"\b")
        return term_regex

    def gen_dict_regex(self):
        """
        Generates a single regex for all terms based on settings.

        Returns:
            re.Pattern: Compiled regex pattern for dictionary terms.
        """
        regex_parts = []
        for _, row in self.dictionary_info.iterrows():
            if row['is_single_word']:
                term = r"\b" + row['terms'] + (r"\b" if not row['part_of_word'] else "")
            else:
                term = self.gen_multiple_word_regex(row['terms'])
            regex_parts.append(term)

        regex = "|".join(regex_parts)
        return re.compile(regex, re.IGNORECASE if self.ignore_case else 0)

    def tag_text(self, text):
        """
        Searches for dictionary terms within a string.

        Args:
            text (str): Input text to search.

        Returns:
            tuple: (found_match, term_matches)
                found_match (bool): Whether any terms were found.
                term_matches (list of tuples): Matches with their positions (if return_matches=True).
        """
        if self.search_type not in {"all", "first"}:
            raise ValueError("Invalid search_type. Must be 'all' or 'first'.")

        matches = list(self.dict_regex.finditer(text))
        if not matches:
            return False, []

        if self.search_type == "first":
            match = matches[0]
            result = [(match.group(0), (match.start(), match.end()))] if self.return_matches else []
            return True, result

        result = [
            (match.group(0), (match.start(), match.end())) for match in matches
        ] if self.return_matches else []
        return True, result

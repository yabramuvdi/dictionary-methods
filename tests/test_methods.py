# from ..src.dictionary_methods.methods import Dictionary

# def run_tests():
#     print("Running tests for Dictionary class...\n")

#     # Test Case 1: Single-word terms, case-insensitive search
#     terms = ["remote", "work", "AI"]
#     part_of_word = [False, False, True]
#     dictionary = Dictionary(
#         terms=terms,
#         part_of_word=part_of_word,
#         ignore_case=True,
#         flexible_multi_word=False,
#         search_type="all",
#         return_matches=True
#     )

#     text = "Remote work and AI are shaping the future."
#     found, matches = dictionary.tag_text(text)
#     print("Test Case 1")
#     print(f"Found: {found}")
#     print(f"Matches: {matches}\n")
#     assert found is True
#     assert len(matches) == 3

#     # Test Case 2: Multi-word terms with flexible separators
#     terms = ["remote work", "machine learning"]
#     part_of_word = [False, False]
#     dictionary = Dictionary(
#         terms=terms,
#         part_of_word=part_of_word,
#         ignore_case=True,
#         flexible_multi_word=True,
#         search_type="all",
#         return_matches=True
#     )

#     text = "Remote-work and machine   learning are essential."
#     found, matches = dictionary.tag_text(text)
#     print("Test Case 2")
#     print(f"Found: {found}")
#     print(f"Matches: {matches}\n")
#     assert found is True
#     assert len(matches) == 2

#     # Test Case 3: First match search type
#     dictionary.search_type = "first"
#     found, matches = dictionary.tag_text(text)
#     print("Test Case 3")
#     print(f"Found: {found}")
#     print(f"Matches: {matches}\n")
#     assert found is True
#     assert len(matches) == 1

#     # Test Case 4: No matches
#     text = "This text contains none of the dictionary terms."
#     found, matches = dictionary.tag_text(text)
#     print("Test Case 4")
#     print(f"Found: {found}")
#     print(f"Matches: {matches}\n")
#     assert found is False
#     assert len(matches) == 0

#     # Test Case 5: Case-sensitive search
#     dictionary.ignore_case = False
#     dictionary.search_type = "all"
#     found, matches = dictionary.tag_text("remote work and ai are important.")
#     print("Test Case 5")
#     print(f"Found: {found}")
#     print(f"Matches: {matches}\n")
#     assert found is False

#     print("All tests passed!")

# if __name__ == "__main__":
#     run_tests()

import unittest
from src.dictionary_methods.methods import Dictionary

class TestDictionaryMethods(unittest.TestCase):

    def test_case_1(self):
        terms = ["remote", "work", "AI"]
        part_of_word = [False, False, True]
        dictionary = Dictionary(
            terms=terms,
            part_of_word=part_of_word,
            ignore_case=True,
            flexible_multi_word=False,
            search_type="all",
            return_matches=True
        )

        text = "Remote work and AI are shaping the future."
        found, matches = dictionary.tag_text(text)
        print("Test Case 1")
        print(f"Found: {found}")
        print(f"Matches: {matches}\n")
        self.assertTrue(found)

    # Add other test cases here
    # def test_case_2(self):
    #     ...

if __name__ == '__main__':
    unittest.main()
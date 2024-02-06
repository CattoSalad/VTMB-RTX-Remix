import unittest
from unittest.mock import patch
from sort_rtx_conf import sort_file, sort_lines, sort_texture_hashes, validate_duplicated_keys, validate_unique_hashes

class TestSortFileMethods(unittest.TestCase):
    def test_sort_lines(self):
        unsortedLines = [
            "a\n",
            "rtx.uiTextures = 0x8879E5EC1AE4587B\n",
            "b\n",
            "rtx.lightConverter = 0x5B14D81FE1EC269F\n",
            "rtx.ignoreTextures = 0x2ECB703D88A51043\n",
            "c\n",
            "rtx.hideInstanceTextures = 0x9B9688DF09FA1625\n"
        ]
        expected = [
            "a\n", "b\n", "c\n",
            "rtx.hideInstanceTextures = 0x9B9688DF09FA1625\n",
            "rtx.ignoreTextures = 0x2ECB703D88A51043\n",
            "rtx.lightConverter = 0x5B14D81FE1EC269F\n",
            "rtx.uiTextures = 0x8879E5EC1AE4587B\n"
        ]
        
        self.assertEqual(sort_lines(unsortedLines), expected)

    def test_sort_texture_hashes(self):
        unsortedLines = [
            "rtx.uiTextures = 0x8879E5EC1AE4587B, 0x5B14D81FE1EC269F, 0x2ECB703D88A51043, 0x9B9688DF09FA1625\n"
        ]
        expected = [
            "rtx.uiTextures = 0x2ECB703D88A51043, 0x5B14D81FE1EC269F, 0x8879E5EC1AE4587B, 0x9B9688DF09FA1625\n"
        ]
        
        self.assertEqual(sort_texture_hashes(unsortedLines), expected)

    def test_validate_unique_hashes_when_valid(self):
        lines = ["rtx.lightConverter = 0x5B14D81FE1EC269F\n", "rtx.uiTextures = 0x8879E5EC1AE4587B\n"]
        result = validate_unique_hashes(lines)

        self.assertTrue(result[0])
        self.assertEqual(result[1], "All texture hashes are unique")

    def test_validate_unique_hashes_valid_on_different_lines(self):
        lines = ["rtx.lightConverter = 0x5B14D81FE1EC269F\n", "rtx.uiTextures = 0x5B14D81FE1EC269F\n"]
        result = validate_unique_hashes(lines)

        self.assertTrue(result[0])
        self.assertEqual(result[1], "All texture hashes are unique")

    def test_validate_unique_hashes_when_invalid(self):
        lines = ["rtx.lightConverter = 0x8879E5EC1AE4587B, 0x8879E5EC1AE4587B\n", "rtx.uiTextures = 0x8879E5EC1AE4587B\n"]
        result = validate_unique_hashes(lines)

        self.assertFalse(result[0])
        self.assertEqual(result[1], "Duplicate texture hashes found in: rtx.lightConverter = 0x8879E5EC1AE4587B")

    def test_validate_duplicated_keys_when_valid(self):
        lines = ["rtx.lightConverter = 0x5B14D81FE1EC269F\n", "rtx.uiTextures = 0x8879E5EC1AE4587B\n"]
        result = validate_duplicated_keys(lines)

        self.assertTrue(result[0])
        self.assertEqual(result[1], "All keys are unique")

    def test_validate_duplicated_keys_when_invalid(self):
        lines = ["rtx.lightConverter = 0x5B14D81FE1EC269F\n", "rtx.lightConverter = 0x8879E5EC1AE4587B\n"]
        result = validate_duplicated_keys(lines)

        self.assertFalse(result[0])
        self.assertEqual(result[1], "Duplicate key found: rtx.lightConverter")

    def test_validate_unique_hashes(self):
        lines_to_write = [
            "rtx.lightConverter = 0x3F1B8E8E71AE6D50, 0x3F1B8E8E71AE6D50, 0x5B14D81FE1EC269F\n",
            "rtx.uiTextures = 0x3F1B8E8E71AE6D50\n"
        ]

        with open('test_rtx_with_duplicate_hashes.conf', 'w') as file:
            file.writelines(lines_to_write)

        expected_lines = [
            "rtx.lightConverter = 0x3F1B8E8E71AE6D50, 0x5B14D81FE1EC269F\n",
            "rtx.uiTextures = 0x3F1B8E8E71AE6D50\n"
        ]

        sort_file('test_rtx_with_duplicate_hashes.conf')

        with open('test_rtx_with_duplicate_hashes.conf', 'r') as file:
            actual_lines = file.readlines()
        self.assertEqual(actual_lines, expected_lines)

    def test_validate_duplicated_keys_and_merge_duplicates(self):
        lines_to_write = [
            "rtx.lightConverter = 0x3F1B8E8E71AE6D50\n",
            "rtx.lightConverter = 0x3F1B8E8E71AE6D50, 0x5B14D81FE1EC269F\n"
        ]

        with open('test_rtx_with_duplicate_keys.conf', 'w') as file:
            file.writelines(lines_to_write)

        expected_lines = [
            "rtx.lightConverter = 0x3F1B8E8E71AE6D50, 0x5B14D81FE1EC269F\n"
        ]

        sort_file('test_rtx_with_duplicate_keys.conf')

        with open('test_rtx_with_duplicate_keys.conf', 'r') as file:
            actual_lines = file.readlines()
        self.assertEqual(actual_lines, expected_lines)


if __name__ == '__main__':
    unittest.main()
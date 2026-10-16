
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class LearningTrackerTests(unittest.TestCase):

    def test_load_topics_when_file_missing(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(main, "DATA_FILE", Path(folder) / "missing.json"):
                self.assertEqual(main.load_topics(), [])

    def test_save_and_load_topics(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "topics.json"

            with patch.object(main, "DATA_FILE", file_path):
                topics = ["Variables", "Loops"]
                main.save_topics(topics)

                self.assertEqual(main.load_topics(), topics)

    def test_saved_file_contains_valid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "topics.json"

            with patch.object(main, "DATA_FILE", file_path):
                main.save_topics(["Functions"])

                saved_data = json.loads(file_path.read_text(encoding="utf-8"))
                self.assertEqual(saved_data, ["Functions"])


if __name__ == "__main__":
    unittest.main()

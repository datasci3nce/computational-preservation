import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_repo import check_all
from normal_form import passage_approx, LAMBDA_STAR


class EditorialRepoTests(unittest.TestCase):
    def test_integrity_and_links(self):
        check_all()

    def test_local_passage_is_finite(self):
        self.assertGreater(passage_approx(0.18), 0)

    def test_slows_near_fold(self):
        self.assertGreater(passage_approx(0.20), passage_approx(0.18))

    def test_invalid_regime(self):
        with self.assertRaises(ValueError):
            passage_approx(LAMBDA_STAR)
        with self.assertRaises(ValueError):
            passage_approx(0.18, width=0)


if __name__ == '__main__':
    unittest.main()

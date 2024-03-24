import unittest
from ai_feature_engineering import AI_Feature_Engineering
import os
import numpy as np


class TestAIFeatureEngineering(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure the test directory and file exist
        cls.test_dir = 'test_wiki'
        cls.test_file_name = 'test_issue.html'
        cls.test_file_path = os.path.join(cls.test_dir, cls.test_file_name)
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)
        if not os.path.isfile(cls.test_file_path):
            with open(cls.test_file_path, 'w') as f:
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Issue</title>
</head>
<body>
    <article>
        <section class="issue-summary">
            <h2>Issue Summary</h2>
            <p><strong>Issue ID:</strong> <span id="issue-id">TEST001</span></p>
            <p><strong>Component:</strong> <span id="component">Test Component</span></p>
            <p><strong>Issue Type:</strong> <span id="issue-type">Test Type</span></p>
            <p><strong>Date Reported:</strong> <span id="date-reported">2024-03-24</span></p>
            <p><strong>Affected Systems:</strong> <span id="affected-systems">Test System</span></p>
        </section>
        <section class="issue-description">
            <h2>Issue Description</h2>
            <p>This is a test description.</p>
        </section>
        <section class="possible-causes">
            <h2>Possible Causes</h2>
            <ul>
                <li>Test Cause 1</li>
                <li>Test Cause 2</li>
            </ul>
        </section>
        <section class="resolution-steps">
            <h2>Resolution Steps</h2>
            <ol>
                <li>Test Step 1</li>
                <li>Test Step 2</li>
            </ol>
        </section>
        <section class="resolution-outcome">
            <h2>Resolution Outcome</h2>
            <p>This is a test outcome.</p>
        </section>
    </article>
</body>
</html>""")

    @classmethod
    def tearDownClass(cls):
        # Clean up: Remove the test directory and its contents
        if os.path.exists(cls.test_file_path):
            os.remove(cls.test_file_path)
        if os.path.exists(cls.test_dir):
            os.rmdir(cls.test_dir)

    def test_process_files(self):
        ai_fe = AI_Feature_Engineering(self.test_dir)
        issues_info = ai_fe.process_files()
        self.assertEqual(len(issues_info), 1)
        self.assertEqual(issues_info[0]['issue_id'], 'TEST001')
        print("------------------")
        print(f"Total issues parsed: {len(issues_info)}")
        print()
        for issue_info in issues_info:
            print(f"{issue_info}")
            print()
        print("------------------")


    def test_feature_engineering(self):
        ai_fe = AI_Feature_Engineering(self.test_dir)
        issues_info = ai_fe.process_files()
        _, matrix = ai_fe.feature_engineering(issues_info)
        self.assertTrue(isinstance(matrix, np.ndarray))
        self.assertEqual(matrix.shape[0], 1)  # Expecting one sample


if __name__ == '__main__':
    unittest.main()

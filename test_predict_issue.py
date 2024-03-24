import unittest
import os
from ai_feature_engineering import AI_Feature_Engineering
from ai_model import AI_Model


class TestIssuePrediction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wiki_dir = 'wiki'
        cls.ai_fe = AI_Feature_Engineering(cls.wiki_dir)
        cls.ai_fe.train_and_evaluate_model()

        # Setup directory for test data
        cls.wiki_dir = 'wiki'
        cls.test_dir = 'test-wiki'
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)

        # Create a sample HTML file
        cls.sample_file_path = os.path.join(cls.test_dir, 'test_issue.html')
        with open(cls.sample_file_path, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Wiki Page Test: Application Unavailability</title>
</head>
<body>
    <article>
        <section class="issue-summary">
            <h2>Issue Summary</h2>
            <p><strong>Issue ID:</strong> <span id="issue-id">TEST001</span></p>
            <p><strong>Component:</strong> <span id="component">Application (Java)</span></p>
            <p><strong>Issue Type:</strong> <span id="issue-type">Unavailability</span></p>
            <p><strong>Date Reported:</strong> <span id="date-reported">2024-03-24</span></p>
            <p><strong>Affected Systems:</strong> <span id="affected-systems">App</span></p>
        </section>
        <section class="issue-description">
            <h2>Issue Description</h2>
            <p>The Java Application becomes unresponsive intermittently, leading to significant downtime and affecting end-user experience.</p>
        </section>
        <!-- Additional sections omitted for brevity -->
    </article>
</body>
</html>""")

    @classmethod
    def tearDownClass(cls):
        # Clean up: Remove the test file and directory
        os.remove(cls.sample_file_path)
        os.rmdir(cls.test_dir)

    def test_predict_future_issue(self):
        # Assuming AI_Feature_Engineering and AI_Model are properly set up to handle a single file prediction

        # Process the test file and predict
        issue_description = self.ai_fe.process_single_file(self.sample_file_path)  # Implement this method
        # Predict the issue type
        prediction = self.ai_fe.predict_issue_type(issue_description)

        # Assuming you have a way to interpret the prediction
        print(f"Predicted issue type: {prediction}")
        self.assertIsNotNone(prediction, "Prediction should not be None")

    def test_predict_impact_of_service_c_change(self):
        # Description of the change in Service C
        change_description = "Service C"

        # Prepare the change description for prediction
        X = self.ai_fe.prepare_change_description(change_description)

        # Predict the impact of the change
        prediction = self.ai_fe.predict_service_impact(X)

        # Print or assert the prediction
        print(f"Predicted impact: {prediction}")
        # Here, you can add assertions based on your expectations

    def test_predict_impact_of_service_c_availability(self):
        # Description of the change in Service C
        change_description = "Service A latency"

        # Prepare the change description for prediction
        X = self.ai_fe.prepare_change_description(change_description)

        # Predict the impact of the change
        prediction = self.ai_fe.predict_service_impact(X)

        # Print or assert the prediction
        print(f"Predicted impact: {prediction}")
        # Here, you can add assertions based on your expectations


if __name__ == '__main__':
    unittest.main()

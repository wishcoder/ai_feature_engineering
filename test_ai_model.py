import unittest
from ai_model import AI_Model
import numpy as np
from ai_feature_engineering import AI_Feature_Engineering


class TestAIModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the AI_Model instance
        cls.model = AI_Model()
        ai_fe = AI_Feature_Engineering('wiki')
        issues_info = ai_fe.process_files()
        feature_names, transformed_matrix = ai_fe.feature_engineering(issues_info)
        cls.X = transformed_matrix
        cls.y = ai_fe.generate_labels()

    def test_train(self):
        # Test that the model can be trained without throwing an error
        try:
            self.model.train(self.X, self.y)
            trained = True
        except Exception as e:
            trained = False
        self.assertTrue(trained, "The model should be trained successfully.")

    def test_predict(self):
        # Ensure predict method works after training
        self.model.train(self.X, self.y)
        predictions = self.model.predict(self.X)
        self.assertEqual(len(predictions), len(self.y), "The model should make one prediction per sample.")

    def test_evaluate(self):
        # Test that evaluate method works and prints the classification report
        self.model.train(self.X, self.y)
        try:
            self.model.evaluate()  # This prints the classification report to stdout
            evaluated = True
        except Exception as e:
            evaluated = False
        self.assertTrue(evaluated, "The model should be evaluated successfully.")


if __name__ == '__main__':
    unittest.main()

import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from ai_feature_engineering import AI_Feature_Engineering  # Your existing feature engineering class


class ModelEvaluator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.feature_engineer = AI_Feature_Engineering(data_path)
        self.models = {
            'LogisticRegression': LogisticRegression(max_iter=1000),
            'RandomForest': RandomForestClassifier(),
            'SVC': SVC()
        }
        self.results = []

    def evaluate_models(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        for name, model in self.models.items():
            print(f"Evaluating model: {name}")
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
            self.results.append((name, report['accuracy']))  # Store model name and accuracy

    def run(self):
        # Process files and generate features
        issues_info = self.feature_engineer.process_files()
        _, X = self.feature_engineer.feature_engineering(issues_info)
        y = self.feature_engineer.generate_labels()

        # Evaluate all models
        self.evaluate_models(X, y)

        # Print results
        for name, accuracy in self.results:
            print(f"Model: {name}, Accuracy: {accuracy}")


if __name__ == "__main__":
    evaluator = ModelEvaluator('wiki')
    evaluator.run()

# AI_Model.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


class AI_Model:
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)

    def train(self, X, y):
        """
        Train the model using the provided features and target labels.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X=None):
        """
        Make predictions using the trained model. If X is not provided, predict on the test set.
        """
        if X is None:
            X = self.X_test
        return self.model.predict(X)

    def evaluate(self):
        """
        Evaluate the model's performance on the test set.
        """
        y_pred = self.predict()
        print(classification_report(self.y_test, y_pred, zero_division=0))

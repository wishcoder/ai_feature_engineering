import re

import nltk
from bs4 import BeautifulSoup
from nltk import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os
from ai_model import AI_Model

# Assuming 'nltk_data' is in the same directory as your Python script
current_directory = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(current_directory, 'nltk_data')

# Add this path to the nltk data path
nltk.data.path.append(nltk_data_path)

# Now you can load NLTK resources as usual, and it will also look in your specified directory
from nltk.corpus import stopwords

nltk.download('stopwords', download_dir=nltk_data_path, quiet=True)


class AI_Feature_Engineering:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.vectorizer = TfidfVectorizer(preprocessor=self.preprocess_text)
        self.model = AI_Model()  # Initialize the AI_Model object

    def parse_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return BeautifulSoup(content, 'html.parser')

    def generate_labels(self):
        issues_info = self.process_files()
        y = [issue['label'] for issue in issues_info]
        return y

    def extract_issue_data(self, soup):
        # Initialize a dictionary to hold the issue data
        issue_data = {
            'issue_id': soup.find(id='issue-id').text if soup.find(id='issue-id') else 'N/A',
            'component': soup.find(id='component').text if soup.find(id='component') else 'N/A',
            'issue_type': soup.find(id='issue-type').text if soup.find(id='issue-type') else 'N/A',
            'date_reported': soup.find(id='date-reported').text if soup.find(id='date-reported') else 'N/A',
            'affected_systems': soup.find(id='affected-systems').text if soup.find(id='affected-systems') else 'N/A',
            'issue_description': soup.find(class_='issue-description').text.strip() if soup.find(
                class_='issue-description') else 'N/A',
        }

        # Handling lists for possible causes and resolution steps
        possible_causes_section = soup.find(class_='possible-causes')
        issue_data['possible_causes'] = [li.text for li in
                                         possible_causes_section.find_all('li')] if possible_causes_section else []

        resolution_steps_section = soup.find(class_='resolution-steps')
        issue_data['resolution_steps'] = [li.text for li in
                                          resolution_steps_section.find_all('li')] if resolution_steps_section else []

        resolution_outcome_section = soup.find(class_='resolution-outcome')
        issue_data[
            'resolution_outcome'] = resolution_outcome_section.text.strip() if resolution_outcome_section else 'N/A'

        # Extract the issue label for 'y'
        issue_label = soup.find(id='issue-type').text if soup.find(id='issue-type') else 'N/A'
        issue_data['label'] = issue_label

        return issue_data

    def process_files(self):
        issues_info = []
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.html'):
                soup = self.parse_html_file(os.path.join(self.dir_path, filename))
                issue_data = self.extract_issue_data(soup)
                issues_info.append(issue_data)
        return issues_info

    def extract_issue_data_with_causes(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        # Initialize a dictionary to hold the issue data
        issue_data = {
            'issue_id': soup.find(id='issue-id').text if soup.find(id='issue-id') else 'N/A',
            'component': soup.find(id='component').text if soup.find(id='component') else 'N/A',
            'issue_type': soup.find(id='issue-type').text if soup.find(id='issue-type') else 'N/A',
            'date_reported': soup.find(id='date-reported').text if soup.find(id='date-reported') else 'N/A',
            'affected_systems': soup.find(id='affected-systems').text if soup.find(id='affected-systems') else 'N/A',
            'issue_description': soup.find(class_='issue-description').text.strip() if soup.find(
                class_='issue-description') else 'N/A',
            # Extracting possible causes as labels
            'labels': []
        }

        # Handling lists for possible causes
        possible_causes_section = soup.find(class_='possible-causes')
        if possible_causes_section:
            issue_data['labels'] = [li.text.strip() for li in possible_causes_section.find_all('li')]

        return issue_data

    def process_files_with_causes(self):
        issues_info = []
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.html'):
                soup = self.parse_html_file(os.path.join(self.dir_path, filename))
                issue_data = self.extract_issue_data_with_causes(soup)
                issues_info.append(issue_data)
        return issues_info

    def process_single_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        # Extract the issue description or any other relevant sections
        issue_description = soup.find(class_='issue-description').text.strip() if soup.find(
            class_='issue-description') else ''

        # Here you can add more processing, e.g., extracting other sections or additional preprocessing of the text
        return issue_description

    def preprocess_text(self, text):
        #     text preprocessing function
        # Lowercasing
        text = text.lower()
        # Remove non-alphanumeric characters
        text = re.sub(r'\W+', ' ', text)
        # Tokenization and stopwords removal could be done here as well
        words = text.split()
        words = [word for word in words if word not in stopwords.words('english')]
        # Stemming
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]
        return ' '.join(words)

    def feature_engineering(self, issues_info):
        all_possible_causes = [" ".join(issue['possible_causes']) for issue in issues_info]
        X = self.vectorizer.fit_transform(all_possible_causes)
        return self.vectorizer.get_feature_names_out(), X.toarray()

    def train_and_evaluate_model(self):
        """
        Train and evaluate the model using the extracted features and provided labels.
        """
        # Assuming feature_engineering method has been called and we have the feature matrix X
        feature_names, X = self.feature_engineering(self.process_files())
        y = self.generate_labels()
        self.model.train(X, y)
        self.model.evaluate()

    def predict_issue_type(self, text):
        # Transform the text into a feature vector
        # Assuming `vectorizer` is your TF-IDF or CountVectorizer instance used during training
        # You might need to load or initialize this vectorizer here if it's not already available
        X = self.vectorizer.transform([text])

        # Use the trained model to predict
        # Assuming `ai_model` is an instance of your AI_Model class with a trained model
        prediction = self.model.predict(X)

        # If your model's prediction is numerical or encoded, map it back to the issue type here
        # For simplicity, this example assumes the prediction can be directly interpreted
        return prediction

    def prepare_change_description(self, description):
        # Directly use the vectorizer to transform the description into a feature vector
        # No need for BeautifulSoup since we're working with plain text
        return self.vectorizer.transform([description])

    def predict_service_impact(self, X):
        # Use the trained model to predict the impact
        prediction = self.model.predict(X)
        # Assuming direct interpretation for simplicity
        return prediction


if __name__ == "__main__":
    dir_path = 'wiki'
    ai_fe = AI_Feature_Engineering(dir_path)
    issues_info = ai_fe.process_files()
    print("------------------")
    print(f"Total issues parsed: {len(issues_info)}")
    print()
    for issue_info in issues_info:
        print(f"{issue_info}")
        print()
    print("------------------")
    print()
    feature_names, transformed_matrix = ai_fe.feature_engineering(issues_info)
    print("Feature Names:", feature_names)
    print("Transformed Feature Matrix:\n", transformed_matrix)

    ai_fe.train_and_evaluate_model()

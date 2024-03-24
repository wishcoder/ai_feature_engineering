from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import os

class AI_Feature_Engineering:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def parse_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return BeautifulSoup(content, 'html.parser')

    def extract_issue_data(self, soup):
        return {
            'issue_id': soup.find(class_='issue-id').text,
            'component': soup.find(class_='component').text,
            'issue_type': soup.find(class_='issue-type').text,
            'date_reported': soup.find(class_='date-reported').text,
            'affected_systems': soup.find(class_='affected-systems').text,
            'issue_description': soup.find(class_='issue-description').text.strip(),
            'possible_causes': [li.text for li in soup.find(class_='possible-causes').find_all('li')],
            'resolution_steps': [li.text for li in soup.find(class_='resolution-steps').find_all('li')],
            'resolution_outcome': soup.find(class_='resolution-outcome').text.strip(),
        }

    def process_files(self):
        issues_info = []
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.html'):
                soup = self.parse_html_file(os.path.join(self.dir_path, filename))
                issue_data = self.extract_issue_data(soup)
                issues_info.append(issue_data)
        return issues_info

    def feature_engineering(self, issues_info):
        vectorizer = CountVectorizer()
        all_possible_causes = [" ".join(issue['possible_causes']) for issue in issues_info]
        X = vectorizer.fit_transform(all_possible_causes)
        return vectorizer.get_feature_names_out(), X.toarray()

if __name__ == "__main__":
    dir_path = 'wiki'
    ai_fe = AI_Feature_Engineering(dir_path)
    issues_info = ai_fe.process_files()
    print(f"Total issues parsed: {len(issues_info)}")

    feature_names, transformed_matrix = ai_fe.feature_engineering(issues_info)
    print("Feature Names:", feature_names)
    print("Transformed Feature Matrix:\n", transformed_matrix)

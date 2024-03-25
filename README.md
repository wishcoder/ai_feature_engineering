# AI Feature Engineering #

Transform your textual and categorical data into numerical formats that ML models can process. For instance, issue types, system components affected, and steps taken can be encoded using techniques like one-hot encoding, TF-IDF for text, or embedding layers for more complex representations.

# Run

> [!TIP]
> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wishcoder/ai_feature_engineering/HEAD)


## Prerequisite

* [Requirements](requirements.txt)


## System components and States

| Component   | Change | Unavailability |
|-------------|:------:|:--------------:|
| App         |   Yes  |       Yes      |
| Service A   |   Yes  |       Yes      |
| Service B   |   Yes  |       Yes      |
| Service C   |   Yes  |       Yes      |
| Firewall    |   Yes  |       Yes      |
| Router      |   Yes  |       Yes      |
| Server      |   Yes  |       Yes      |


## Architecture

```
   +----------------+       +--------+       +----------+       +-----+
   | Outside Network| ----> | Router | ----> | Firewall | ----> | App |
   +----------------+       +--------+       +----------+       +-----+
                                                                   |
                                                                   v
                                                            +-----------+
                                                            | Service A |
                                                            +-----------+
                                                                   |
                                                                   v
                                                            +-----------+
                                                            | Service B |
                                                            +-----------+
                                                                   |
                                                                   v
                                                            +-----------+
                                                            | Service C |
                                                            +-----------+
```

## Data Source

* Code Repositories
* Bug Tracking System
* Incident Management System
* System of Record Tool_
* Wiki Pages


## Application


### Incident Forecasting (For - Upper Management, Application Support, Developers)
* **AI Model:**  Time Series Forecasting and Anomaly Detection models are utilized to predict future incidents based on historical data. These models analyze patterns and trends over time to forecast potential system issues before they occur.
* **Data Used:** The models leverage a combination of historical incident data (including severity, duration, affected components, and resolution details), system metrics (is available), and change logs from Code Repositories detailing system modifications. This data is interconnected through **common labels** to provide a comprehensive view of the factors leading to incidents.
* **Benefit:** Predict the likelihood of future incidents based on patterns, such as number of application dependencies, or specific component vulnerabilities. This can help in proactive resource allocation and incident prevention.

### Root Cause Analysis For - Application Support, Developers)
* **AI Model:** Machine Learning models, particularly Natural Language Processing (NLP) for analyzing incident reports and logs, and Graph Neural Networks (GNNs) for understanding the relationships and dependencies between different system components. These models work together to identify patterns and anomalies that could indicate the root cause of incidents.  
* **Data Used:** This approach utilizes detailed incident reports, system logs, and operational data from Incident Management System, Repositories commit logs, and Bug Tracking System tickets. The data includes timestamps, error messages, system metrics, changes made (linked through common **labels**), and user-reported issues. By correlating this information, the AI models can trace back through the data to pinpoint the origin of a problem.
* **Benefit:** Analyze past incidents and identify common factors or sequences of events that often lead to issues. This can improve the speed and accuracy of root cause identification for new incidents.

### Predictive Incident Management in Incident Management System (For - Upper Management, Application Support, Developers)
* **AI Model:** Time series forecasting and anomaly detection models.
* **Data Used:** Incident reports, resolution times, and incident characteristics from Incident Management System.
* **Benefit:** Predict and identify potential future incidents before they occur, allowing preemptive action. This can help in resource allocation and minimizing downtime.

### Automated Ticket Triaging in Bug Tracking System (For - Management, Developers)
* **AI Model:** Natural Language Processing (NLP) and classification models trained using data from Bug Tracking System.
* **Data Used:** Historical Bug Tracking System tickets (description, priority, resolution time, etc.).
* **Benefit:** Automatically categorize and prioritize incoming tickets based on their content, historical data, and urgency. This reduces manual triaging workload and speeds up response times.

### Code Quality and Bug Prediction in Code Repositories (For - Developers)
* **AI Model:** Machine learning models trained on code metrics, commit logs, and bug history.
* **Data Used:** Commit history, code changes, and linked Bug Tracking System bug tickets.
* **Benefit:** Predict potential bugs in code commits or pull requests before they are merged, based on historical bug data and code changes. This can significantly reduce the bug rate and improve code quality.

### Automated Resolution Suggestions for Incidents (For - Application Support, Developers)
* **AI Model:** NLP and recommendation systems.
* **Data Used:** Historical incident reports and their resolutions in Incident Management System, linked with Bug Tracking System tickets and Repositories commits.
* **Benefit:** Provide automated resolution suggestions for new incidents by learning from past incidents and their successful resolutions. This can speed up incident resolution times.

### Cross-Platform Analytics and Insights (For - Upper Management)
* **AI Model:** Data integration and analysis tools, possibly with some predictive modeling.
* **Data Used:** Data from Code Repositories, Bug Tracking System, and Incident Management System, focusing on common **labels** to connect data points.
* **Benefit:** Gain comprehensive insights into project health, developer productivity, incident trends, and more. This holistic view can help in strategic decision-making and identifying areas for improvement.
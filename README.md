# AI Feature Engineering #

Transform your textual and categorical data into numerical formats that ML models can process. For instance, issue types, system components affected, and steps taken can be encoded using techniques like one-hot encoding, TF-IDF for text, or embedding layers for more complex representations.

## Prerequisite

##### Python library for parsing HTML content.
> * pip install beautifulsoup4

##### Pandas is an open-source library providing high-performance, easy-to-use data structures, and data analysis tools for Python. The name "pandas" is derived from "panel data," an econometrics term for multidimensional structured data sets. It's particularly well-suited for handling and analyzing input data in various forms, such as CSV files, SQL databases, or Excel spreadsheets.
> * pip install pandas

##### Scikit-learn is an open-source machine learning library for Python. It is built on top of other popular libraries like NumPy, SciPy, and matplotlib. Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface.
> * pip install scikit-learn


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


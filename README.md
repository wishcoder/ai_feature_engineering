# AI Feature Engineering #

Transform your textual and categorical data into numerical formats that ML models can process. For instance, issue types, system components affected, and steps taken can be encoded using techniques like one-hot encoding, TF-IDF for text, or embedding layers for more complex representations.

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


# SecureLink: Machine Learning-Based Phishing URL Detection System

## Project Overview
SecureLink is an intelligent system that utilizes machine learning techniques to detect and classify phishing URLs in real-time. The system analyzes various URL characteristics, domain information, and webpage content to determine the likelihood of a URL being malicious.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

## Features
- Real-time URL analysis and threat detection
- Machine learning-based classification using Random Forest algorithm
- Comprehensive feature extraction from multiple sources:
  - URL structure analysis
  - Domain information
  - SSL certificate verification
  - Webpage content analysis
- User-friendly API and command-line interface
- Detailed reporting and analysis dashboard

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository
```bash
git clone https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System.git
cd securelink
```

2. Create and activate virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
```
Phishing-Detection-system/
├── app.py                 # Command-line interface
├── data/                  # Training dataset
├── requirement.txt        # Python dependencies
└── src/
  ├── features.py        # URL feature extraction
  ├── predict.py         # Model training and prediction
  └── utils.py           # Data loading and URL preprocessing
```

## Usage

### Basic Usage
```bash
python app.py
```

### Command Line Interface
The application trains the model from `data/data_bal - 20000.xlsx`, then accepts
URLs interactively. Enter `quit` to exit.
## Testing
Run the test suite:
```bash
pytest tests/
```

## Performance Metrics
- Accuracy: 92.5%
- Precision: 94.3%
- Recall: 91.8%
- F1 Score: 93.0%

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors
- Mahmoud Osama - *Initial work* - (https://github.com/Mahmoud-Ossama)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Dataset provided by PhishTank
- Inspired by research on ML-based phishing detection
- Thanks to Delta University/Faculty of AI - Cybersecurity Department for project support

## Contact
Mahmoud Osama - vip.m.osama@gmail.com
Project Link: https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System

## Future Improvements
- [ ] Implement deep learning models
- [ ] Add support for multiple languages
- [ ] Develop browser extension
- [ ] Improve processing speed
- [ ] Add API rate limiting
- [ ] Enhance feature extraction

## Citation
If you use this project in your research, please cite:
```
@misc{securelink2024,
  author = {Mahmoud Osama},
  title = {SecureLink: Machine Learning-Based Phishing URL Detection System},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/Mahmoud-Ossama/ML-Based-Phishing-URL-Detection-System}
}
```
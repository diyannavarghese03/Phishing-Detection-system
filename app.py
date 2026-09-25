import os
import shutil
import sys

if sys.version_info[:2] != (3, 12):
    py312 = shutil.which("python3.12")
    if py312:
        os.execv(py312, [py312, __file__, *sys.argv[1:]])
    print("This project requires Python 3.12. Please run: python3.12 app.py")
    raise SystemExit(1)

from src.predict import PhishingDetector
from src.utils import load_data


def main():
    # Load data
    urls, labels = load_data()

    # Initialize and train model
    detector = PhishingDetector()
    
    # Train model (store report but don't print)
    report = detector.train(urls, labels)
    
    # New interactive interface
    while True:
        url = input("\nEnter URL (or 'quit' to exit): ")
        if url.lower() == 'quit':
            break
            
        print("-------------------")
        result = detector.predict(url)
        print(f"Is it phishing: {result['is_phishing']}")
        print(f"Probability: {result['probability']:.2f}")

if __name__ == "__main__":
    main()    cd /workspaces/Phishing-Detection-system
    git add .
    git commit -m "Fix Python runtime compatibility and app launch"
    git push
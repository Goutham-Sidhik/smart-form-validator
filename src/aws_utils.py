
"""
aws_utils.py - Mocked wrapper for AWS Rekognition and Textract calls.
"""

def analyze_with_rekognition(image):
    # Dummy Rekognition analysis
    print("Analyzing image with AWS Rekognition...")
    return {"ModerationLabels": [], "Gender": "Male"}

def extract_with_textract(image):
    # Dummy Textract analysis
    print("Extracting text using AWS Textract...")
    return {"Name": "John Doe", "ApplicationID": "FORM123"}

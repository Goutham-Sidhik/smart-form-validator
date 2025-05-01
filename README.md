# 🧾 Smart Form Validator (Automated Backend)

An intelligent backend system that automatically validates scanned application forms stored in a secure database. The system detects inappropriate or spoofed images, validates gender identity, and extracts form fields using OCR.

---

## 📌 Overview

**Smart Form Validator** is a backend-only application that performs scheduled validation on encrypted image data stored in a database. The system automatically decrypts, processes, and validates each form image through a rule-based pipeline.

> ⚠️ This version excludes production datasets, models, and credentials due to company IP restrictions. Placeholder functions and examples are provided to demonstrate structure and flow.

---

## 🔁 Key Features

- 🗂️ **Automated DB Polling** – Regularly checks the database for new encrypted form images
- 🔐 **Decryption Layer** – Securely decrypts each image before processing
- 🧠 **Face ROI Detection** – Extracts the face region using OpenCV for downstream validation
- 🛡️ **Content Moderation** – Detects obscenities, nudity, celebrity spoofing, or masks using AWS Rekognition
- 🚻 **Gender Validation** – Predicts gender from image and compares with form entry
- 🧾 **Text Extraction** – Extracts handwritten/typed fields using AWS Textract and Pytesseract
- 🧪 **Validation Engine** – Flags mismatches or failed checks and logs structured results

---

## 🧠 Architecture

![Architecture Diagram](architecture.png)

---

## 🛠 Tech Stack

| Component          | Tool/Service                 |
|-------------------|------------------------------|
| Language           | Python                       |
| Image Processing   | OpenCV, Pillow               |
| OCR                | Pytesseract, AWS Textract    |
| Content Analysis   | AWS Rekognition              |
| API Framework      | Flask                        |
| Database           | MySQL                        |

---

## 📂 Project Structure

```
smart-form-validator/
│
├── README.md                 # Project overview and documentation
├── requirements.txt          # Required Python packages
│
├── src/                      # Source code
│   ├── main.py               # Entry point with scheduler loop
│   ├── db_reader.py          # Reads & decrypts image data from the DB
│   ├── validator.py          # Content moderation & gender validation logic
│   ├── extractor.py          # Text extraction and field validation
│   ├── aws_utils.py          # Rekognition and Textract integration
│   └── utils.py              # Logging, image helpers, etc.
│
├── docs/                     # Documentation assets
│   └── architecture.png      # Architecture flow diagram

```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-form-validator.git
cd smart-form-validator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory with your credentials:

```ini
AWS_ACCESS_KEY=your_key
AWS_SECRET_KEY=your_secret
DB_URI=mysql://user:password@host:port/dbname
```

### 4. Start the service

```bash
python src/main.py
```

* This will run the code that regularly checks the database for new encrypted form images and automatically processes them.
* The regular checking interval can also be changed to run just once, to process all images available up to the current time, based on the user's requirement.

---

## 📥 Example Output

```json
{
  "application_id": "FORM_20250401_0012",
  "status": "Alert",
  "face_clear": true,
  "gender_match": false,
  "moderation_passed": true,
  "extracted_fields": {
    "name": "Ravi Kumar",
    "dob": "1992-07-11",
    "gender": "Male"
  }
}
```

---

## 🔒 Disclaimer

This repository demonstrates a professional-grade application structure and processing pipeline.  
It **does not include** proprietary data, production-trained models, or confidential credentials.  
All functions are **dummy implementations** created solely to illustrate the flow and structure of the system.  
You are free to adapt the structure, pipeline logic, and modular components for educational, testing, or private deployments.


---

## 👨‍💻 Author

**Goutham Sidhik**  
AI/ML Engineer | Computer Vision & GenAI Developer  
[LinkedIn](https://www.linkedin.com/in/goutham-sidhik-amuluru-50231b163/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


# 📦 Component Logistics Extractor API

An AI-powered extraction API built to automate the processing of messy, unstructured supply chain and logistics text. Leveraging Large Language Models (like Google Gemini) and strict Pydantic schema validation, this service reliably converts shipping manifests, quality control reports, and vendor emails into structured, actionable JSON data.

## 📑 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Features
- **Smart Logistics Parsing:** Extracts tracking numbers, line-item components, and carrier details from raw shipping manifests.
- **QC Report Analysis:** Categorizes defects and scores severity from unstructured inspector notes.
- **Vendor Email Extraction:** Identifies backorders, expected delivery dates, and quantity adjustments from vendor communications.
- **Strict Data Validation:** Enforces LLM output conformity using Pydantic schemas, raising custom `LLMOutputParsingError` exceptions when models hallucinate or return invalid JSON.
- **Prompt Engineering Engine:** Utilizes YAML-based system instructions and JSON few-shot examples to maintain deterministic, factual extraction.

## 🛠️ Technologies Used
- **Framework:** FastAPI & Uvicorn
- **Validation:** Pydantic (v2) & Pydantic Settings
- **AI/LLM:** Google Generative AI (Gemini 1.5 Pro / Flash)
- **Utilities:** PyYAML for prompt templating
- **Testing:** Pytest & HTTPX

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mtepenner/component-logistics-extractor.git
   cd component-logistics-extractor
    ````

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Copy the example environment file and add your specific API keys.

    ```bash
    cp .env.example .env
    ```

    Open `.env` and set your secrets:

    ```env
    EXTRACTOR_API_KEY="your-super-secret-local-dev-key"
    GEMINI_API_KEY="your_google_gemini_api_key_here"
    ```

## ⚙️ Usage

To start the API server locally, simply run:

```bash
python main.py
```

*Alternatively, you can run it via Uvicorn:* `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

Once the server is running, navigate to the interactive Swagger UI documentation at:
👉 **[http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)**

*Note: All protected endpoints require the `x-api-key` header to match your configured `EXTRACTOR_API_KEY`.*

## 🌐 API Endpoints

The API v1 namespace currently exposes the following key routes:

  - `POST /api/v1/manifests/process`: Upload a messy shipping manifest (PDF/Image/Text) to extract tracking and line-item data.
  - `POST /api/v1/qc-reports/analyze`: Structure raw quality control notes into passed/failed schemas with severity scoring.
  - `POST /api/v1/vendor-emails/extract`: Extract inventory updates, expected dates, and backordered SKUs from vendor emails.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

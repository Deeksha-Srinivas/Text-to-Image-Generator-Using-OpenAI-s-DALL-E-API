
# Flask Text-to-Image Generator

A simple web-based application that generates images based on text descriptions using OpenAI's powerful DALL·E API. Built with Flask, this project demonstrates how generative AI can be integrated into a user-friendly application.

---

## Features
- Accepts a text description as input.
- Generates an AI-powered image matching the description.
- Displays the generated image directly in the web application.

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- An OpenAI account with an API key

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Text-to-Image-Generator-Using-OpenAI-s-DALL-E-API.git
   cd Text-to-Image-Generator-Using-OpenAI-s-DALL-E-API
   
2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Add Your OpenAI API Key:**
    -Create a .env file in the project root directory.
    -Add your OpenAI API key:

     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5. **Run the Application:**
   ```bash
   python app.py
6. **Open in Your Browser: Navigate to *http://127.0.0.1:5000***

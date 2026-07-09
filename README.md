# 👾 CodeReview AI – Intelligent Code Review Assistant

An AI-powered code review assistant built with **Streamlit**, **LangChain**, and **Groq** that analyzes source code, detects bugs, evaluates code quality, suggests optimizations, and generates refactored code with detailed explanations.

---

## ✨ Features

* 🔍 AI-powered code review
* ⭐ Overall code quality rating
* 🐞 Bug detection
* 🔒 Security issue identification
* ⚡ Performance optimization suggestions
* 🎨 Code style analysis
* ⏱️ Time and space complexity analysis
* 💻 AI-generated refactored code
* 📖 Explanation of suggested improvements
* 🌐 Support for multiple programming languages
* 🖥️ Interactive Streamlit interface

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Language:** Python
* **LLM Framework:** LangChain
* **LLM Provider:** Groq
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```text
CodeReview-AI/
│
├── app.py               # Streamlit application
├── prompts.py           # Prompt templates
├── requirements.txt     # Project dependencies
├── .gitignore
├── .env                 # Groq API Key (not committed)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shlokstack/CodeReview-AI.git
cd CodeReview-AI
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📋 How It Works

1. Select the programming language.
2. Choose the desired coding standard.
3. Paste your source code.
4. Click **Submit**.
5. The AI analyzes your code and returns:

   * Overall Rating
   * Summary
   * Strengths
   * Bugs
   * Security Issues
   * Performance Improvements
   * Code Style Issues
   * Time Complexity
   * Space Complexity
   * Refactored Code
   * Explanation of Changes

---

## Supported Languages

* Python
* C++
* Java
* JavaScript
* C
* Go
* Rust

---

## Example Output

* ⭐ Overall Rating: **8.8/10**
* 🐞 Bugs Found
* 🔒 Security Analysis
* ⚡ Performance Suggestions
* 🎨 Style Improvements
* ⏱️ Complexity Analysis
* 💻 Refactored Code
* 📖 Detailed Explanation

---

## Future Improvements

* 📁 Upload source code files
* 📄 Download review reports (PDF/Markdown)
* 🔗 GitHub repository review
* 💬 AI follow-up chat for reviewed code
* 🧪 Unit test generation
* ⚖️ Side-by-side code comparison
* 🤖 Multiple LLM support

---

## Author

**Shlok Shah**

GitHub: https://github.com/shlokstack

---

## License

This project is licensed under the MIT License.

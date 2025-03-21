# Project: Deep Research Assistant

A research assistant powered by LangChain and Gemini LLM, designed to help you conduct comprehensive research across academic sources, news, and the web.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshot](#screenshot)
- [Contributing](#contributing)

---

## About

This project is a research assistant tool that leverages state-of-the-art language models and external knowledge sources to provide detailed and accurate research insights. The tool is built using:

- **LangChain**: A framework for building AI-powered research tools
- **Gemini LLM**: For generating context-aware responses
- **Google Search API**: For broad web search
- **ArXiv API**: For academic paper access
- **Wikipedia API**: For general knowledge
- **DuckDuckGo**: For diverse web search

---

## Features

### 1. Multi-source Search
- **Google Search**: Access reliable, up-to-date information from the web
- **ArXiv**: Query academic papers for scholarly insights
- **Wikipedia**: Get summarized and detailed information
- **DuckDuckGo**: Perform broad web searches for diverse perspectives

### 2. AI-powered Analysis
- **Gemini LLM**: Generate context-aware responses
- **Zero-shot Reasoning**: Automatically connect information from different sources
- **Summarization**: Condense key points from search results

### 3. User Interface
- **Streamlit**: Access the tool via a web interface
- **Chat-like Interaction**: Engage with the research assistant naturally
- **Visual Results**: Side-by-side presentation of search results and analysis

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/deep-research-assistant.git
cd deep-research-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up API keys:
- Create a `.env` file in your project directory:
  ```bash
  echo "GOOGLE_CSE_ID=your_cse_id" >> .env
  echo "GOOGLE_API_KEY=your_api_key" >> .env
  ```
- Add your credentials to the `.gitignore` file to keep them secure.

4. Run the app:
```bash
streamlit run deep_research_assistant.py
```

---

## Usage

1. Open the app in your browser:
   - The app will be available at `http://localhost:8501`

2. Enter your research query in the chat interface:
   - Type your question or topic in the input box
   - Click "Send" to get a research response

3. View the results:
   - The assistant will display relevant information from multiple sources
   - Results are presented in a clean, organized format

---

## Screenshot

![Research Assistant Screenshot](https://via.placeholder.com/600x400?text=Research+Assistant)

*Note: Replace this placeholder with a screenshot of your app in action.*

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. Make sure to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes
4. Push to your new branch
5. Open a pull request against the `main` branch

---

## Notes

- The app requires an internet connection to access external APIs
- For production use, consider deploying it on a cloud platform like Streamlit Cloud
- The tool is currently available in English; translations are welcome
- Bugs and errors: feel free to report them in the issue tracker

---

This tool is designed to assist researchers and students in quickly gathering and analyzing information from multiple sources. It's a powerful but flexible solution that can be extended with additional features or connected to other tools in the LangChain ecosystem.

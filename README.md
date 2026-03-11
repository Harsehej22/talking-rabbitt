# 🐰 Talking Rabbitt – Conversational Analytics for Business Data

**Transform your business data into insights with natural language conversations.**

Talking Rabbitt is an innovative web application that allows business users to upload CSV datasets and ask natural language questions about their data. The system analyzes the dataset and returns clear text answers with automatic visualizations, eliminating the need to build complex dashboards.

## ✨ Features

- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT to understand and answer natural language questions
- 📊 **Automatic Visualizations**: Generates relevant charts based on query types
- 💬 **Chat Interface**: Maintains conversation history for continuous analysis
- 📁 **CSV Upload Support**: Easy data import with instant preview
- 🎯 **Business-Focused**: Designed for non-technical business users
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download the project files**
   ```bash
   # Make sure you have all files in one directory:
   # - app.py
   # - requirements.txt
   # - sample_sales_data.csv
   # - README.md
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

### First Time Setup

1. **Enter your OpenAI API key** in the sidebar
2. **Load sample data** using the "Load Sample Sales Data" button, or
3. **Upload your own CSV file** using the file uploader
4. **Start asking questions!**

## 💡 How to Use

### 1. Upload Data
- Click "Load Sample Sales Data" to try with pre-configured data, or
- Upload your own CSV file using the file uploader

### 2. Explore Your Data
- View dataset information (rows, columns, data types)
- Preview the first 10 rows of your data
- See available columns and their statistics

### 3. Ask Questions
Type questions in natural language, such as:

**Revenue Analysis:**
- "Which region had the highest revenue?"
- "What is the total revenue?"
- "Show revenue by region"
- "What's the average revenue?"

**Performance Comparison:**
- "Which quarter performed best?"
- "Compare regions by revenue"
- "Show me the top performing products"
- "What's the difference between North and South regions?"

**Trends and Patterns:**
- "How does revenue vary by quarter?"
- "Show revenue trends over time"
- "Which products are growing fastest?"

### 4. Get Insights
- Receive human-readable answers
- View automatic visualizations (bar charts for comparisons, line charts for trends)
- Maintain conversation history for follow-up questions

## 🏗️ Project Structure

```
talking-rabbitt-mvp/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── sample_sales_data.csv       # Sample dataset for demo
└── README.md                   # This file
```

## 📊 Sample Data

The included `sample_sales_data.csv` contains:
- **Region**: North, South, East, West
- **Product**: Laptop, Tablet, Phone
- **Quarter**: Q1, Q2, Q3
- **Revenue**: Sales figures in USD

This sample data allows you to immediately test all features without preparing your own dataset.

## 🔧 Technical Details

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Processing**: Pandas
- **AI/ML**: OpenAI GPT-3.5-turbo
- **Visualization**: Plotly, Matplotlib
- **Backend**: Python 3.8+

### Key Components

1. **Data Loading & Validation**
   - CSV file upload with error handling
   - Automatic data type detection
   - Missing value handling

2. **Natural Language Processing**
   - OpenAI API integration for question understanding
   - Context-aware responses based on dataset
   - Conversational memory

3. **Visualization Engine**
   - Automatic chart type selection
   - Bar charts for categorical comparisons
   - Line charts for time-series trends
   - Color-coded and labeled charts

4. **User Interface**
   - Chat-style conversation display
   - Responsive layout
   - Professional styling with custom CSS

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. **Create a GitHub repository** with all project files
2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
3. **Connect your GitHub account**
4. **Select the repository and branch**
5. **Set the main file path to `app.py`**
6. **Add your OpenAI API key** in the Secrets section
7. **Click Deploy**

### Manual Deployment

For production deployment on your own server:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-api-key-here"

# Run with custom port and host
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 🔒 Security & Privacy

- **API Keys**: Your OpenAI API key is stored in session state only
- **Data Privacy**: All data processing happens locally in your session
- **No Data Storage**: Uploaded data is not persisted after session ends
- **Secure Communication**: OpenAI API calls use HTTPS encryption

## 🤝 Contributing

This is an MVP demonstration. Potential enhancements include:

- [ ] Support for Excel files
- [ ] More visualization types (pie charts, scatter plots)
- [ ] Data cleaning suggestions
- [ ] Export functionality for charts and insights
- [ ] Multi-language support
- [ ] Advanced analytics (correlations, predictions)

## 📞 Support

If you encounter issues:

1. **Check your OpenAI API key** is valid and has credits
2. **Ensure CSV format** is correct (comma-separated, headers in first row)
3. **Verify Python version** is 3.8 or higher
4. **Check internet connection** for OpenAI API calls

## 📄 License

MIT License - feel free to use and modify for your projects.

---

**🐰 Talking Rabbitt © 2024 | Transform your data into conversations**

*Built with ❤️ using Streamlit, OpenAI, and Plotly*

# NQL Agent - Natural Language Query System

A powerful Natural Language Query (NQL) agent built with Python, LangChain, and React that allows users to query databases using natural language. The system supports both MongoDB and SQL databases, making it versatile for different data storage needs.

## 🚀 Features

- **Natural Language Processing**: Convert natural language queries into database queries using LangChain
- **Multi-Database Support**: Works with both MongoDB and SQL databases
- **RESTful API**: Clean API endpoints for frontend integration
- **React Frontend**: Modern, responsive user interface
- **Modular Architecture**: Well-organized codebase with separation of concerns

## 📁 Project Structure

```
NLQ/
├── app/                    # Application core
├── db/                     # Database configurations and utilities
│   ├── mongodb.py         # MongoDB connection and operations
│   ├── mysql_config.py    # MySQL/SQL database configuration
│   └── seed_mongo.py      # MongoDB data seeding script
├── routes/                 # API route handlers
│   └── query_route.py     # Query processing endpoints
├── services/               # Business logic and services
│   ├── mongo_chain.py     # MongoDB LangChain integration
│   ├── router.py          # Service routing logic
│   └── sql_chain.py 
 ── main.py       # SQL LangChain integration
├── .env                   # Environment variables
├── .env.example 
├── frontend/               # React frontend application
├               # Application entry point
          # Environment variables template
└── README.md              # Project documentation
```

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **LangChain** - For natural language processing and AI integration
- **FastAPI/Flask** - Web framework (inferred from structure)
- **MongoDB** - NoSQL database support
- **MySQL/PostgreSQL** - SQL database support

### Frontend
- **React** - User interface framework
- **Modern JavaScript**

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- Node.js 16+ and npm/yarn
- MongoDB (if using MongoDB features)
- MySQL/PostgreSQL (if using SQL features)
- OpenAI API key or other LLM provider credentials

## 🚀 Installation & Setup

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nitishrai1/NLQ.git
   cd NLQ
   ```



2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   # Database Configuration
   MONGODB_URI=mongodb://localhost:27017/nlq_db
   MYSQL_HOST=localhost
   MYSQL_USER=your_username
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=nlq_db
   
   # AI/LLM Configuration
   GEMINI_API_KEY=your_openai_api_key
   
   # Application Configuration
   DEBUG=True
   PORT=8000
   ```

5. **Initialize databases**
   ```bash
   # Seed MongoDB (if using MongoDB)
   python db/seed_mongo.py
   ```

6. **Run the backend server**
   ```bash
   python main.py
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the development server**
   ```bash
   npm start
   # or
   yarn start
   ```

## 🔧 Configuration

### Database Configuration

The application supports multiple database types:

- **MongoDB**: Configure connection in `db/mongodb.py`
- **SQL Databases**: Configure connection in `db/mysql_config.py`

### LangChain Configuration

The NQL processing is handled by:
- `services/mongo_chain.py` - For MongoDB queries
- `services/sql_chain.py` - For SQL queries

## 📚 API Documentation

### Query Endpoint

```
POST /api/query
```

**Request Body:**
```json
{
  "question:":"give me the data of all the client"
}
```

**Response:**
```json
{
  "question": "List the transactions above ₹1000.",
    "decided_data_source": "mysql",
    "format": "text",
    "response": {
        "type": "text",
        "message": "No data found for your query."
    }
}
```

## 🧪 Usage Examples

### Natural Language Queries

1. **MongoDB Examples:**
   - "Show me all products with price greater than $100"
   - "Find users who haven't logged in for 30 days"
   - "Get the top 10 best-selling products this month"

2. **SQL Examples:**
   - "List all customers from New York"
   - "Show sales data for the last quarter"
   - "Find employees with salary above average"

 ### work flow
 ![image](https://github.com/user-attachments/assets/c2c1e39b-5250-41bc-be92-ba12dfbbe88f)


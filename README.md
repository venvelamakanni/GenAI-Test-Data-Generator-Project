# GenAI Test Data Generator

A powerful FastAPI-based web application that leverages Google's Gemini 2.0 Flash LLM to generate comprehensive API test scenarios and pytest code. This tool helps developers automate the creation of test cases for their APIs, ensuring better test coverage and quality.

## 🌟 Features

### API Playground
- Generate test scenarios for multiple API endpoints in batch
- Support for various HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Multiple test scenario types:
  - Positive test cases
  - Negative test cases
  - Edge cases
  - Performance scenarios
  - Security test cases
- Interactive web interface for easy scenario generation

### Chatbot Interface
- Natural language interaction for test generation
- Intelligent intent classification
- Dynamic API details collection
- Real-time pytest code generation
- Support for complex API testing scenarios

### Core Features
- Asynchronous API endpoints
- Comprehensive logging system
- Error handling and validation
- CORS support
- Static file serving
- API documentation (Swagger UI and ReDoc)

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd genai-test-data-generator
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📁 Project Structure

```
genai_test_data_generator/
├── app/
│   ├── main.py             # FastAPI app instance
│   ├── core/               # Core configurations
│   │   └── config.py       # Settings and configuration
│   ├── schemas/            # Pydantic models
│   │   ├── playground.py   # Playground request/response models
│   │   └── chatbot.py      # Chatbot request/response models
│   ├── services/           # Business logic
│   │   └── llm_service.py  # Gemini LLM integration
│   ├── routers/            # API endpoints
│   │   ├── playground.py   # Playground routes
│   │   └── chatbot.py      # Chatbot routes
│   └── utils/              # Utility functions
│       └── logger.py       # Logging configuration
├── static/                 # Frontend files
│   ├── index.html         # Landing page
│   ├── playground.html    # Playground interface
│   └── chatbot.html       # Chatbot interface
├── logs/                   # Log files
├── tests/                  # Test files
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## 🎯 Usage Examples

### 1. Using the API Playground

1. Open [http://127.0.0.1:8000/static/playground.html](http://127.0.0.1:8000/static/playground.html)
2. Fill in the endpoint details:
   - API Endpoint: `/api/v1/users`
   - HTTP Method: POST
   - Description: "Creates a new user"
   - Select scenario types
3. Click "Generate Scenarios"

### 2. Using the Chatbot Interface

1. Open [http://127.0.0.1:8000/static/chatbot.html](http://127.0.0.1:8000/static/chatbot.html)
2. Type your request: "Generate tests for the login API"
3. Provide API details when prompted
4. Review and use the generated test code

### 3. Direct API Usage

#### Generate Test Scenarios
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/playground/generate-scenarios" \
  -H "Content-Type: application/json" \
  -d '{
    "endpoints": [
      {
        "endpoint": "/api/v1/users",
        "method": "POST",
        "description": "Creates a new user",
        "scenario_types": ["POSITIVE", "NEGATIVE"]
      }
    ]
  }'
```

#### Chat with the Bot
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/chatbot/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Generate tests for the login API"}'
```

## 📚 API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Testing

Run tests with coverage:
```bash
pytest --cov=app tests/
```

## 📝 Logging

Logs are stored in the `logs/` directory with rotation:
- Max file size: 10MB
- Keep 5 backup files
- Daily rotation
- Separate logs for:
  - Application logs (`app.log`)
  - Error logs (`error.log`)
  - LLM interactions (`llm.log`)

## 🔒 Security Considerations

- API keys are stored in environment variables
- CORS is configured for development (customize for production)
- Input validation using Pydantic models
- Rate limiting (to be implemented)
- Authentication (to be implemented)

## 🛠️ Configuration

Key configuration options in `app/core/config.py`:
- API version prefix
- Project name
- LLM model settings
- Logging configuration
- Test scenario types
- File paths

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## 📞 Support

For support, please:
1. Check the documentation
2. Open an issue
3. Contact the maintainers

## 🔄 Future Enhancements

- [ ] Add authentication
- [ ] Implement rate limiting
- [ ] Add more test scenario types
- [ ] Support for WebSocket testing
- [ ] Integration with CI/CD pipelines
- [ ] Custom test templates
- [ ] Test data generation
- [ ] Performance benchmarking 
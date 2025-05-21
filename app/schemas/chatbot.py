from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from .playground import HTTPMethod

class ChatMessage(BaseModel):
    message: str = Field(..., description="User's message")
    session_id: Optional[str] = Field(None, description="Optional session ID for conversation context")

class IntentClassification(BaseModel):
    intent: str = Field(..., description="Classified intent of the user's message")
    endpoint: Optional[str] = Field(None, description="Extracted API endpoint")
    method: Optional[HTTPMethod] = Field(None, description="Extracted HTTP method")
    requires_details: bool = Field(..., description="Whether additional API details are needed")

class ApiDetails(BaseModel):
    base_url: str = Field(..., description="Base URL of the API")
    headers: Dict[str, str] = Field(default_factory=dict, description="Request headers")
    request_body: Optional[Dict] = Field(None, description="Example request body")
    success_status_code: int = Field(200, description="Expected success status code")
    example_response: Optional[Dict] = Field(None, description="Example successful response")

class PytestGenerationRequest(BaseModel):
    intent_data: IntentClassification
    api_details: ApiDetails

class PytestGenerationResponse(BaseModel):
    code: str = Field(..., description="Generated pytest code")
    filename: str = Field(..., description="Suggested filename for the test file")
    test_count: int = Field(..., description="Number of test cases generated")

class ChatResponse(BaseModel):
    message: str = Field(..., description="Response message")
    intent: Optional[IntentClassification] = Field(None, description="Classified intent if applicable")
    pytest_code: Optional[PytestGenerationResponse] = Field(None, description="Generated pytest code if applicable") 
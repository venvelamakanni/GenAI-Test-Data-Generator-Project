from fastapi import APIRouter, HTTPException
from app.schemas.chatbot import (
    ChatMessage,
    ChatResponse,
    IntentClassification,
    PytestGenerationRequest,
    PytestGenerationResponse
)
from app.services.llm_service import llm_service
from app.utils.logger import get_logger

logger = get_logger("chatbot_router")
router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """
    Process a chat message and classify the intent.
    
    Args:
        message: ChatMessage containing user message and optional session ID
        
    Returns:
        ChatResponse with classified intent and optional follow-up message
    """
    try:
        logger.info(
            f"Processing chat message: {message.message}",
            extra={"session_id": message.session_id}
        )
        
        # TODO: Implement intent classification using LLM
        # For now, return a placeholder response
        return ChatResponse(
            message="I understand you want to generate API tests. Could you please provide more details about the API endpoint?",
            intent=IntentClassification(
                intent="generate_tests",
                requires_details=True
            )
        )
        
    except Exception as e:
        logger.error(f"Error processing chat message: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process chat message: {str(e)}"
        )

@router.post("/generate-pytest", response_model=PytestGenerationResponse)
async def generate_pytest(request: PytestGenerationRequest):
    """
    Generate pytest code based on intent classification and API details.
    
    Args:
        request: PytestGenerationRequest containing intent data and API details
        
    Returns:
        PytestGenerationResponse with generated code and filename
    """
    try:
        logger.info(
            "Generating pytest code",
            extra={
                "endpoint": request.intent_data.endpoint,
                "method": request.intent_data.method
            }
        )
        
        code = await llm_service.generate_pytest_code(
            endpoint=request.intent_data.endpoint or "",
            method=request.intent_data.method or "GET",
            base_url=request.api_details.base_url,
            headers=request.api_details.headers,
            request_body=request.api_details.request_body,
            success_status_code=request.api_details.success_status_code,
            example_response=request.api_details.example_response
        )
        
        # Generate filename based on endpoint
        endpoint_name = request.intent_data.endpoint or "unknown"
        filename = f"test_{endpoint_name.replace('/', '_').strip('_')}.py"
        
        # Count test cases (rough estimate based on number of test functions)
        test_count = code.count("def test_")
        
        return PytestGenerationResponse(
            code=code,
            filename=filename,
            test_count=test_count
        )
        
    except Exception as e:
        logger.error(f"Error generating pytest code: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate pytest code: {str(e)}"
        ) 
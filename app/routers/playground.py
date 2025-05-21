from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.playground import (
    BatchRequest,
    BatchResponse,
    EndpointResponse,
    TestScenario
)
from app.services.llm_service import llm_service
from app.utils.logger import get_logger

logger = get_logger("playground_router")
router = APIRouter()

@router.post("/generate-scenarios", response_model=BatchResponse)
async def generate_scenarios(request: BatchRequest):
    """
    Generate test scenarios for multiple API endpoints.
    
    Args:
        request: BatchRequest containing list of endpoints
        
    Returns:
        BatchResponse containing generated scenarios for each endpoint
    """
    try:
        results = []
        
        for endpoint_request in request.endpoints:
            logger.info(
                f"Generating scenarios for endpoint: {endpoint_request.endpoint}",
                extra={
                    "endpoint": endpoint_request.endpoint,
                    "method": endpoint_request.method,
                    "scenario_types": endpoint_request.scenario_types
                }
            )
            
            scenarios = await llm_service.generate_test_scenarios(
                endpoint=endpoint_request.endpoint,
                method=endpoint_request.method,
                description=endpoint_request.description,
                scenario_types=[t.value for t in endpoint_request.scenario_types]
            )
            
            # Convert scenarios to TestScenario objects
            test_scenarios = [
                TestScenario(
                    type=scenario["type"],
                    description=scenario["description"],
                    input=scenario["input"],
                    expected_output=scenario["expected_output"]
                )
                for scenario in scenarios
            ]
            
            results.append(
                EndpointResponse(
                    endpoint=endpoint_request.endpoint,
                    method=endpoint_request.method,
                    scenarios=test_scenarios
                )
            )
            
        return BatchResponse(results=results)
        
    except Exception as e:
        logger.error(f"Error generating scenarios: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate test scenarios: {str(e)}"
        ) 
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum

class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

class ScenarioType(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    EDGE_CASE = "EDGE_CASE"
    PERFORMANCE = "PERFORMANCE"
    SECURITY = "SECURITY"

class EndpointRequest(BaseModel):
    endpoint: str = Field(..., description="API endpoint path")
    method: HTTPMethod = Field(..., description="HTTP method")
    description: str = Field(..., description="Description of what the endpoint does")
    scenario_types: List[ScenarioType] = Field(
        default=[ScenarioType.POSITIVE, ScenarioType.NEGATIVE],
        description="Types of scenarios to generate"
    )

class BatchRequest(BaseModel):
    endpoints: List[EndpointRequest] = Field(
        ...,
        max_items=5,
        description="List of endpoints to generate scenarios for"
    )

class TestScenario(BaseModel):
    type: ScenarioType
    description: str
    input: str
    expected_output: str

class EndpointResponse(BaseModel):
    endpoint: str
    method: HTTPMethod
    scenarios: List[TestScenario]

class BatchResponse(BaseModel):
    results: List[EndpointResponse] 
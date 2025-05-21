import json
from typing import Dict, List, Optional, Union
import google.generativeai as genai
from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger("llm_service")

class LLMService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
        logger.info("LLM service initialized with Gemini model")

    def generate_content(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Generate content using the Gemini model.
        
        Args:
            prompt: The input prompt
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            Generated text response
        """
        try:
            logger.debug("Generating content with prompt", extra={"llm": True, "prompt": prompt})
            
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens
                }
            )
            
            result = response.text
            logger.debug("Content generated successfully", extra={"llm": True, "result": result})
            return result
            
        except Exception as e:
            logger.error(f"Error generating content: {str(e)}", extra={"llm": True})
            raise

    async def generate_test_scenarios(
        self,
        endpoint: str,
        method: str,
        description: str,
        scenario_types: List[str]
    ) -> List[Dict[str, str]]:
        """
        Generate test scenarios for an API endpoint.
        
        Args:
            endpoint: API endpoint path
            method: HTTP method
            description: Endpoint description
            scenario_types: List of scenario types to generate
            
        Returns:
            List of test scenarios with their types
        """
        prompt = f"""Generate test scenarios for the following API endpoint:
Endpoint: {endpoint}
Method: {method}
Description: {description}
Scenario Types: {', '.join(scenario_types)}

For each scenario type, provide:
1. A clear description of the test case
2. Expected input data
3. Expected response/behavior

Format the response as a JSON array of objects with the following structure:
[
    {{
        "type": "SCENARIO_TYPE",
        "description": "Test case description",
        "input": "Expected input data",
        "expected_output": "Expected response/behavior"
    }}
]

Ensure the response is valid JSON and only contains the array of scenarios."""

        try:
            response = self.generate_content(prompt, temperature=0.7)
            scenarios = json.loads(response)
            logger.info(f"Generated {len(scenarios)} test scenarios", extra={"llm": True})
            return scenarios
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {str(e)}", extra={"llm": True})
            raise
        except Exception as e:
            logger.error(f"Error generating test scenarios: {str(e)}", extra={"llm": True})
            raise

    async def generate_pytest_code(
        self,
        endpoint: str,
        method: str,
        base_url: str,
        headers: Dict[str, str],
        request_body: Optional[Dict] = None,
        success_status_code: int = 200,
        example_response: Optional[Dict] = None
    ) -> str:
        """
        Generate pytest code for testing an API endpoint.
        
        Args:
            endpoint: API endpoint path
            method: HTTP method
            base_url: Base URL of the API
            headers: Request headers
            request_body: Example request body
            success_status_code: Expected success status code
            example_response: Example successful response
            
        Returns:
            Generated pytest code as a string
        """
        prompt = f"""Generate a pytest test file for the following API endpoint:
Endpoint: {endpoint}
Method: {method}
Base URL: {base_url}
Headers: {json.dumps(headers, indent=2)}
Request Body: {json.dumps(request_body, indent=2) if request_body else 'None'}
Expected Success Status Code: {success_status_code}
Example Response: {json.dumps(example_response, indent=2) if example_response else 'None'}

Requirements:
1. Use the requests library
2. Include appropriate imports
3. Create a fixture for base_url and headers
4. Generate at least one positive test case
5. Generate at least one negative test case
6. Use appropriate pytest markers
7. Include clear test case descriptions
8. Add assertions for status codes and response data

Format the response as a Python code string with proper indentation.
The response should only contain the Python code, no explanations."""

        try:
            code = self.generate_content(prompt, temperature=0.3)
            logger.info("Generated pytest code successfully", extra={"llm": True})
            return code
        except Exception as e:
            logger.error(f"Error generating pytest code: {str(e)}", extra={"llm": True})
            raise

llm_service = LLMService() 
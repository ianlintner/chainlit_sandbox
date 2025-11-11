"""
Unit tests for the Goal-Seeking AI Chatbot app
"""

import os
import sys

import pytest

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestImports:
    """Test that all required modules can be imported"""

    def test_import_chainlit(self):
        """Test chainlit import"""
        import chainlit as cl

        assert cl is not None

    def test_import_openai(self):
        """Test openai import"""
        import openai

        assert openai is not None

    def test_import_dotenv(self):
        """Test dotenv import"""
        from dotenv import load_dotenv

        assert load_dotenv is not None

    def test_import_app(self):
        """Test that app module can be imported"""
        import app

        assert app is not None


class TestPromptStructure:
    """Test that all prompts are properly defined"""

    def test_system_prompt_exists(self):
        """Test SYSTEM_PROMPT exists and is not empty"""
        import app

        assert hasattr(app, "SYSTEM_PROMPT")
        assert isinstance(app.SYSTEM_PROMPT, str)
        assert len(app.SYSTEM_PROMPT) > 0

    def test_performance_eval_prompt_exists(self):
        """Test PERFORMANCE_EVAL_PROMPT exists and is not empty"""
        import app

        assert hasattr(app, "PERFORMANCE_EVAL_PROMPT")
        assert isinstance(app.PERFORMANCE_EVAL_PROMPT, str)
        assert len(app.PERFORMANCE_EVAL_PROMPT) > 0

    def test_topic_analysis_prompt_exists(self):
        """Test TOPIC_ANALYSIS_PROMPT exists and is not empty"""
        import app

        assert hasattr(app, "TOPIC_ANALYSIS_PROMPT")
        assert isinstance(app.TOPIC_ANALYSIS_PROMPT, str)
        assert len(app.TOPIC_ANALYSIS_PROMPT) > 0

    def test_strategy_prompt_exists(self):
        """Test STRATEGY_PROMPT exists and is not empty"""
        import app

        assert hasattr(app, "STRATEGY_PROMPT")
        assert isinstance(app.STRATEGY_PROMPT, str)
        assert len(app.STRATEGY_PROMPT) > 0

    def test_response_generation_prompt_exists(self):
        """Test RESPONSE_GENERATION_PROMPT exists and is not empty"""
        import app

        assert hasattr(app, "RESPONSE_GENERATION_PROMPT")
        assert isinstance(app.RESPONSE_GENERATION_PROMPT, str)
        assert len(app.RESPONSE_GENERATION_PROMPT) > 0


class TestPromptContent:
    """Test that prompts contain expected keywords"""

    def test_system_prompt_contains_key_elements(self):
        """Test SYSTEM_PROMPT contains key parody elements"""
        import app

        prompt = app.SYSTEM_PROMPT.lower()
        assert "switch 1" in prompt or "switch 2" in prompt
        assert "hustle" in prompt or "grinding" in prompt
        assert "parody" in prompt or "over-the-top" in prompt

    def test_performance_eval_contains_metrics(self):
        """Test PERFORMANCE_EVAL_PROMPT mentions evaluation metrics"""
        import app

        prompt = app.PERFORMANCE_EVAL_PROMPT.lower()
        assert "progress" in prompt or "score" in prompt or "interest" in prompt

    def test_topic_analysis_contains_relevance(self):
        """Test TOPIC_ANALYSIS_PROMPT mentions topic analysis"""
        import app

        prompt = app.TOPIC_ANALYSIS_PROMPT.lower()
        assert "topic" in prompt or "relevant" in prompt or "conversation" in prompt

    def test_strategy_prompt_contains_strategies(self):
        """Test STRATEGY_PROMPT mentions strategy selection"""
        import app

        prompt = app.STRATEGY_PROMPT.lower()
        assert "strategy" in prompt or "approach" in prompt

    def test_response_generation_mentions_response(self):
        """Test RESPONSE_GENERATION_PROMPT is about generating responses"""
        import app

        prompt = app.RESPONSE_GENERATION_PROMPT.lower()
        assert "response" in prompt or "reply" in prompt or "message" in prompt


class TestFunctionExistence:
    """Test that all required functions exist and are properly defined"""

    def test_analyze_performance_exists(self):
        """Test analyze_performance function exists"""
        import app

        assert hasattr(app, "analyze_performance")
        assert callable(app.analyze_performance)

    def test_analyze_topic_exists(self):
        """Test analyze_topic function exists"""
        import app

        assert hasattr(app, "analyze_topic")
        assert callable(app.analyze_topic)

    def test_determine_strategy_exists(self):
        """Test determine_strategy function exists"""
        import app

        assert hasattr(app, "determine_strategy")
        assert callable(app.determine_strategy)

    def test_generate_response_exists(self):
        """Test generate_response function exists"""
        import app

        assert hasattr(app, "generate_response")
        assert callable(app.generate_response)

    def test_start_handler_exists(self):
        """Test start handler exists"""
        import app

        assert hasattr(app, "start")
        assert callable(app.start)

    def test_main_handler_exists(self):
        """Test main handler exists"""
        import app

        assert hasattr(app, "main")
        assert callable(app.main)


class TestAsyncFunctions:
    """Test that functions are properly defined as async"""

    def test_analyze_performance_is_async(self):
        """Test analyze_performance is an async function"""
        import inspect

        import app

        assert inspect.iscoroutinefunction(app.analyze_performance)

    def test_analyze_topic_is_async(self):
        """Test analyze_topic is an async function"""
        import inspect

        import app

        assert inspect.iscoroutinefunction(app.analyze_topic)

    def test_determine_strategy_is_async(self):
        """Test determine_strategy is an async function"""
        import inspect

        import app

        assert inspect.iscoroutinefunction(app.determine_strategy)

    def test_generate_response_is_async(self):
        """Test generate_response is an async function"""
        import inspect

        import app

        assert inspect.iscoroutinefunction(app.generate_response)


class TestClientInitialization:
    """Test OpenAI client initialization"""

    def test_get_client_function_exists(self):
        """Test get_client function exists"""
        import app

        assert hasattr(app, "get_client")
        assert callable(app.get_client)

    def test_get_client_requires_api_key(self):
        """Test get_client raises error without API key"""
        import app

        # Clear any existing client
        app._client = None
        # Clear environment variable
        original_key = os.environ.get("OPENAI_API_KEY")
        if "OPENAI_API_KEY" in os.environ:
            del os.environ["OPENAI_API_KEY"]

        try:
            with pytest.raises(ValueError, match="OPENAI_API_KEY"):
                app.get_client()
        finally:
            # Restore original key if it existed
            if original_key:
                os.environ["OPENAI_API_KEY"] = original_key
            app._client = None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

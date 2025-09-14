#!/usr/bin/env python3
"""
Test script for OpenMemory provider configuration.

This script tests the new provider configuration system to ensure it works correctly
with different LLM and embedder providers.
"""

import json
import requests
import time
import sys
from typing import Dict, Any

# Configuration
API_BASE_URL = "http://localhost:8765"
TEST_USER_ID = "test_user"

def test_api_connection():
    """Test if the API is accessible."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/config/")
        if response.status_code == 200:
            print("✅ API connection successful")
            return True
        else:
            print(f"❌ API connection failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ API connection failed: Could not connect to server")
        return False

def get_current_config():
    """Get the current configuration."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/config/")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get current config: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error getting current config: {e}")
        return None

def get_supported_providers():
    """Get the list of supported providers."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/config/providers")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get supported providers: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error getting supported providers: {e}")
        return None

def test_provider_config(provider: str, config: Dict[str, Any], config_type: str):
    """Test a specific provider configuration."""
    print(f"\n🧪 Testing {config_type} provider: {provider}")
    
    # Update the configuration
    update_data = {
        "mem0": {
            config_type: {
                "provider": provider,
                "config": config
            }
        }
    }
    
    try:
        response = requests.put(
            f"{API_BASE_URL}/api/v1/config/",
            json=update_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print(f"✅ {config_type} configuration updated successfully")
            
            # Wait a moment for the configuration to take effect
            time.sleep(2)
            
            # Test memory operations
            if test_memory_operations():
                print(f"✅ {provider} {config_type} working correctly")
                return True
            else:
                print(f"❌ {provider} {config_type} memory operations failed")
                return False
        else:
            print(f"❌ Failed to update {config_type} configuration: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing {provider} {config_type}: {e}")
        return False

def test_memory_operations():
    """Test basic memory operations."""
    try:
        # Test creating a memory
        create_data = {
            "user_id": TEST_USER_ID,
            "text": "This is a test memory for provider configuration testing.",
            "metadata": {"test": True},
            "app": "test_app"
        }
        
        response = requests.post(
            f"{API_BASE_URL}/api/v1/memories/",
            json=create_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Memory creation successful")
            
            # Test searching memories
            search_response = requests.get(
                f"{API_BASE_URL}/api/v1/memories/",
                params={"user_id": TEST_USER_ID, "search_query": "test memory"}
            )
            
            if search_response.status_code == 200:
                print("✅ Memory search successful")
                return True
            else:
                print(f"❌ Memory search failed: {search_response.status_code}")
                return False
        else:
            print(f"❌ Memory creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing memory operations: {e}")
        return False

def test_openai_config():
    """Test OpenAI configuration."""
    config = {
        "model": "gpt-4o-mini",
        "temperature": 0.1,
        "max_tokens": 2000,
        "api_key": "env:OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1"
    }
    return test_provider_config("openai", config, "llm")

def test_ollama_config():
    """Test Ollama configuration."""
    config = {
        "model": "llama3.1:latest",
        "temperature": 0.1,
        "max_tokens": 2000,
        "ollama_base_url": "http://host.docker.internal:11434"
    }
    return test_provider_config("ollama", config, "llm")

def test_anthropic_config():
    """Test Anthropic configuration."""
    config = {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.1,
        "max_tokens": 2000,
        "anthropic_api_key": "env:ANTHROPIC_API_KEY"
    }
    return test_provider_config("anthropic", config, "llm")

def test_together_config():
    """Test Together AI configuration."""
    config = {
        "model": "meta-llama/Llama-3.1-8B-Instruct-Turbo",
        "temperature": 0.1,
        "max_tokens": 2000,
        "together_api_key": "env:TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1"
    }
    return test_provider_config("together", config, "llm")

def test_groq_config():
    """Test Groq configuration."""
    config = {
        "model": "llama-3.1-8b-instant",
        "temperature": 0.1,
        "max_tokens": 2000,
        "groq_api_key": "env:GROQ_API_KEY",
        "base_url": "https://api.groq.com/openai/v1"
    }
    return test_provider_config("groq", config, "llm")

def test_embedder_configs():
    """Test embedder configurations."""
    print("\n🧪 Testing Embedder Configurations")
    
    # Test OpenAI embedder
    openai_embedder_config = {
        "model": "text-embedding-3-small",
        "api_key": "env:OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1"
    }
    test_provider_config("openai", openai_embedder_config, "embedder")
    
    # Test Ollama embedder
    ollama_embedder_config = {
        "model": "nomic-embed-text:latest",
        "ollama_base_url": "http://host.docker.internal:11434"
    }
    test_provider_config("ollama", ollama_embedder_config, "embedder")

def reset_to_default():
    """Reset configuration to default."""
    try:
        response = requests.post(f"{API_BASE_URL}/api/v1/config/reset")
        if response.status_code == 200:
            print("✅ Configuration reset to default")
            return True
        else:
            print(f"❌ Failed to reset configuration: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error resetting configuration: {e}")
        return False

def main():
    """Main test function."""
    print("🚀 OpenMemory Provider Configuration Test")
    print("=" * 50)
    
    # Test API connection
    if not test_api_connection():
        print("\n❌ Cannot proceed without API connection")
        sys.exit(1)
    
    # Get current configuration
    print("\n📋 Current Configuration:")
    current_config = get_current_config()
    if current_config:
        print(json.dumps(current_config, indent=2))
    
    # Get supported providers
    print("\n📋 Supported Providers:")
    providers = get_supported_providers()
    if providers:
        print(f"LLM Providers: {len(providers.get('llm_providers', []))}")
        print(f"Embedder Providers: {len(providers.get('embedder_providers', []))}")
    
    # Test LLM configurations
    print("\n🧪 Testing LLM Configurations")
    print("-" * 30)
    
    llm_tests = [
        ("OpenAI", test_openai_config),
        ("Ollama", test_ollama_config),
        ("Anthropic", test_anthropic_config),
        ("Together AI", test_together_config),
        ("Groq", test_groq_config),
    ]
    
    llm_results = []
    for name, test_func in llm_tests:
        try:
            result = test_func()
            llm_results.append((name, result))
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")
            llm_results.append((name, False))
    
    # Test embedder configurations
    test_embedder_configs()
    
    # Summary
    print("\n📊 Test Summary")
    print("=" * 50)
    
    print("\nLLM Provider Results:")
    for name, result in llm_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {name}: {status}")
    
    # Reset to default
    print("\n🔄 Resetting to default configuration...")
    reset_to_default()
    
    print("\n✨ Test completed!")

if __name__ == "__main__":
    main()

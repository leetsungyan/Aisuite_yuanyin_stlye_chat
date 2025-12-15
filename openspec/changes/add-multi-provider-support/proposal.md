## Why
Currently the app only supports Groq provider. Adding support for multiple AI providers (OpenAI, Mistral, etc.) would give users more options and improve reliability.

## What Changes
- Add configuration for multiple providers
- Modify the reply function to accept provider parameter
- Update UI to allow provider selection
- **BREAKING**: Change API key handling to support multiple keys

## Impact
- Affected specs: thinking-generator capability
- Affected code: main script, reply function, gradio interface
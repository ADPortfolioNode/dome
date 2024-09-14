# OpenAI API Endpoints Catalogue

## Models
- `GET /v1/models`: Lists the currently available models
- `GET /v1/models/{model}`: Retrieves a specific model

## Completions
- `POST /v1/completions`: Creates a completion for the provided prompt and parameters

## Chat
- `POST /v1/chat/completions`: Creates a chat completion for the provided messages and parameters

## Edits
- `POST /v1/edits`: Creates an edited version of the provided input

## Images
- `POST /v1/images/generations`: Creates an image from a text prompt
- `POST /v1/images/edits`: Creates an edited or extended image given an original image and a prompt
- `POST /v1/images/variations`: Creates a variation of a given image

## Embeddings
- `POST /v1/embeddings`: Creates an embedding vector representing the input text

## Audio
- `POST /v1/audio/transcriptions`: Transcribes audio into the input language
- `POST /v1/audio/translations`: Translates audio into English

## Files
- `GET /v1/files`: Lists files that have been uploaded
- `POST /v1/files`: Upload a file that can be used across various endpoints
- `DELETE /v1/files/{file_id}`: Delete a file
- `GET /v1/files/{file_id}`: Retrieves information about a specific file
- `GET /v1/files/{file_id}/content`: Retrieves the contents of the specified file

## Fine-tunes
- `POST /v1/fine-tunes`: Creates a job that fine-tunes a specified model
- `GET /v1/fine-tunes`: List your organization's fine-tuning jobs
- `GET /v1/fine-tunes/{fine_tune_id}`: Gets info about a specific fine-tune job
- `POST /v1/fine-tunes/{fine_tune_id}/cancel`: Cancels a fine-tune job

## Moderations
- `POST /v1/moderations`: Classifies if text violates OpenAI's Content Policy


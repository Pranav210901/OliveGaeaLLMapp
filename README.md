# COGVLM (model)
## COGVLM.PY
This project utilizes CogVLM2, a conversational visual-language model, to handle user queries with or without image input. The model is based on the Llama 3 architecture, fine-tuned for both natural language processing and image comprehension. The code uses Hugging Face Transformers, PyTorch, and PIL to interact with the model.

---

## Requirements

Ensure the following packages are installed:
Use the following command based on your Python version:

```bash
pip install -r requirements.txt
```

**requirements.txt** contains the following:
- xformers
- torch>=2.0.0
- torchvision
- transformers>=4.40
- huggingface-hub>=0.23.0
- pillow
- chainlit>=1.0
- pydantic>=2.7.1
- timm>=0.9.16
- openai>=1.30.1
- loguru>=0.7.2
- pydantic>=2.7.1
- einops
- sse-starlette>=2.1.0
- bitsandbytes>=0.43.1 (for int4 quantization)

---

## How It Works

1. **Model Setup**:
   The model weights and tokenizer are downloaded from Hugging Face and loaded into memory with the necessary precision (bfloat16 or float16 based on GPU capabilities).

2. **Handling Image Input**:
   If an image is provided, it is processed with PIL and passed to the model along with the user query. The image must be in RGB format for proper processing.

3. **Conversation History**:
   The code maintains a conversation history that is passed to the model to simulate continuous interaction between the user and the AI assistant.

4. **Text-Only or Multimodal**:
   If no image is provided, the conversation defaults to text-only mode. If an image is provided, it leverages both image and text inputs to generate more contextually aware responses.

---

## Model Usage

1. **Download the Model**:
   The model is downloaded from Hugging Face using the `snapshot_download()` function and stored locally.

2. **Text/Visual Input**:
   You can query the model with or without an image.

3. **Generate Responses**:
   The model generates responses based on user input and past conversation history.

### Running the Code (Without Flask)
1. **Prepare the environment**:
   Ensure all dependencies are installed.

2. **Configure Image Path**:
   Update the image path in the code: `image_path = '/path/to/your/image.jpeg'`.

3. **Start the Flask Server (optional)**:
   The server can be started to enable web-based interaction.

4. **Run the Script**:
   Execute the Python script to interact with the model:
   ```bash
   python3 cogvlm.py
   ```

---

## Example Usage

- **Text-Only Conversation**:
  If no image is provided, the code simulates a regular conversation between the user and the assistant. The assistant responds based on previous inputs and conversation history.

- **Text and Image Input**:
  When an image is provided, the model incorporates visual data into the response generation process, giving more context-aware and detailed answers.

---

## Key Variables

- **MODEL_PATH**:
  The path where the model is stored locally.

- **DEVICE**:
  The device (CPU/GPU) to run the model on.

- **TORCH_TYPE**:
  The precision used by the model, determined by the available hardware.

- **gen_kwargs**:
  Generation settings like max token length.

---

## Notes

- **CUDA**:
  Ensure your environment supports CUDA for optimal performance. If no GPU is available, the model will default to CPU.

- **Memory**:
  Depending on the hardware and user preferences for using int-8 quantization, the model may require significant memory resources. The code uses `low_cpu_mem_usage=True` to minimize resource consumption.

---
    
## COGVLM FLASK APPLICATION

This is a Flask-based web application that allows users to upload an image via a POST request, 
and execute a Python script (cogvlm.py) for generating a response based on a text query and 
an optional image input.

---------------------------------------------------------------------
HOW TO RUN THE APPLICATION:

1. Install Requirements:
Ensure all necessary dependencies are installed by running:

    pip install -r requirements.txt

2. Start the Flask Server:
To start the Flask server, run the following command:

    python3 app.py

The server will not start at http://localhost:8000 by default. 
Ensure use at http://34.45.152.152/

---------------------------------------------------------------------
API ENDPOINTS:

1. POST /api:
    Description: Uploads an image to the server.

    Usage: Use this endpoint to upload an image for model processing. The image is stored in 
           the 'uploads/' directory.

    Example:
    curl -X POST -F file=@path_to_image http://34.45.152.152/api

2. GET /api:
    Description: Runs the cogvlm.py script and returns the model's response based on the user 
                 query and the uploaded image.

    Example:
    curl http://34.45.152.152/api

---------------------------------------------------------------------
PROJECT STRUCTURE:

├── app.py                # Main Flask application

├── cogvlm.py             # Model script for handling queries

├── uploads/              # Directory for storing uploaded images

├── requirements.txt      # Required dependencies

└── README.txt            # This documentation

---------------------------------------------------------------------
NOTES:

- Ensure that CUDA is enabled on your system for optimal performance if you have a compatible GPU.
- The 'uploads/' directory will be created automatically if it doesn't exist.

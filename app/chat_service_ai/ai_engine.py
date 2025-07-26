# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# chat_history_ids = None

# async def chat_with_ai(prompt: str) -> str:
#     global chat_history_ids

   
#     new_input = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

    
#     if chat_history_ids is not None:
#         input_ids = torch.cat([chat_history_ids, new_input], dim=-1)
#     else:
#         input_ids = new_input

  
#     output_ids = model.generate(
#         input_ids,
#         max_length=1000,
#         pad_token_id=tokenizer.eos_token_id,
#         do_sample=True,
#         top_k=50,
#         top_p=0.95
#     )

    
#     chat_history_ids = output_ids

    
#     response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

#     return response.strip()
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

model_id = "microsoft/phi-2"  # lightweight and free
device = 0 if torch.cuda.is_available() else -1

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

async def chat_with_ai(prompt: str) -> str:
    try:
        response = generator(prompt, max_length=200, do_sample=True, top_k=50, top_p=0.95)[0]["generated_text"]
        # Extract only the AI's answer part if needed
        return response[len(prompt):].strip()
    except Exception as e:
        return f"Error: {str(e)}"

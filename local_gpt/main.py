"""from llama_cpp import Llama

# Load the GGUF model
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",  # path to your .gguf model
    n_ctx=2048,          # context window size
    n_threads=8,         # adjust based on your CPU
    use_mlock=True       # optional, locks model in RAM
)

# Instruct-style prompt
prompt = "### Instruction:\nWhat is the capital of India?\n\n### Response:"

# Run inference
output = llm(prompt, max_tokens=100, temperature=0.7, stop=["###"])

print("Model Response:\n", output["choices"][0]["text"].strip())"""


"""from llama_cpp import Llama

# Load the GGUF model
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",  # path to your .gguf model
    n_ctx=2048,          # context window size
    n_threads=8,         # adjust based on your CPU
    use_mlock=True       # optional, locks model in RAM
)

# Take user input
user_question = input("Ask your question: ")

# Format in instruct-style prompt
prompt = f"### Instruction:\n{user_question}\n\n### Response:"

# Run inference
output = llm(prompt, max_tokens=100, temperature=0.7, stop=["###"])

# Print response
print("\nModel Response:\n", output["choices"][0]["text"].strip())"""



from llama_cpp import Llama

# Load the GGUF model
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",  # path to your .gguf model
    n_ctx=2048,          # context window size
    n_threads=8,         # adjust based on your CPU
    use_mlock=True       # optional, locks model in RAM
)

print("Say 'hii' to start chatting with the model. Say 'thanks' to exit.")

# Start the loop
while True:
    user_input = input("\nYou: ").strip().lower()

    if user_input == "thanks":
        print("Model: You're welcome! Have a great day 😊")
        break
    elif user_input == "hii":
        print("Model: Hello! Ask me anything.")
        continue
    elif not user_input:
        print("Model: Please type something.")
        continue

    # Format prompt
    prompt = f"### Instruction:\n{user_input}\n\n### Response:"

    # Run inference
    output = llm(prompt, max_tokens=100, temperature=0.7, stop=["###"])

    # Display model's response
    print("\nModel:", output["choices"][0]["text"].strip())


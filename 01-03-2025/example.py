from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
output = generator("Hello, I am a language model.", max_length=50)

print(output)

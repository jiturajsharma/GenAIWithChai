import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')
print("Vocab Size", encoder.n_vocab)

text = "The cat sat on the mat."
tokens = encoder.encode(text)
print("Tokens:", tokens)
print("Decoded:", encoder.decode(tokens))
print("Token Count:", len(tokens))

# Vector Embeddings -> Semantic meaning
# Tokenization -> Text to tokens
# Text to tokens -> Tokenization
# Tokens -> Vector Embeddings

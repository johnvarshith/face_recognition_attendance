import pickle

with open('encodings.pkl', 'rb') as f:
    encodings = pickle.load(f)

print(encodings)

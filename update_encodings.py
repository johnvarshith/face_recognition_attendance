import pickle

# Load the existing encodings
with open('encodings.pkl', 'rb') as f:
    encodings = pickle.load(f)

# Update the key "John" to "Messi"
if "John" in encodings:
    encodings["Messi"] = encodings.pop("John")

# Save the updated encodings back to the file
with open('encodings.pkl', 'wb') as f:
    pickle.dump(encodings, f)

print("Updated encodings: John -> Messi")

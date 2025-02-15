import json

def sort_knowledge_base(file_path='knowledge_base.json'):
    with open(file_path, 'r') as file:
        knowledge_base = json.load(file)

    # Sort questions alphabetically
    knowledge_base["questions"].sort(key=lambda q: q["question"])

    with open(file_path, 'w') as file:
        json.dump(knowledge_base, file, indent=4)

# Run the function
sort_knowledge_base()
print("✅ Knowledge base sorted successfully!")

from transformers import BertTokenizer

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize and prepare dataset
def tokenize_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
print(tokenized_dataset)

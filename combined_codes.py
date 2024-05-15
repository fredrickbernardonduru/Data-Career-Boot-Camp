from datasets import load_dataset
from transformers import BertTokenizer, BertForSequenceClassification, TrainingArguments, Trainer

# Load MultiNLI dataset
dataset = load_dataset("multi_nli")

# Tokenize and prepare dataset
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
def tokenize_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Fine-tune BERT model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
training_args = TrainingArguments("output_dir")
trainer = Trainer(
    model=model, args=training_args, train_dataset=tokenized_dataset["train"], eval_dataset=tokenized_dataset["validation"]
)
trainer.train()

# Evaluate fine-tuned model
eval_results = trainer.evaluate(tokenized_dataset["test"])
accuracy = eval_results["eval_accuracy"]
f1_score = eval_results["eval_f1"]

print(f"Accuracy: {accuracy}")
print(f"F1 Score: {f1_score}")

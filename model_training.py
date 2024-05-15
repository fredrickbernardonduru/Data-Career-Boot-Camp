from transformers import BertForSequenceClassification, TrainingArguments, Trainer
from datasets import load_from_disk

# Load tokenized dataset
tokenized_dataset = load_from_disk("tokenized_dataset")

# Fine-tune BERT model for three-way classification
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
training_args = TrainingArguments("output_dir", evaluation_strategy="epoch")
trainer = Trainer(
    model=model, args=training_args, train_dataset=tokenized_dataset["train"], eval_dataset=tokenized_dataset["validation"]
)
trainer.train()

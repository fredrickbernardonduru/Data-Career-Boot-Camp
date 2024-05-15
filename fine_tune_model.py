from transformers import BertForSequenceClassification, TrainingArguments, Trainer

# Fine-tune BERT model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
training_args = TrainingArguments("output_dir")
trainer = Trainer(
    model=model, args=training_args, train_dataset=tokenized_dataset["train"], eval_dataset=tokenized_dataset["validation"]
)
trainer.train()

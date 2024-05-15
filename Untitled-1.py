from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
import torch
dataset = load_dataset("multi_nli")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)  # 3 labels: entailment, contradiction, neutral
training_args = TrainingArguments(
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    evaluation_strategy="epoch",
    logging_dir="./logs",
    output_dir="./results",
    overwrite_output_dir=True,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation_matched"],
    tokenizer=tokenizer,
)
trainer.train()
model.save_pretrained("./fine-tuned-model")
tokenizer.save_pretrained("./fine-tuned-model")
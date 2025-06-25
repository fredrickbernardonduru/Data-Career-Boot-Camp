from transformers import BertForSequenceClassification, BertTokenizer

# Load BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)  # 3 labels for NLI task
import torch
from datasets import load_dataset

# Load MultiNLI dataset
dataset = load_dataset('multi_nli')

# Tokenize and encode text data
def tokenize_data(example):
    return tokenizer(example['premise'], example['hypothesis'], truncation=True, padding='max_length')

tokenized_dataset = dataset.map(tokenize_data, batched=True)
from transformers import TrainingArguments, Trainer

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',          # Directory for saving model checkpoints and logs
    num_train_epochs=3,              # Number of training epochs
    per_device_train_batch_size=8,   # Batch size per GPU/CPU during training
    per_device_eval_batch_size=16,   # Batch size for evaluation
    warmup_steps=500,                # Warmup steps for learning rate scheduler
    weight_decay=0.01,               # Weight decay for optimizer
    logging_dir='./logs',            # Directory for storing logs
    logging_steps=100,               # Log every X updates steps
)

# Initialize Trainer
trainer = Trainer(
    model=model,                     # The instantiated 🤗 Transformers model to be trained
    args=training_args,              # Training arguments
    train_dataset=tokenized_dataset['train'],  # Training dataset
    eval_dataset=tokenized_dataset['validation_matched'],  # Evaluation dataset (matched setting)
)
# Fine-tune the model
trainer.train()
# Evaluate the fine-tuned model
evaluation_results = trainer.evaluate(eval_dataset=tokenized_dataset['validation_mismatched'])
print(evaluation_results)
# Assuming you have a separate evaluation dataset in a similar format
eval_dataset = load_dataset('your_evaluation_dataset_name')
tokenized_eval_dataset = eval_dataset.map(tokenize_data, batched=True)
# Assuming you have a separate evaluation dataset in a similar format
eval_dataset = load_dataset('your_evaluation_dataset_name')
tokenized_eval_dataset = eval_dataset.map(tokenize_data, batched=True)
from sklearn.metrics import accuracy_score, f1_score

# Get predictions from the fine-tuned model
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average='weighted')  # Calculate F1 score
    return {'accuracy': acc, 'f1_score': f1}

# Evaluate the fine-tuned model on the evaluation dataset
evaluation_results = trainer.evaluate(eval_dataset=tokenized_eval_dataset, metric_key_prefix='eval')
print("Evaluation Results:")
for key, value in evaluation_results.items():
    print(f"{key}: {value}")

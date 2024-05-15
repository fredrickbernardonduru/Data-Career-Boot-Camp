# Evaluate fine-tuned model
eval_results = trainer.evaluate(tokenized_dataset["test"])
accuracy = eval_results["eval_accuracy"]
f1_score = eval_results["eval_f1"]

print(f"Accuracy: {accuracy}")
print(f"F1 Score: {f1_score}")

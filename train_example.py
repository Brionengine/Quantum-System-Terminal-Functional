from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
import pandas as pd
from datasets import Dataset

# Load and prepare data
data = pd.read_csv("data.csv")  # Contains input commands and expected outputs
dataset = Dataset.from_pandas(data)

# Load pre-trained T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Tokenize the data
def preprocess(data):
    return tokenizer(data['input'], padding="max_length", truncation=True, max_length=512)

tokenized_data = dataset.map(preprocess, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01
)

# Create a Trainer and train the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data,
)

# Train the model
trainer.train()

import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertForMaskedLM, AdamW
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

# Define a simple dataset class for emotion classification
class EmotionDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        label = self.labels[idx]

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

# Fine-tuning function
def fine_tune_emotion_model(model, train_dataset, val_dataset, optimizer, epochs):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.train()

    for epoch in range(epochs):
        train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
        val_loader = DataLoader(val_dataset, batch_size=8)

        total_loss = 0

        for batch in tqdm(train_loader, desc=f'Epoch {epoch + 1}'):
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            total_loss += loss.item()

            loss.backward()
            optimizer.step()

        avg_train_loss = total_loss / len(train_loader)

        print(f'Epoch {epoch + 1}/{epochs}, Train Loss: {avg_train_loss:.4f}')

# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=NUM_LABELS)

# Fine-tune the model on your emotion-labeled dataset
train_dataset = EmotionDataset(train_texts, train_labels, tokenizer, max_length=128)
val_dataset = EmotionDataset(val_texts, val_labels, tokenizer, max_length=128)

optimizer = AdamW(model.parameters(), lr=2e-5)
fine_tune_emotion_model(model, train_dataset, val_dataset, optimizer, epochs=3)

# Now, let's define a function to generate responses based on the detected emotion
def generate_response(model, tokenizer, user_input, emotion):
    inputs = tokenizer.encode_plus(user_input, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Classify emotion
    outputs = model(input_ids, attention_mask=attention_mask)
    predicted_class = torch.argmax(outputs.logits).item()

    # Now you have the predicted emotion class, you can use it to generate a response
    if predicted_class == 0:  # Assuming 0 corresponds to 'happy'
        return "That's great to hear!"
    elif predicted_class == 1:  # Assuming 1 corresponds to 'sad'
        return "I'm sorry to hear that. Is there anything I can do to help?"
    # Add more conditions for other emotions

# Example usage
user_input = "I just got a promotion at work!"
emotion = generate_emotion(model, tokenizer, user_input)
response = generate_response(model, tokenizer, user_input, emotion)
print(response)

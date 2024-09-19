from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class NLPEngine:
    def __init__(self, model_name='t5-base'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def parse_input(self, user_input):
        prompt = f"Translate this into a shell command: {user_input}"
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=100, num_beams=5, early_stopping=True)
        command = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return command.strip()

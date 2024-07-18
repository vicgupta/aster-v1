from ollama import Client


class OllamaChat:

    def __init__(self, host: str = "http://localhost:11434", model: str = "llama3"):
        self._host = host
        self._model = model
        self._ollama = Client(host)

    def ask(
        self,
        prompt: str,
        format: str = "",
        temperature: float = 0.5,
        context_window: int = 4096,
    ):
        return self._ollama.chat(
            model=self._model,
            messages=prompt,
            format=format,
            options={
                "temperature": temperature,
                "num_ctx": context_window,
            },
        )["message"]["content"]

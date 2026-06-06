# openclaw-experiment

A small Python script that generates a message with a local [Ollama](https://ollama.com) model and broadcasts it to a list of recipients over WhatsApp using the [`openclaw`](https://github.com/) messaging CLI.

## How it works

`app.py`:

1. Prompts you for some message content on the command line.
2. Passes that prompt to an Ollama model (`ollama run <model> <prompt>`) and captures the generated reply.
3. Sends the generated reply to each phone number in the hardcoded `numbers` list via the `openclaw message send` command.

## Requirements

- Python 3
- [Ollama](https://ollama.com) installed and running, with the desired model pulled (e.g. `ollama pull llama3`)
- The `openclaw` CLI installed and configured with a WhatsApp account

## Configuration

Behavior is controlled through environment variables (with sensible defaults):

| Variable           | Default          | Description                              |
| ------------------ | ---------------- | ---------------------------------------- |
| `OLLAMA`           | `ollama`         | Path to the Ollama executable            |
| `OLLAMA_MODEL`     | `llama3:latest`  | Ollama model used to generate the reply  |
| `OPENCLAW`         | `openclaw`       | Path to the openclaw executable          |
| `CHANNEL`          | `whatsapp`       | Messaging channel                        |
| `WHATSAPP_ACCOUNT` | `default`        | openclaw account to send from            |

`config.json` holds additional reference settings (Ollama host/model and email/SMTP details).

## Usage

```bash
python app.py
```

You'll be prompted to enter message content; the generated reply is then sent to every recipient.

## Recipients

The target phone numbers are currently hardcoded in `app.py` in the `numbers` list. Edit that list to change who receives the message.

from pathlib import Path

import torch
from flask import Flask, request, render_template_string
from transformers import AutoTokenizer, AutoModelForCausalLM


# ------------------------------------------------------------
# PRIVATE FILES
# ------------------------------------------------------------
# These files are intentionally NOT included in the public repo.
#
# models/oracle/       = your trained model files
# voice_primer.txt     = your private poetic voice primer
#
# Both are excluded via .gitignore.

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "oracle"
VOICE_FILE = BASE_DIR / "voice_primer.txt"


# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

print("Loading The Oracle...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_DIR,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR,
    local_files_only=True
)

if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token

model.eval()

VOICE = VOICE_FILE.read_text(encoding="utf-8").strip()

print("The Oracle is ready.")


# ------------------------------------------------------------
# WEB APP
# ------------------------------------------------------------

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>The Oracle</title>

    <style>
        body {
            background: #0b0b0b;
            color: #f4f1ea;
            font-family: Georgia, serif;
            max-width: 760px;
            margin: 80px auto;
            padding: 0 24px;
        }

        h1 {
            font-weight: normal;
            font-size: 48px;
        }

        textarea {
            box-sizing: border-box;
            width: 100%;
            min-height: 110px;
            background: #151515;
            color: #f4f1ea;
            border: 1px solid #68645e;
            padding: 16px;
            font: 18px Georgia, serif;
        }

        button {
            margin-top: 14px;
            background: #f4f1ea;
            color: #111;
            border: none;
            padding: 12px 24px;
            cursor: pointer;
        }

        .oracle {
            margin-top: 45px;
            font-size: 22px;
            line-height: 1.7;
            white-space: pre-wrap;
        }
    </style>
</head>

<body>

<h1>The Oracle</h1>

<p>
A poetic language model built by fine-tuning GPT-2
on a private literary corpus.
</p>

<form method="post">
    <textarea
        name="prompt"
        placeholder="Write something..."
        required></textarea>

    <br>

    <button type="submit">Speak</button>
</form>

{% if response %}
<div class="oracle">
    {{ response }}
</div>
{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def oracle():

    response = ""

    if request.method == "POST":

        user_prompt = request.form.get("prompt", "").strip()

        if user_prompt:

            full_prompt = VOICE + "\n\n" + user_prompt

            inputs = tokenizer(
                full_prompt,
                return_tensors="pt"
            )

            with torch.no_grad():

                output = model.generate(
                    **inputs,
                    max_new_tokens=24,
                    do_sample=True,
                    temperature=0.70,
                    top_p=0.82,
                    top_k=35,
                    repetition_penalty=1.12,
                    pad_token_id=tokenizer.eos_token_id
                )

            new_tokens = output[
                0,
                inputs["input_ids"].shape[1]:
            ]

            response = tokenizer.decode(
                new_tokens,
                skip_special_tokens=True
            ).strip()

    return render_template_string(
        PAGE,
        response=response
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

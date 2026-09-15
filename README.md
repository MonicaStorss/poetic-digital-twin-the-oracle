# the-oracle 
A Poetic Digital Twin
# The Oracle

**The Oracle** is a poetic digital twin and co-writing language model created by fine-tuning GPT-2 on a private corpus of writing by Monica Storss.

The project explores what happens when a small language model is shaped by a single writer's corpus and used not as a general-purpose assistant, but as a constrained poetic interlocutor and collaborator. Self portrait in a convex mirror.

The Oracle is part of Digital Poetics, and an ongoing research and artistic practice concerning poetics, artificial intelligence, authorship, relationality, and experimental publishing.

## What This Repository Contains

This repository documents the software and methodology used to run The Oracle.

Included:

* Python application code
* model-loading and inference code
* generation settings
* interface code
* software dependencies
* documentation of the method

## What Is Not Included

The following materials are intentionally private and are **not distributed through this repository**:

* the original poetry corpus
* training texts
* the trained Oracle model weights
* `model.safetensors`
* the private poetic voice primer
* unpublished literary material

This repository shares the **method**, not the literary corpus or a distributable copy of The Oracle.

## Use and Permissions

This repository is publicly viewable for research, scholarly, artistic, and documentation purposes, but it is **not open source**.

Reuse, modification, redistribution, publication, incorporation into another project, or other use of the original code or materials requires **prior written permission from Monica-Lita Storss**.

Any authorized use must include appropriate attribution to Monica-Lita Storss and The Oracle.

The literary corpus, poetry, private voice primer, training materials, and trained Oracle model weights are not included in this repository and are not licensed for reuse.

## Model Architecture

The Oracle uses the GPT-2 small architecture.

The base GPT-2 model was fully fine-tuned on a private literary corpus. The resulting fine-tuned weights are retain

# The Oracle

**The Oracle** is a poetic digital twin and co-writing language model created by fine-tuning GPT-2 on a private corpus of writing by Monica-Lita Storss.

The project explores what happens when a small language model is shaped by a single writer's corpus and used not as a general-purpose assistant, but as a constrained poetic interlocutor.

The Oracle is part of an ongoing research and artistic practice concerning poetics, artificial intelligence, authorship, relationality, and experimental publishing.

## What This Repository Contains

This repository documents the software and methodology used to run The Oracle.

Included:

* Python application code
* model-loading and inference code
* generation settings
* interface code
* software dependencies
* documentation of the method

## What Is Not Included

The following materials are intentionally private and are **not distributed through this repository**:

* the original poetry corpus
* training texts
* the trained Oracle model weights
* `model.safetensors`
* the private poetic voice primer
* unpublished literary material

This repository shares the **method**, not the literary corpus or a distributable copy of The Oracle.

## Model Architecture

The Oracle uses the GPT-2 small architecture.

The base GPT-2 model was fully fine-tuned on a private literary corpus. The resulting fine-tuned weights are retained privately.

At inference time, a short private voice primer is combined with the participant's input before generation.

Current generation settings include:

```python
max_new_tokens=24
do_sample=True
temperature=0.70
top_p=0.82
top_k=35
repetition_penalty=1.12
```

These settings are intentionally conservative and favor short poetic continuations rather than long-form assistant responses.

## Reproducing the Method

Researchers, writers, and artists can adapt the public code in this repository to create their own small corpus-specific language model.

A typical workflow is:

1. Assemble a text corpus for which you have appropriate rights or permission.
2. Prepare the corpus as plain text.
3. Load a pretrained GPT-2 model and tokenizer.
4. Fine-tune the model on the corpus.
5. Save the resulting weights locally.
6. Create a private voice primer if desired.
7. Use the application code in this repository to load and interact with the resulting model.

The private files expected by `oracle_app.py` are:

```text
models/oracle/
voice_primer.txt
```

These paths are excluded from the public repository.

## Privacy and Literary Rights

The source corpus used to create The Oracle is not open data.

The absence of the corpus and trained weights from this repository is deliberate. Public access to the software should not be interpreted as permission to reproduce, scrape, train on, distribute, or republish the author's literary work.

The software and the underlying literary works should therefore be understood as separate artifacts with separate rights and permissions.

## Status

The Oracle is currently a research prototype.

The project is under active development, including work on:

* multi-turn poetic exchange
* public exhibition interfaces
* experimental publishing
* provenance and authorship
* responsible access to writer-specific models

## Credits

The Oracle was created by Monica-Lita Storss.

It uses the GPT-2 architecture originally developed by OpenAI and the Hugging Face Transformers library for model loading and inference.

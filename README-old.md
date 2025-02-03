# Dhwani - Indic Speech To Text Translation

Dhwani enables Speech-to-Text Translation for Indic Languages. It supports translation from Indic Language (X) → English and vice-versa.

## Supported Languages (X):
- Hindi
- Marathi
- Gujarati
- Bengali
- Tamil
- Telugu
- Malayalam
- Kannada

## Use-Cases:
- **Multilingual Communication** – Enables seamless conversations between people speaking different Indic languages.
- **Media & Entertainment** – Translates movies, TV shows, and podcasts for Indic audiences.
- **Education & E-learning** – Helps in translating lectures, training materials, and online courses.
- **Travel & Tourism** – Assists travelers with translation of speech.
- **Customer Support** – Enhances multilingual customer service through automated translations.
- **Healthcare** – Facilitates doctor-patient communication in different languages.
- **Business & Corporate** – Enables meetings and document translation for multinational teams.
- **Legal & Government** – Supports courtroom interpretation and official document translation.
- **News & Journalism** – Helps in broadcasting and reporting news in multiple languages.
- **Accessibility & Inclusion** – Assists the deaf, hard of hearing, and non-native speakers with translated audio.
- And many more…

## Technical Details

### Model Architecture:
#### **Dual Encoder Structure:**
- **Speech Encoder:** Utilizes the Whisper model's speech encoder to process speech inputs.
- **Audio Encoder:** Employs the BEATs audio encoder for non-speech audio inputs, such as environmental sounds and music.

#### **Connection Module:**
- **Window-Level Query Transformer (Q-Former):** Acts as a bridge between the audio encoders and the Large Language Model (LLM). It segments the variable-length outputs from the encoders into fixed-size windows, converting them into a set of textual tokens that the LLM can process.

#### **Large Language Model (LLM):**
- **Krutrim LLM:** A pre-trained text-based LLM that receives the processed tokens from the Q-Former, enabling it to handle and interpret audio-derived information.

#### **Adaptation Mechanism:**
- **Low-Rank Adaptation (LoRA):** Applied to the Krutrim LLM to fine-tune its parameters, ensuring effective alignment between the audio-derived inputs and the model's output space.

## Benchmarks

### En → Indic (X) BLEU Scores:
| Language Pair | BLEU Score |
|--------------|------------|
| en → hin | 57.7 |
| en → guj | 44.3 |
| en → mar | 43.3 |
| en → ben | 49.0 |
| en → tam | 47.0 |
| en → tel | 40.8 |
| en → mal | 39.0 |
| en → kan | 47.0 |
| **Average** | **46.0** |

### Indic (X) → En BLEU Scores:
| Language Pair | BLEU Score |
|--------------|------------|
| hin → en | 35.7 |
| guj → en | 34.6 |
| mar → en | 33.2 |
| ben → en | 19.2 |
| tam → en | 25.4 |
| tel → en | 17.4 |
| mal → en | 38.9 |
| kan → en | 28.0 |
| **Average** | **30.0** |

## How to Access and Run

### **Website Access:**
- Visit: [Dhwani Online](https://cloud.olakrutrim.com/console/languageLabs?section=speech)
- **Step 1:** Record Audio to be translated.
- **Step 2:** Select source language and target language from the drop-down.
- **Step 3:** Press **“Submit Speech”**.

### **Run the Model Locally:**
To run the model locally, check out the following GitHub repository:
- [Dhwani GitHub Repo](https://github.com/ola-silicon/Dhwani)

## How to inference in CLI

1. Our environment: The python version is 3.9.17, and other required packages can be installed with the following command: ```pip install -r requirements.txt```.
2. Download [whisper large v2](https://huggingface.co/openai/whisper-large-v2/tree/main) to ```whisper_path```.
3. Download [Fine-tuned BEATs_iter3+ (AS2M) (cpt2)](https://1drv.ms/u/s!AqeByhGUtINrgcpj8ujXH1YUtxooEg?e=E9Ncea) to `beats_path`.
4. Download krutrim llm to ```llama_path```.
5. add krutrim ckpt path to ```ckpt```.
6. Running with ```python3 cli_inference.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. Now you can input ```wav_path``` and ```prompt```. Enjoy yourself !

## How to infer the model

1. Same as **How to inference in CLI: 1-4**.
2. add krutrim ckpt path to ```ckpt```.
3. Running with ```python3 infer.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. 

---
Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request on GitHub.

# Dhwani - Indic Speech To Text Translation

## 1. Introduction
Dhwani enables Speech-to-Text Translation for Indic Languages. It supports translation from Indic Language (X) → English and vice-versa.

## 2. Model Summary

Current model trained using [SALMONN](https://openreview.net/pdf?id=14rn7HpKVk) architecture.

### PreTraining
- **Speech Encoder:** Utilizes the Whisper model's speech encoder to process speech inputs.
- **Audio Encoder:** Employs the BEATs audio encoder for non-speech audio inputs, such as environmental sounds and music.
- **Connection Module:** Uses the Window-Level Query Transformer (Q-Former) to bridge the audio encoders and the Large Language Model (LLM).
- **Large Language Model (LLM):** The Krutrim LLM receives the processed tokens, handling audio-derived information.
- **Adaptation Mechanism:** Low-Rank Adaptation (LoRA) is applied to fine-tune the LLM to align the audio inputs with the model's output.


### PostTraining

## 3. Model Downloads
To run the model locally, visit the [Dhwani Hugging Face Repo](https://huggingface.co/krutrim-ai-labs/Dhwani/blob/main/checkpoint_best.pth).

## 4. Evaluation Results

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

## 5. API Platform
Visit [Dhwani Online](https://cloud.olakrutrim.com/console/languageLabs?section=speech) to access the model via the web interface. 

### How to inference in CLI

1. Our environment: The python version is 3.9.17, and other required packages can be installed with the following command: ```pip install -r requirements.txt```.
2. Download [whisper large v2](https://huggingface.co/openai/whisper-large-v2/tree/main) to ```whisper_path```.
3. Download [Fine-tuned BEATs_iter3+ (AS2M) (cpt2)](https://1drv.ms/u/s!AqeByhGUtINrgcpj8ujXH1YUtxooEg?e=E9Ncea) to `beats_path`.
4. Download [krutrim llm](https://huggingface.co/krutrim-ai-labs/Dhwani/blob/main/checkpoint_best.pth) to ```llama_path```.
5. add krutrim ckpt path to ```ckpt```.
6. Running with ```python3 cli_inference.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. Now you can input ```wav_path``` and ```prompt```. Enjoy yourself !

### How to infer the model

1. Same as **How to inference in CLI: 1-4**.
2. add krutrim ckpt path to ```ckpt```.
3. Running with ```python3 infer.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. 



## 6. License

## 7. Citation

@inproceedings{
  sanket2025IndicST,
  title={{IndicST}: Indian Multilingual Translation Corpus For Evaluating Speech Large Language Models},
  author={Sanket Shah, Kavya Ranjan Saxena, Kancharana Manideep Bharadwaj, Sharath Adavanne, Nagaraj Adiga},
  booktitle={Proc. Satellite Workshop SALMA: Speech and Audio Language Models - Architectures, Data Sources, and Training Paradigms, ICASSP},
  year={2025},
}

@inproceedings{
  tang2024salmonn,
  title={{SALMONN}: Towards Generic Hearing Abilities for Large Language Models},
  author={Changli Tang and Wenyi Yu and Guangzhi Sun and Xianzhao Chen and Tian Tan and Wei Li and Lu Lu and Zejun MA and Chao Zhang},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024},
  url={https://openreview.net/forum?id=14rn7HpKVk}
}
## 8. Contact
Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request on GitHub.

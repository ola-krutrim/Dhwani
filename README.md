---
viewer: false
---

# Dhwani - Indic Speech To Text Translation
[![Static Badge](https://img.shields.io/badge/Huggingface-Dhwani-yellow?logo=huggingface)](https://huggingface.co/krutrim-ai-labs/Dhwani)	[![Static Badge](https://img.shields.io/badge/Github-Dhwani-green?logo=github)](https://github.com/ola-krutrim/Dhwani)	[![Static Badge](https://img.shields.io/badge/Krutrim_Cloud-Dhwani-orange?logo=data:image/png%2bxml;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADpUlEQVRYCbVXTUhbQRDeRJqi2JSS1BQtgpCa0kiPehdNi6dWbfWgF0s9eGtPFSFG8VDMpSiCB28KQou0NwsS9NA/Dx4qNP1TUIqSmlKSFjQx4vabbXbJz8vLe2kz8GX3zc7MN2/2J/sszLichekN4A7gBZxpcLQ/0gijfQq8BFLAf5ELiBIEfgNEZgSxtA/5liw2eD4EfgJGSLVsyPcBQLFMiR3WIUAraCm6F4hFMQ2JB1afgFKI9Hw+IubVYhnQwvpSBnKZ2GfEvlgoiTMYeFNGcpnEK3AQV548gkYalbslLiGWdEtl2QbOpZ9FMzg4yGprazNVpvrr6+tseXlZy+cXlFeAAzk4i07eW29sbPB/kampqbyYGTzEyagC5wHKJG+v6lWgqamJdXV1wY2xhYUFtr1NBcwWnQqQYRJwUQK3gOeArjidTkakJMfHx6y+vp4tLi6KZ5/Px1ZWVkTf5M9tstcsP/SifFarlQcCAX50dKRm4/T0lPf19ann9vZ2Xl1dzZubm3lVVZVe2XPHxDS8k2Ra7fj4uCKSnUgkwnt7e+Uj393d5ZQUSSqV4sFgMJeo0DNxsx0tYtLR2x8eHorA4XCY19TUqECZCZAB1gDf398XtvTT0dGhbAvFh37Hip9LgKbYbDZWWVkpxtbW1tjBgdo1rKGhQegTiQQbHR1lbreb9fT0qDgtLS2qr9MR3AkYFMyW3pwkGo3yzs5OPjAwwFdXV4WOfra2tpSv3W5X+snJSaXXiU/chaeAHLu7u1VQrQ6VXhJgWyqT/v5+pZfjGu0OdEx3EZJTW1sbX1pa4pgGgZmZGT40NCTIMisgDy5MC3c4HEYSEItwlkjMQi7Cvb095etyufjc3ByfmJhQuiJxiVscREYdlN3w8DA/OTnhsVhM6YqQadndpAToKNZdiLmBvV4vTyaTYgo2Nze5xWLRCl5MR0exOv5NTcPY2Jiaf2zTYkSFxkX56RwgCQBUBUNSUVEh7OicoP3e2trKpqenGf1fGBTi8ufaPoGiULZZ+sbGRh6Px9WWk52RkZEsO514j3PJ6Zlure8BQ0E8Hg+fn58X2zIUCnG/38/r6uqM+L4Fx9/jFZ1cuQzFN8BIoFJsviJ20Xm6DqN4GZKIIqYbMCQOWL0GSnlLLR+6rVBMU0I75B4QAbSCGtF9h+99QO42dM0L3ZRp1Zr9OCWfrFu2FrW8lmuN5erOQuED7gLXAPl5TjHk5/kH9J8BdBc39Hn+BxqB1clokCTRAAAAAElFTkSuQmCC)](https://cloud.olakrutrim.com/console/inference-service?section=models&modelName=Krutrim&artifactName=Krutrim-Dhwani&artifactType=model)	[![Static Badge](https://img.shields.io/badge/Krutrim_AI_Labs-Dhwani-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzYiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCAzNiAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjM2IiBoZWlnaHQ9IjM2IiByeD0iMTgiIGZpbGw9IiMxMEE1NTQiLz4KPHBhdGggZD0iTTI2LjQxNCAxMi41OTE5SDE5LjMzVjE1LjY0OTlDMjAuMDM0IDE1LjIzOTIgMjAuODQwNyAxNS4wMzM5IDIxLjc1IDE1LjAzMzlDMjIuNzkxMyAxNS4wMzM5IDIzLjY0MiAxNS4zNTY1IDI0LjMwMiAxNi4wMDE5QzI0Ljk3NjcgMTYuNjQ3MiAyNS4zMTQgMTcuNTQxOSAyNS4zMTQgMTguNjg1OUMyNS4zMTQgMTkuMzMxMiAyNS4xODkzIDIwLjA0OTkgMjQuOTQgMjAuODQxOUMyNC43MDUzIDIxLjYzMzkgMjQuMzE2NyAyMi40NDA1IDIzLjc3NCAyMy4yNjE5TDIxLjIgMjEuODMxOUMyMS41MzczIDIxLjM3NzIgMjEuODE2IDIwLjkwNzkgMjIuMDM2IDIwLjQyMzlDMjIuMjU2IDE5LjkzOTkgMjIuMzY2IDE5LjQ0MTIgMjIuMzY2IDE4LjkyNzlDMjIuMzY2IDE4LjM4NTIgMjIuMjQ4NyAxOC4wMDM5IDIyLjAxNCAxNy43ODM5QzIxLjc5NCAxNy41NjM5IDIxLjUwMDcgMTcuNDUzOSAyMS4xMzQgMTcuNDUzOUMyMC43OTY3IDE3LjQ1MzkgMjAuMTQ0IDE3Ljc2MTkgMjAuMTQ0IDE3Ljc2MTlDMjAuMTQ0IDE3Ljc2MTkgMTkuMTE0NyAxOC4xODcyIDE4Ljg4IDE4LjQyMTlWMjMuODU1OUgxNi4zODJWMjEuMDYxOUMxNS44OTggMjEuMzQwNSAxNS40MDY3IDIxLjU1MzIgMTQuOTA4IDIxLjY5OTlDMTQuNDI0IDIxLjg0NjUgMTMuODU5MyAyMS45MTk5IDEzLjIxNCAyMS45MTk5QzEyLjQwNzMgMjEuOTE5OSAxMS42NjY3IDIxLjc3MzIgMTAuOTkyIDIxLjQ3OTlDMTAuMzMyIDIxLjE3MTkgOS44MDQgMjAuNzI0NSA5LjQwOCAyMC4xMzc5QzkuMDEyIDE5LjU1MTIgOC44MTQgMTguODE3OSA4LjgxNCAxNy45Mzc5QzguODE0IDE3LjExNjUgOS4wMTIgMTYuNDEyNSA5LjQwOCAxNS44MjU5QzkuODA0IDE1LjIyNDUgMTAuMzU0IDE0Ljc2MjUgMTEuMDU4IDE0LjQzOTlDMTEuNzYyIDE0LjEwMjUgMTIuNTc2IDEzLjkzMzkgMTMuNSAxMy45MzM5QzEzLjkxMDcgMTMuOTMzOSAxNC4zMjEzIDEzLjk0ODUgMTQuNzMyIDEzLjk3NzlDMTUuMTU3MyAxNC4wMDcyIDE1LjQ4NzMgMTQuMDU4NSAxNS43MjIgMTQuMTMxOUwxNS41MDIgMTYuNTczOUMxNS4wMzI3IDE2LjQ1NjUgMTQuNTEyIDE2LjM5NzkgMTMuOTQgMTYuMzk3OUMxMy4yNTA3IDE2LjM5NzkgMTIuNzE1MyAxNi41MzcyIDEyLjMzNCAxNi44MTU5QzExLjk1MjcgMTcuMDc5OSAxMS43NjIgMTcuNDUzOSAxMS43NjIgMTcuOTM3OUMxMS43NjIgMTguNTI0NSAxMS45NDUzIDE4LjkyNzkgMTIuMzEyIDE5LjE0NzlDMTIuNjc4NyAxOS4zNjc5IDEzLjA3NDcgMTkuNDc3OSAxMy41IDE5LjQ3NzlDMTQuMTE2IDE5LjQ3NzkgMTQuNjU4NyAxOS4zMzg1IDE1LjEyOCAxOS4wNTk5QzE1LjYxMiAxOC43ODEyIDE2LjAzIDE4LjQ1ODUgMTYuMzgyIDE4LjA5MTlWMTIuNTkxOUg4VjEwLjE3MTlIMjYuNDE0VjEyLjU5MTlaIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNMjIuMDc0IDI4Ljk4MTlDMjEuNjkyNyAyOS4xNzI1IDIxLjIzOCAyOS4zNDg1IDIwLjcxIDI5LjUwOTlDMjAuMTY3MyAyOS42NzEyIDE5LjUyMiAyOS43NTE5IDE4Ljc3NCAyOS43NTE5QzE4LjA0MDcgMjkuNzUxOSAxNy4zODggMjkuNjEyNSAxNi44MTYgMjkuMzMzOUMxNi4yNDQgMjkuMDY5OSAxNS43OTY3IDI4LjY5NTkgMTUuNDc0IDI4LjIxMTlDMTUuMTM2NyAyNy43NDI1IDE0Ljk2OCAyNy4xOTI1IDE0Ljk2OCAyNi41NjE5QzE0Ljk2OCAyNS41MDU5IDE1LjM0MiAyNC42NjI1IDE2LjA5IDI0LjAzMTlDMTYuODIzMyAyMy40MTU5IDE3LjQyOTMgMjMuMDYzOSAxOC44MDggMjIuOTc1OUwxOS4wNzIgMjUuMjQxOUMxOC4zMjQgMjUuMjg1OSAxOC4yNjA3IDI1LjQyNTIgMTcuOTgyIDI1LjY1OTlDMTcuNzAzMyAyNS45MDkyIDE3LjU2NCAyNi4xOTUyIDE3LjU2NCAyNi41MTc5QzE3LjU2NCAyNy4xOTI1IDE4LjAxMTMgMjcuNTI5OSAxOC45MDYgMjcuNTI5OUMxOS4yNDMzIDI3LjUyOTkgMTkuNTg4IDI3LjQ3ODUgMTkuOTQgMjcuMzc1OUMyMC4yOTIgMjcuMjczMiAyMC43MTczIDI3LjA5NzIgMjEuMjE2IDI2Ljg0NzlMMjIuMDc0IDI4Ljk4MTlaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K)](https://ai-labs.olakrutrim.com/models/Dhwani-1)

## Introduction
Dhwani enables Speech-to-Text Translation for Indic Languages. It supports translation from Indic Language (X) → English and vice-versa.

[![Dhwani](https://img.youtube.com/vi/T3qA4pmTDb4/0.jpg)](https://www.youtube.com/watch?v=T3qA4pmTDb4)

## Model Summary

Current model trained using [SALMONN](https://openreview.net/pdf?id=14rn7HpKVk) architecture.

### PreTraining
- **Speech Encoder:** Utilizes the Whisper model's speech encoder to process speech inputs.
- **Audio Encoder:** Employs the BEATs audio encoder for non-speech audio inputs, such as environmental sounds and music.
- **Connection Module:** Uses the Window-Level Query Transformer (Q-Former) to bridge the audio encoders and the Large Language Model (LLM).
- **Large Language Model (LLM):** The Krutrim LLM receives the processed tokens, handling audio-derived information.
- **Adaptation Mechanism:** Low-Rank Adaptation (LoRA) is applied to fine-tune the LLM to align the audio inputs with the model's output.


### PostTraining
To adapt Q-former and LoRA weights, we used techniques mentioned in the paper [IndicST](https://huggingface.co/datasets/krutrim-ai-labs/IndicST). Along with the IndicST translation dataset, we also used in-house-collected translation data to further improve the performance of translation results.

## Model Downloads

1. Download [whisper large v2](https://huggingface.co/openai/whisper-large-v2/tree/main).
2. Download [Fine-tuned BEATs_iter3+ (AS2M) (cpt2)](https://1drv.ms/u/s!AqeByhGUtINrgcpj8ujXH1YUtxooEg?e=E9Ncea).
3. Download [krutrim llm](https://huggingface.co/krutrim-ai-labs/Krutrim-1-base).
4. Download [ckpt](https://huggingface.co/datasets/krutrim-ai-labs/Dhwani/blob/main/ckpt/checkpoint_best.pth).

## Evaluation Results

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

## API Platform
Visit [Dhwani Online](https://cloud.olakrutrim.com/console/languageLabs?section=speech) to access the model via the web interface. 

### How to inference in CLI

1. conda create -n dhwani_env python=3.9.17
2. Our environment: The python version is 3.9.17, and other required packages can be installed with the following command: ```pip install -r requirements.txt```.
3. add [whisper large v2](https://huggingface.co/openai/whisper-large-v2/tree/main) to ```whisper_path```.
4. add [Fine-tuned BEATs_iter3+ (AS2M) (cpt2)](https://1drv.ms/u/s!AqeByhGUtINrgcpj8ujXH1YUtxooEg?e=E9Ncea) to `beats_path`.
5. add [krutrim llm](https://huggingface.co/krutrim-ai-labs/Dhwani/blob/main/checkpoint_best.pth) to ```llama_path```.
6. add krutrim ckpt path to ```ckpt```.
7. Running with ```python3 cli_inference.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. Now you can input ```wav_path``` and ```prompt```. Enjoy yourself !

### How to infer the model

1. Same as **How to inference in CLI: 1-4**.
2. add krutrim ckpt path to ```ckpt```.
3. Running with ```python3 infer.py --cfg-path configs/decode_config.yaml``` in A100-SXM-80GB. 



## License
This code repository and the model weights are licensed under the [Krutrim Community License.](LICENSE.md)

## Citation
```
@inproceedings{
  sanket2025IndicST,
  title={{IndicST}: Indian Multilingual Translation Corpus For Evaluating Speech Large Language Models},
  author={Sanket Shah, Kavya Ranjan Saxena, Kancharana Manideep Bharadwaj, Sharath Adavanne, Nagaraj Adiga},
  booktitle={Proc. ICASSP},
  year={2025},
}
```

## Contact
Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request on GitHub.

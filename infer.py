# Copyright (2024) Tsinghua University, Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

import torch
from transformers import WhisperFeatureExtractor

from config import Config
from models.dhwani import DHWANI
from utils import prepare_one_sample

PROMPTS = {
    "s2tt_en_hindi": "Translate to Hindi",
}


parser = argparse.ArgumentParser()
parser.add_argument("--cfg-path", type=str, required=True, help='path to configuration file')
parser.add_argument("--device", type=str, default="cuda:0")
parser.add_argument(
    "--options",
    nargs="+",
    help="override some settings in the used config, the key-value pair "
    "in xxx=yyy format will be merged into config file (deprecate), "
    "change to --cfg-options instead.",
)

args = parser.parse_args()
cfg = Config(args)

model = DHWANI.from_config(cfg.config.model)
model.to(args.device)
model.eval()

wav_processor = WhisperFeatureExtractor.from_pretrained(cfg.config.model.whisper_path)

def run_dhwani(wav_path, task, target_language = "english"):
    try:
        
        samples = prepare_one_sample(wav_path, wav_processor)
        if task == "s2tt":
            prompt = PROMPTS[task] + target_language
        else:
            prompt = PROMPTS[task]
        prompt = [
            cfg.config.model.prompt_template.format("<Speech><SpeechHere></Speech> " + prompt.strip())
        ]
        
        with torch.cuda.amp.autocast(dtype=torch.float16):
            output = model.generate(samples, cfg.config.generate, prompts=prompt)[0]
            print(output)
            return output
    except Exception as e:
        print(e)


run_dhwani("examples/audio_demo/mountain.wav", "s2tt_en_hindi")
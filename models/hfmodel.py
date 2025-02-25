from huggingface_hub import hf_hub_download
import torch

class HFMODEL:
    def __init__(self):
        pass
    def load_hf_model(self, repo_id, filename):        
        # Download the checkpoint file
        ckpt_path = hf_hub_download(repo_id=repo_id, filename=filename)

        # Load the model checkpoint
        ckpt = torch.load(ckpt_path, map_location="cpu")

        return ckpt

from huggingface_hub import snapshot_download

snapshot_download(repo_id="bert-base-uncased", allow_patterns=["*.*"], local_dir="./my_model2/")
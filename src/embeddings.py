from sentence_transformers import SentenceTransformer

def load_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2",
        cache_folder="hf_cache"
    )

def get_embeddings(model, chunks):
    return model.encode(chunks, show_progress_bar=True)
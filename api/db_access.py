import os
from supabase import create_client, Client
import json

url: str = os.environ.get("DATABASE_URL")
key: str = os.environ.get("PUBLIC_SUPABASE_ANON_KEY")

def find_embeddings():
    supabase: Client = create_client(url, key)
    data = supabase.table("Documents").select("embedding").execute()
    list_data = json.loads(data.data[0]['embedding'])
    return list_data


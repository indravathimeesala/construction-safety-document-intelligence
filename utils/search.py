from utils.database import search_documents

def search_keyword(keyword):
    results = search_documents(keyword)
    return results
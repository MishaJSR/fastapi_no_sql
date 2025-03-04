import json
import logging
import os

from elasticsearch import Elasticsearch
from fastapi import HTTPException, APIRouter

router = APIRouter(
    prefix="/els",
    tags=["Elsstic"]
)

es = Elasticsearch("http://172.18.0.3:9200", verify_elasticsearch=False)

@router.post("/add_document/")
async def add_document(index_name: str, doc_id: int, name: str, description: str):
    document = {
        "name": name,
        "description": description
    }
    res = es.index(index=index_name, id=doc_id, body=document)
    return {"status": "Document added", "id": res["_id"]}

@router.post("/add_all_document/")
async def add_document(doc_id: int, name: str, description: str):
    with open('ex.json', 'r', encoding='utf-8') as file:
        data = json.load(file)["articles"]
    for item in data:
        _ = es.index(index="article", id=doc_id, body=item)
        doc_id += 1
    return {"status": "Document added"}

@router.get("/get_document/{doc_id}")
async def get_document(index_name: str, doc_id: int):
    res = es.get(index=index_name, id=doc_id)
    if not res["found"]:
        raise HTTPException(status_code=404, detail="Document not found")
    return res["_source"]

@router.get("/search/")
async def search(index_name: str, query: str):
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["content", "description"],
                "type": "best_fields",
                "fuzziness": "AUTO"
            }
        }
    }
    res = es.search(index=index_name, body=body)
    return [hit["_source"] for hit in res["hits"]["hits"]]
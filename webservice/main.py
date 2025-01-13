from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import crud

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/documents/", response_model=list[dict])
async def get_all_documents_endpoint():
    documents = await crud.get_all_documents()
    return documents


@app.post("/documents/", response_model=dict)
async def create_document_endpoint(document: dict):
    new_document = await crud.create_document(document)
    return new_document


@app.get("/documents/{id}", response_model=dict)
async def get_document_endpoint(id: str):
    document = await crud.get_document(id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@app.put("/documents/{id}", response_model=dict)
async def update_document_endpoint(id: str, document: dict):
    updated_document = await crud.update_document(id, document)
    if updated_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return updated_document


@app.delete("/documents/{id}")
async def delete_document_endpoint(id: str):
    await crud.delete_document(id)
    return {"message": "Document deleted successfully"}

from bson import ObjectId
from database import document_collection


async def get_all_documents() -> list[dict]:
    documents = []
    async for document in document_collection.find():
        document["_id"] = str(document["_id"])  # Pastikan _id adalah string
        # Tambahkan pemeriksaan jika ada field yang hilang
        if "Country Name" not in document:
            document["Country Name"] = "Unknown"
        if "Country ISO3" not in document:
            document["Country ISO3"] = "Unknown"
        if "Year" not in document:
            document["Year"] = 0
        if "data" not in document:
            document["data"] = {}  # Sesuaikan jika data kosong
        documents.append(document)
    return documents


async def get_document(id: str) -> dict:
    document = await document_collection.find_one({"_id": ObjectId(id)})
    if document:
        document["_id"] = str(document["_id"])  # Pastikan _id adalah string
        # Tambahkan pemeriksaan jika ada field yang hilang
        if "Country Name" not in document:
            document["Country Name"] = "Unknown"
        if "Country ISO3" not in document:
            document["Country ISO3"] = "Unknown"
        if "Year" not in document:
            document["Year"] = 0
        if "data" not in document:
            document["data"] = {}  # Sesuaikan jika data kosong
        return document
    return None


async def create_document(document: dict) -> dict:
    result = await document_collection.insert_one(document)
    document["_id"] = str(result.inserted_id)
    return document


async def update_document(id: str, document: dict) -> dict:
    # Remove the '_id' field from the document to avoid modifying it
    document.pop("_id", None)
    result = await document_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": document}
    )
    if result.matched_count:
        document["_id"] = id
        return document
    return None


async def delete_document(id: str):
    await document_collection.delete_one({"_id": ObjectId(id)})

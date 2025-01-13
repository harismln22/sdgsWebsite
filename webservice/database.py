from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb+srv://db:123@cluster0.vuwlz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.sdgs

document_collection = database.get_collection("transform_climate_change_idn")

address_collection = database.get_collection("addresses")
# Tambahkan koleksi lain sesuai kebutuhan

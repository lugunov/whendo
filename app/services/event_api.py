import httpx

BASE_URL = "http://localhost:8000"

async def get_similar_events(user_id: int, query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/events", params={"user_id": user_id, "q": query})
        return response.json() if response.status_code == 200 else []

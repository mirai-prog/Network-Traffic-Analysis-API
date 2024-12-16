from fastapi import APIRouter

router = APIRouter()

@router.post("/upload", summary="Тестовый эндпоинт")
def test_upload():
    return {"message": "Upload is working!"}


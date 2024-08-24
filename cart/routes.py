from fastapi import APIRouter
from accounts import User

router = APIRouter(
    tags=['carts'],
    prefix='/carts'
)


@router.get('/list')
async def carts(user: User = Depends()):
    pass
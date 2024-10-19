from fastapi import FastAPI, APIRouter, Depends

from services.api_gateway.routers import user_router, role_router, user_role_router, \
    quest_router, dependency_router, category_router, \
    board_router, column_router,\
    adventure_router,\
    party_router
from services.common.utils.api import check_api_key

app = FastAPI()

router = APIRouter(prefix="/task-manager")
router.include_router(user_router, dependencies=[Depends(check_api_key)])
router.include_router(role_router, dependencies=[Depends(check_api_key)])
router.include_router(user_role_router, dependencies=[Depends(check_api_key)])
router.include_router(quest_router, dependencies=[Depends(check_api_key)])
router.include_router(dependency_router, dependencies=[Depends(check_api_key)])
router.include_router(category_router, dependencies=[Depends(check_api_key)])
router.include_router(board_router, dependencies=[Depends(check_api_key)])
router.include_router(column_router, dependencies=[Depends(check_api_key)])
router.include_router(adventure_router, dependencies=[Depends(check_api_key)])
router.include_router(party_router, dependencies=[Depends(check_api_key)])

app.include_router(router)

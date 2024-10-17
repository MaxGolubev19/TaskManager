from fastapi import FastAPI, APIRouter

from services.api_gateway.routers import user_router, role_router, user_role_router, \
    quest_router, dependency_router, category_router, \
    board_router, column_router,\
    adventure_router,\
    party_router

app = FastAPI()

router = APIRouter(prefix="/task-manager")
router.include_router(user_router)
router.include_router(role_router)
router.include_router(user_role_router)
router.include_router(quest_router)
router.include_router(dependency_router)
router.include_router(category_router)
router.include_router(board_router)
router.include_router(column_router)
router.include_router(adventure_router)
router.include_router(party_router)

app.include_router(router)

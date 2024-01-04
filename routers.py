from fastapi import APIRouter
from view.github_oauth.githubloginRouter import github_login_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(github_login_router, prefix="/github_login")

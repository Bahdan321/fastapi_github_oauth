import httpx

from fastapi import APIRouter
from starlette.responses import RedirectResponse


github_login_router = APIRouter()
github_client_id = "10d7d500704eeee6ee39"
github_client_secret = "ea7178d0785dc818090e3b4d5404e0021111e8ab"


@github_login_router.get("/github-login")
async def github_login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={github_client_id}", status_code=302)

@github_login_router.get("/github-code")
async def github_code(code: str):
    params = {
        "client_id": github_client_id,
        "client_secret": github_client_secret,
        "code": code
    }

    headers = {"Accept": "application/json"}

    async with httpx.AsyncCLient() as client:
        response = await client.post(url="https://github.com/login/oauth/", params=params, headers=headers)
        response_json = response.json()
        print(response_json)
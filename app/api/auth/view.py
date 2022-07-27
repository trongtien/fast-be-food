from fastapi import APIRouter
from app.api.auth.schema import SchemaLoginRequest

router = APIRouter()

@router.post(
    path="/admin",
    name="Employee login"
)
async def login_admin(login_request: SchemaLoginRequest):
    return {
        "id": 1,
        "name": "admin",
        "avartar": "https://gravatar.com/avatar/bfc048fe6df7d1b3ab23762ff20e11eb?s=400&d=retro&r=x",
        "role": "owner",
        "token": "jhmgIDvk4kyj62iGgmYYnQ==",
        "menu": [
            { "id": "1", "name": 'Dashboard', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "2", "name": 'products', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [
                    { "id": "2.1", "name": 'Products=Analytics', "icon": "UserOutlined", "path": "/products-analytics", "code": "products-analytics", "subMenu": [] },
                    { "id": "2.2", "name": 'Products=Schedule', "icon": "AppstoreOutlined", "path": "/products-schedule", "code": "products-schedule", "subMenu": [] }
                ] 
            },
            { "id": "3", "name": 'analytics', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "4", "name": 'schedule', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] }
        ]
    }


@router.post(
    path="/admin-acess-token",
    name="Employee login"
)
async def login_acccess_token(access_token: str):
    return {
        "id": 1,
        "name": "admin",
        "avartar": "https://gravatar.com/avatar/bfc048fe6df7d1b3ab23762ff20e11eb?s=400&d=retro&r=x",
        "role": "owner",
        "token": "jhmgIDvk4kyj62iGgmYYnQ==",
        "menu": [
            { "id": "1", "name": 'Dashboard', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "2", "name": 'products', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [
                    { "id": "2.1", "name": 'Products=Analytics', "icon": "UserOutlined", "path": "/products-analytics", "code": "products-analytics", "subMenu": [] },
                    { "id": "2.2", "name": 'Products=Schedule', "icon": "AppstoreOutlined", "path": "/products-schedule", "code": "products-schedule", "subMenu": [] }
                ] 
            },
            { "id": "3", "name": 'analytics', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] },
            { "id": "4", "name": 'schedule', "icon": "DesktopOutlined", "path": "/", "code": "dashboard", "subMenu": [] }
        ]
    }
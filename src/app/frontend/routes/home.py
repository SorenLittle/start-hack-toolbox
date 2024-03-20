import fastapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = fastapi.APIRouter()
templates = Jinja2Templates(directory="src/app/frontend/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: fastapi.Request) -> fastapi.Response:

    context = {"request": request}

    return templates.TemplateResponse("home.html", context)

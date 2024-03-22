import fastapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# from src.app.example_data import allocation
from src.opt.crop_optimization import allocation


router = fastapi.APIRouter()
templates = Jinja2Templates(directory="src/app/frontend/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: fastapi.Request) -> fastapi.Response:

    context = {"request": request, "allocation": allocation}

    return templates.TemplateResponse("home.html", context)

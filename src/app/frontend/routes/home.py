import fastapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from src.app.example_data import allocation
from src.opt.models import AgricultureData
from src.opt.models import Crop
from src.opt import croptimization

# from src.app.example_data import allocation
from src.opt.crop_optimization import allocation


router = fastapi.APIRouter()
templates = Jinja2Templates(directory="src/app/frontend/templates")

class OptRequestModel(BaseModel):
    number_of_fields: Optional[int] =5
    number_of_seasons: Optional[int]= 10
    crops: list[Crop]
    initial_nutrients: Optional[int] =10
    min_nutrients: Optional[int] = 3   
    max_nutrients: Optional[int] = 20




@router.post("/opt", response_model =AgricultureData)  # Changed to POST
async def opt(opt_request: OptRequestModel):  # Using Request for template rendering
    agriculture_data = croptimization(opt_request.number_of_fields, opt_request.number_of_seasons, opt_request.crops, opt_request.initial_nutrients, opt_request.min_nutrients, opt_request.max_nutrients)


    return agriculture_data
@router.get("/", response_class=HTMLResponse)
async def home(request: fastapi.Request) -> fastapi.Response:

    context = {"request": request, "allocation": allocation}

    return templates.TemplateResponse("home.html", context)
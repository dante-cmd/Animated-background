from fastapi import FastAPI, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from read_img import get_rgb


app = FastAPI()

# templates
templates = Jinja2Templates(directory="templates")

# index, include css and js

@app.get("/", response_class=HTMLResponse)
async def index(request:Request):
    # 1. make the root in the sever
    # 2. where is the root
    # 3. the name for the html file
    app.mount("/static", StaticFiles(directory="static"), name="static1")

    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

# websocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        url_img = await websocket.receive_text()
        # to_Export = "rgb({}, {}, {})".format(*get_rgb(url_img))
        color_middle, color_max = get_rgb(url_img)
        # print(get_rgb(url_img))
        toExportMiddle = "#{0:02x}{1:02x}{2:02x}".format(*color_middle)
        toExportMax = "#{0:02x}{1:02x}{2:02x}".format(*color_max)
        
        # print(f"Received: {url_img}")
        # 
        await websocket.send_text(toExportMax + " ," + toExportMiddle)
    

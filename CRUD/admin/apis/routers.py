from distutils import extension
from distutils.log import error
from fastapi import APIRouter,Depends, UploadFile, File,status
from datetime import datetime
from pydantic import FilePath
from .models import *
from admin.apis.pydantic_models import Addsong, AdminUser
import os

router=APIRouter()

@router.post("/admin/")
async def create_user(data:AdminUser):
    adduser= await AddUser.create(fname=data.fname, mobile=data.mobile, email=data.email, password=data.password)
    return{"status": True, "message": "ok"}


# @router.post("/song/")
# async def create_songs(data:Addsong=Depends()):
#     # try:
#         if await Song.exists(song_name=data.song_name):
#             return{"status":False, "message": "This song is already Exists"}
#         # else:
#         #    FILEPATH = "static/song/"
#         # #    if not os.path.isdir(FILEPATH):
#         # #         os.mkdir(FILEPATH)
#         # filename = song.filename
#         # extension = filename.split(".")[1]
#         # songname = filename.split(".")[0]
#         # if extension not in ["MP3","mp3", "mp4"]:
#         #     return{"status": "error", "detial": "File extension not allowed"}
#         # dt = datetime.now()
#         # dt_timestamp = round(datetime.timestamp(dt))

#         # modified_image_name = songname+"_"+str(dt_timestamp)+"."+extension
#         # genrated_name = FILEPATH + modified_image_name
#         # file_content = await song.read()
#         # with open(genrated_name, "wb") as file:
#         #     file.write(file_content)
#         #     file.close()

#         song_obj = await Song.create(
#                 #song=genrated_name,
#                 song_name= data.song_name
#             )
        # if song_obj:
#             return {"status": True, "message":"Song Added"}
#         else:
#             return{"status": False, "message": "Somthing Wrong"}
#     # except Exception as ex:
#         # return{str(ex)}


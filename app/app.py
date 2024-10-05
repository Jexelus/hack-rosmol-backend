from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from database.database import pdProject, pdUser
from database.User.methods import create_user, get_user_by_vk_id, update_last_project_id
from database.Project.methods import new_Project, get_Project_by_id, delete_Project, get_Projects_by_author_id_with_pagination, update_Project, get_Projects_with_pagination
import orjson

app = FastAPI()


@app.get("/")
async def root():
    return ORJSONResponse({"message": "Hello World"}, status_code=200)

@app.post("/user/create/", response_model=pdUser, responses={
    409: {
        "description": "User already exists", "content": {
        "application/json": {
            "example": {
                "message": "User already exists"
                }
            }
        }
    },
    200:{
        "description": "User created",
        "content": {
            "application/json": {
                "example": {
                    "vk_id": 1,
                    "last_project_id": 1
                }
            } 
        }
    }
})
async def cr_user(request: Request):
    data = await request.body()
    data = orjson.loads(data)
    if get_user_by_vk_id(data['vk_id']) is not None:
        return ORJSONResponse(status_code=409, content={"message": "User already exists"})
    user = create_user(data['vk_id'], data['email'], data['fio'], data['competencies'])
    return ORJSONResponse(user.to_dict(), status_code=200)

@app.get("/user/{vk_id}/", response_model=pdUser, responses={
    404: {
        "description": "User not found", "content": {
        "application/json": {
            "example": {
                "message": "User not found"
                }
            }
        }
    },
    200:{
        "description": "User found",
        "content": {
            "application/json": {
                "example": {
                    "vk_id": 1,
                    "last_project_id": 1
                }
            } 
        }
    }
})
async def get_user(vk_id: int):
    user = get_user_by_vk_id(vk_id)
    if user is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    return ORJSONResponse(user, status_code=200)

@app.post("/user/update/{vk_id}/", response_model=pdUser, responses={
    404: {
        "description": "User not found", "content": {
        "application/json": {
            "example": {
                "message": "User not found"
                }
            }
        }
    },
    200:{
        "description": "User updated",
        "content": {
            "application/json": {
                "example": {
                    "vk_id": 1,
                    "last_project_id": 1
                }
            } 
        }
    }
})
async def update_user(vk_id: int, data: dict):
    if get_user_by_vk_id(vk_id) is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    return ORJSONResponse(status_code=200, content=update_last_project_id(vk_id, data))

@app.post("/Project/create/", response_model=pdProject, responses={
    200:{
        "description": "Project created",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "author_id": 1,
                    "creation_time": "2022-01-01 00:00:00"
                }
            } 
        }
    },
    404: {
        "description": "User not found", "content": {
        "application/json": {
            "example": {
                "message": "User not found"
                }
            }
        }
    }
})
async def create_Project(data: dict):
    if get_user_by_vk_id(data["author_id"]) is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    return ORJSONResponse(status_code=200, content=new_Project(data["author_id"]))

@app.get("/Project/{Project_id}/", response_model=pdProject, responses={
    404: {
        "description": "Project not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Project not found"
                }
            }
        }
    },
    200:{
        "description": "Project found",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "author_id": 1,
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    }
})
async def get_Project(Project_id: int):
    Project = get_Project_by_id(Project_id)
    if Project is None:
        return ORJSONResponse(status_code=404, content={"message": "Project not found"})
    return ORJSONResponse(Project, status_code=200)

@app.delete("/Project/{Project_id}/", responses={
    404: {
        "description": "Project not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Project not found"
                }
            }
        }
    },
    200:{
        "description": "Project deleted",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "author_id": 1,
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    }
})
async def del_Project(Project_id: int):
    Project = get_Project_by_id(Project_id)
    if Project is None:
        return ORJSONResponse(status_code=404, content={"message": "Project not found"})
    return ORJSONResponse(status_code=200, content=delete_Project(Project.id))

@app.patch("/Project/{Project_id}/", response_model=pdProject, responses={
    404: {
        "description": "Project not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Project not found"
                }
            }
        }
    },
    200:{
        "description": "Project updated",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "author_id": 1,
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    }
})
async def upd_Project(Project_id: int, data: dict):
    Project = get_Project_by_id(Project_id)
    if Project is None:
        return ORJSONResponse(status_code=404, content={"message": "Project not found"})
    return ORJSONResponse(status_code=200, content=update_Project(Project_id, data))

@app.get("/Projects/{page}/{page_size}/", response_model=list[pdProject], responses={
    200:{
        "description": "Projects found",
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 1,
                        "author_id": 1,
                        "creation_time": "2022-01-01 00:00:00"
                    }
                ]
            }
        }
},
    404: {
        "description": "Projects not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Projects not found"
                }
            }
        }
    }
})
async def get_Projects_with_pag(page: int, page_size: int):
    Projects = get_Projects_with_pagination(page_size, page)
    if Projects is None:
        return ORJSONResponse(status_code=404, content={"message": "Projects not found"})
    return ORJSONResponse(Projects, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
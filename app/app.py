from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from database.database import pdIdea, pdUser
from database.User.methods import create_user, get_user_by_vk_id, update_last_project_id
from database.Ideas.methods import new_idea, get_idea_by_id, delete_idea, get_ideas_by_author_id_with_pagination, update_idea, get_ideas_with_pagination
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

@app.post("/idea/create/", response_model=pdIdea, responses={
    200:{
        "description": "Idea created",
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
async def create_idea(data: dict):
    if get_user_by_vk_id(data["author_id"]) is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    return ORJSONResponse(status_code=200, content=new_idea(data["author_id"]))

@app.get("/idea/{idea_id}/", response_model=pdIdea, responses={
    404: {
        "description": "Idea not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Idea not found"
                }
            }
        }
    },
    200:{
        "description": "Idea found",
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
async def get_idea(idea_id: int):
    idea = get_idea_by_id(idea_id)
    if idea is None:
        return ORJSONResponse(status_code=404, content={"message": "Idea not found"})
    return ORJSONResponse(idea, status_code=200)

@app.delete("/idea/{idea_id}/", responses={
    404: {
        "description": "Idea not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Idea not found"
                }
            }
        }
    },
    200:{
        "description": "Idea deleted",
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
async def del_idea(idea_id: int):
    idea = get_idea_by_id(idea_id)
    if idea is None:
        return ORJSONResponse(status_code=404, content={"message": "Idea not found"})
    return ORJSONResponse(status_code=200, content=delete_idea(idea.id))

@app.patch("/idea/{idea_id}/", response_model=pdIdea, responses={
    404: {
        "description": "Idea not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "Idea not found"
                }
            }
        }
    },
    200:{
        "description": "Idea updated",
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
async def upd_idea(idea_id: int, data: dict):
    idea = get_idea_by_id(idea_id)
    if idea is None:
        return ORJSONResponse(status_code=404, content={"message": "Idea not found"})
    return ORJSONResponse(status_code=200, content=update_idea(idea_id, data))

@app.get("/ideas/{page}/{page_size}/", response_model=list[pdIdea], responses={
    200:{
        "description": "Ideas found",
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
        "description": "Ideas not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Ideas not found"
                }
            }
        }
    }
})
async def get_ideas_with_pag(page: int, page_size: int):
    ideas = get_ideas_with_pagination(page_size, page)
    if ideas is None:
        return ORJSONResponse(status_code=404, content={"message": "Ideas not found"})
    return ORJSONResponse(ideas, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from database.database import pdProject, pdUser, pdTeam
from database.User.methods import create_user, get_user_by_vk_id, update_last_project_id, accept_invite, leave_team
from database.Project.methods import (new_Project, 
                                      get_Project_by_id, 
                                      delete_Project, 
                                      get_Projects_by_author_id_with_pagination, 
                                      update_Project, 
                                      get_Projects_with_pagination,
                                      get_Projects_by_category_with_pagination,
                                      get_all_projects,
                                      get_projects_by_category,
                                      get_projects_by_category_with_pagination)

from database.Team.methods import create_team, get_team_by_id, new_project_in_team, all_teams, update_team, delete_team

import orjson

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8090",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8090",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/user/{vk_id}/{team_id}/accept_invite/", response_model=pdTeam, responses={
    200:{
        "description": "Invite accepted",
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
async def accept_inv(vk_id: int, team_id: int):
    user = get_user_by_vk_id(vk_id)
    if user is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    user = accept_invite(user, team_id)
    return ORJSONResponse(user, status_code=200)

@app.post("/user/{vk_id}/{team_id}/leave_team/", response_model=pdUser, responses={
    200:{
        "description": "User left",
        "content": {
            "application/json": {
                "example": {
                    "vk_id": 1,
                    "last_project_id": 1
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
async def leav_team(vk_id: int, team_id: int):
    user = get_user_by_vk_id(vk_id)
    if user is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    user = leave_team(vk_id, team_id)
    return ORJSONResponse(user, status_code=200)

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
    
    return ORJSONResponse(status_code=200, content=new_Project(data))

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
async def get_Projects_with_pag(page: int=1, page_size: int=10):
    Projects = get_Projects_with_pagination(page_size, page)
    if Projects is None:
        return ORJSONResponse(status_code=404, content={"message": "Projects not found"})
    return ORJSONResponse(Projects, status_code=200)

@app.get("/Projects/", response_model=list[pdProject], responses={
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
async def get_all_Projects():
    Projects = get_all_projects()
    if Projects is None:
        return ORJSONResponse(status_code=404, content={"message": "Projects not found"})
    return ORJSONResponse(Projects, status_code=200)

@app.get("/Project/{category}/", response_model=list[pdProject], responses={
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
def get_Projects_by_category(category: str):
    Projects = get_projects_by_category(category)
    if Projects is None:
        return ORJSONResponse(status_code=404, content={"message": "Projects not found"})
    return ORJSONResponse(Projects, status_code=200)

@app.get("/Project/{category}/{page}/{page_size}/", response_model=list[pdProject], responses={
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
async def get_Projects_by_category_with_pag(category: str, page: int=1, page_size: int=10):
    Projects = get_projects_by_category_with_pagination(category, page_size, page)
    if Projects is None:
        return ORJSONResponse(status_code=404, content={"message": "Projects not found"})
    return ORJSONResponse(Projects, status_code=200)

@app.post("/team/create/", response_model=pdTeam, responses={
    200:{
        "description": "Team created",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Team 1",
                    "description": "Team 1 description",
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    },
    404: {
        "description": "User not found", 
        "content": {
            "application/json": {
                "example": {
                    "message": "User not found"
                }
            }
        }
    }
})
async def new_team(data: dict):
    if get_user_by_vk_id(data["leader_id"]) is None:
        return ORJSONResponse(status_code=404, content={"message": "User not found"})
    return ORJSONResponse(status_code=200, content=create_team(data))

@app.get("/team/", response_model=list[pdTeam], responses={
    200:{
        "description": "Teams found",
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 1,
                        "name": "Team 1",
                        "description": "Team 1 description",
                        "creation_time": "2022-01-01 00:00:00"
                    }
                ]
            }
        }
    },
    404: {
        "description": "Teams not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Teams not found"
                }
            }
        }
    }
})
async def get_all_teams():
    teams = all_teams()
    if teams is None:
        return ORJSONResponse(status_code=404, content={"message": "Teams not found"})
    return ORJSONResponse(teams, status_code=200)

@app.get("/team/{team_id}/", response_model=pdTeam, responses={
    200:{
        "description": "Team found",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Team 1",
                    "description": "Team 1 description",
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    },
    404: {
        "description": "Team not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Team not found"
                }
            }
        }
    }
})
async def get_team(team_id: int):
    team = get_team_by_id(team_id)
    if team is None:
        return ORJSONResponse(status_code=404, content={"message": "Team not found"})
    return ORJSONResponse(team, status_code=200)

@app.post("/team/update/{team_id}/", response_model=pdTeam, responses={
    200:{
        "description": "Team updated",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Team 1",
                    "description": "Team 1 description",
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    },
    404: {
        "description": "Team not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Team not found"
                }
            }   
        }
    }
})
async def upd_team(team_id: int, data: dict):
    team = get_team_by_id(team_id)
    if team is None:
        return ORJSONResponse(status_code=404, content={"message": "Team not found"})
    return ORJSONResponse(status_code=200, content=update_team(team_id, data))

@app.delete("/team/{team_id}/", responses={
    200:{
        "description": "Team deleted",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "name": "Team 1",
                    "description": "Team 1 description",
                    "creation_time": "2022-01-01 00:00:00"
                }
            }
        }
    },
    404: {
        "description": "Team not found",
        "content": {
            "application/json": {
                "example": {
                    "message": "Team not found"
                }
            }
        }
    }
})
async def del_team(team_id: int):
    team = get_team_by_id(team_id)
    if team is None:
        return ORJSONResponse(status_code=404, content={"message": "Team not found"})
    return ORJSONResponse(status_code=200, content=delete_team(team_id))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
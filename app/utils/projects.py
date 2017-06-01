def projects():
    projects=[
    {
        "id":1,
        "name":"Project x",
        "description":"Project x description",
        "createdAt":"5/31/2017",
        "notes":
        [
            {
                "note_id":1,
                "email":"email 0",
                "text":"text 0",
                "subject":"subject 0",
                "images":{
                    "1.jpg",
                    "2.jpg"
                }
            },
            {   "note_id":2,
                "email":"email 1",
                "text":"text 1",
                "subject":"subject 1"
            }
        ]
    },
    {
        "id": 2,
        "name": "Project y",
        "description": "Project y description",
        "createdAt": "5/31/2017",
        "notes":
        [
            {
                "note_id": 3,
                "email": "email project y 0",
                "text": "text project y 0",
                "subject": "subject project y 0"
            }
        ]
      }
    ]
    return projects

def projects():
    projects=[
    {
        "id":1,
        "name":"Project x",
        "description":"Project x description",
        "createdAt":"5/31/2017",
        #notes
        "notes":
        [
            {
                "note_id":1,
                "email":"email 0",
                "text":"text 0",
                "subject":"subject 0",
                "images":[
                    "1.jpg",
                    "2.jpg"
                ]
            },
            {   "note_id":2,
                "email":"email 1",
                "text":"text 1",
                "subject":"subject 1"
            }
        ],
        #end of notes
        "retail":[
            {
                "customer_satisfaction": [
                    {
                        "period":"January",
                        "percentage":30

                    },
                    {
                        "period":"February",
                        "percentage":70
                    },
                    {
                        "period": "March",
                        "percentage": 20
                    },
                    {
                        "period": "April",
                        "percentage": 10
                    },
                    {
                        "period": "May",
                        "percentage": 80
                    }
                ],
                # stock
                "stock": [
                    {
                        "period":"January",
                        "percentage":40,
                        "region": [
                            {
                                "city": "Obilic",
                                "amount": 1
                            },
                            {
                                "city": "Prizren",
                                "amount": 3
                            },
                        ]
                    },
                    {
                        "period": "Ferbruary",
                        "percentage": 50,
                         "region": [
                            {
                                "city": "Obilic",
                                "amount": 20
                            },
                            {
                                "city": "Prizren",
                                "amount": 10
                            },
                        ]
                    }
                ],
                #end of stock
                "sales": [
                    {
                        "period": "January",
                        "percentage": 30

                    },
                    {
                        "period": "February",
                        "percentage": 70
                    },
                    {
                        "period": "March",
                        "percentage": 20
                    },
                    {
                        "period": "April",
                        "percentage": 10
                    },
                    {
                        "period": "May",
                        "percentage": 80
                    }
                ],
            }
        ],
        #end of retail
        'healthcare':[
            {
            "customer_satisfaction": [

                    {
                        "period": "January",
                        "percentage": 50,
                        "region": [
                            {
                                "city": "Obilic",
                                "amount": 20,
                                "hospitals":[
                                    {
                                        "hospital":"Hospital x",
                                        "amount":20
                                    },
                                    {
                                        "hospital": "Hospital y",
                                        "amount": 10
                                    },
                                ]
                            },
                            {
                                "city": "Prizren",
                                "amount": 10,
                                "hospitals": [
                                    {
                                        "hospital": "Hospital x Prizren",
                                        "amount": 20
                                    },
                                    {
                                        "hospital": "Hospital y Prizren",
                                        "amount": 10
                                    },
                                ]
                            },
                        ]
                    },

                {
                    "period": "Ferbruary",
                    "percentage": 20,
                    "region": [
                        {
                            "city": "Obilic",
                            "amount": 20,
                            "hospitals": [
                                {
                                    "hospital": "Hospital x",
                                    "amount": 20
                                },
                                {
                                    "hospital": "Hospital y",
                                    "amount": 10
                                },
                            ]
                        },
                        {
                            "city": "Prizren",
                            "amount": 10,
                            "hospitals": [
                                {
                                    "hospital": "Hospital x Prizren",
                                    "amount": 20
                                },
                                {
                                    "hospital": "Hospital y Prizren",
                                    "amount": 10
                                },
                            ]
                        },
                    ]
                }#end of january

                ]#end of customer sat
            }
        ]#end of healthcare
    },
    #end of project 1
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

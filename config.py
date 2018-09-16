config = {
    "foodUrl" : "https://hooks.slack.com/services/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"
}

statOrderBody ={
    "text": "Please rate your food experience",
    "attachments": [
        {
            "fallback": "Rate food",
            "title": "How do you feel about your food?",
            "callback_id": "food_rate",
            "color": "#3AA3E3",
            "text": "This will affect following restaurants choice.",
            "actions": [
                {
                    "name": "action",
                    "type": "button",
                    "text": "Amazing",
                    "style": "primary",
                    "value": "amazing"
                },
                {
                    "name": "action",
                    "type": "button",
                    "text": "Good",
                    "style": "primary",
                    "value": "good"
                },                
                {
                    "name": "action",
                    "type": "button",
                    "text": "So-so",
                    "style": "",
                    "value": "soso"
                },  
                {
                    "name": "action",
                    "type": "button",
                    "text": "Bad",
                    "style": "danger",
                    "value": "bad"
                },                  
            ]
        }
    ]
}
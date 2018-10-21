config = {
    "foodUrl" : "https://hooks.slack.com/services/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",
    "test1Url" : "https://hooks.slack.com/services/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",
    "test2Url" : "https://hooks.slack.com/services/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",
    "G4G6YHQM6": "https://hooks.slack.com/services/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",
    "CCSAZ5M0T": "https://hooks.slack.com/services/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",
    "GCX98V9RN": "https://hooks.slack.com/services/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"
}

helperBody ={
    "attachments": [
        {
            "callback_id": "helper",
            "color": "#3AA3E3",
            "text": "Usage:	@food-order-bot COMMAND [PARAMS]\nCommands:\n"+
            "\t\ttom(orrow)\t\t[url] [event_name(default:demo)]\n"+
            "\t\ttod(ay)   \t\t\t[url] [event_name(default:demo)]\n"+
            "\t\tclear\t\t\t\t   clear all scheduled reminders in this channel\n"+
            "\t\tstatus\t\t\t\t show #reminders in this channel",            
        }
    ]
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
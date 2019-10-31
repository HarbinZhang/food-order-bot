config = {
    "test1Url" : "https://hooks.slack.com/services/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",
    "test2Url" : "https://hooks.slack.com/services/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",
    "G4G6YHQM6": "https://hooks.slack.com/services/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",
    "CCSAZ5M0T": "https://hooks.slack.com/services/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",
    "GCX98V9RN": "https://hooks.slack.com/services/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"
}

rateToScore = {
    'amazing' : 100,
    'good' : 90,
    'moderate' : 60,
    'bad' : 0
}

rateSummaryBody = lambda restaurant, cnt, score : {
    "attachments": [
        {
            "callback_id": "rateSummaryBody",
            "color": "#3AA3E3",
            "title": restaurant,
            "text": "Got " + score + "/100 score in the last food order rate\n"+
            "\tfrom " + cnt + " people's feedback",  
        }
    ]    
}

ephemeralBody = lambda text : {
  "response_type": "ephemeral",
  "replace_original": False,
  "text": text
}


helperBody = {
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


statOrderBody = lambda callback_id : {
    "text": "Please rate your food experience",
    "attachments": [
        {
            "fallback": "Rate food",
            "title": "How do you feel about your food?",
            "callback_id": callback_id,
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
                    "text": "Moderate",
                    "style": "",
                    "value": "moderate"
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
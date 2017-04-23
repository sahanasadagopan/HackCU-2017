<h1>Voice Controlled Bot Car using Amazon Echo</h1>

<h4>(This Project is incomplete as we couldn't solve our bot's control issues and couldn't make our bot's servo and DC-motors move in a sync.)</h4>

So, what we have coded so far on integrating Amazon Echo and fetching the decoded direction from AWS on our local system is uploaded here.
1) Command.py is python file which queries DynamoDB on AWS and print changing direction.
2) NewWorkingLambdaFunc is the lambda function code which needs to be there on AWS (not to be run on local system)
3) "Intent Schema" on developer.amazon.com:
```javascript
{
  "intents": [
    {
      "slots": [
        {
          "name": "Command",
          "type": "LIST_OF_COMMANDS"
        }
      ],
      "intent": "BotMovementIsIntent"
    },
    {
      "intent": "WhatsNewBotDirectionIsIntent"
    },
    {
      "intent": "AMAZON.HelpIntent"
    }
  ]
}
```
4) Echo Skill Config
![alt tag](https://github.com/vibhormishra/HackCU-2017/blob/master/Echo_Skill_Config.png)

5) Lambda Configureation:
![alt tag](https://github.com/vibhormishra/HackCU-2017/blob/master/Lambda_Config.png)

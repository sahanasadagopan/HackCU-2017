1) Command.py is python file which queries DynamoDB on AWS and print changing direction.
2) NewWorkingLambdaFunc is the lambda function code which needs to be there on AWS (not to be run on local system)
3) "Intent Schema" on developer.amazon.com:

{
  "intents": [
    {
      "slots": [
        {
          "name": "Command",
          "type": "LIST_OF_COMMANDS"
        }
      ],
      "intent": "MyColorIsIntent"
    },
    {
      "intent": "WhatsMyColorIntent"
    },
    {
      "intent": "AMAZON.HelpIntent"
    }
  ]
}

This project contains a bare bones AWS SAM Lambda application to determine the correct configuration for debugging in VS Code

To build the Lambda I'm runnig:

```
sam build --use-container
```

To invoke the Lambda I'm running

```
sam local invoke -d 5890
```

Currently when I put a breakpoint in the code found in the `.aws-sam/build` folder that is created by `sam build`, and start the debugger in VS Code, the code executes but the breakpoint is ignored
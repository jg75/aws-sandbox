import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_sandbox.aws_sandbox_stack import AwsSandboxStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_sandbox/aws_sandbox_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsSandboxStack(app, "aws-sandbox")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

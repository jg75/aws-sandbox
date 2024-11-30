from typing import Any

from aws_cdk import Stack
from constructs import Construct

from aws_sandbox.config.params import Params
from aws_sandbox.constructs.vpc import VpcConstruct


class AwsSandboxStack(Stack):
    """The stack for the AWS sandbox."""

    params: Params

    def __init__(self, scope: Construct, construct_id: str, params: Params, **kwargs: Any) -> None:
        """Create a new stack with the given parameters."""
        super().__init__(scope, construct_id, **kwargs)
        self.params = params
        self.createConstructs()

    def createConstructs(self) -> None:
        """Create the constructs for the stack."""
        VpcConstruct(self, "VpcConstruct", self.params)

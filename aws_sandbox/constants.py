from typing import Type

from aws_cdk import Stack

from aws_sandbox.config.params import Params
from aws_sandbox.config.sandbox import Sandbox
from aws_sandbox.stacks.aws_sandbox_stack import AwsSandboxStack


class Constants:
    """Constants for the application."""

    def __init__(self) -> None:
        """Initialize the constants."""
        pass

    stages: dict[str, Type[Params]] = {
        "sandbox": Sandbox,
    }
    stacks: list[dict[str, str | Type[Stack]]] = [
        {
            "name": "AwsSandbox",
            "class": AwsSandboxStack,
        }
    ]

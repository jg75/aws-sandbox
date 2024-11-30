from typing import Any

from aws_cdk import App, Environment

from aws_sandbox.config.params import Params
from aws_sandbox.constants import Constants


class Main:
    """Main application class."""

    app: App
    stage: str
    params: Params
    env: Environment

    def __init__(self) -> None:
        """Create the App and Stacks."""
        self.app = App()
        self.stage = self.get_stage()
        self.params = self.get_params()
        self.env = self.get_env()

        for stack in Constants.stacks:
            tags: dict = {
                "Environment": self.stage,
                "Project": Constants.project,
            }

            stack["class"](self.app, stack["name"], self.params, env=self.env, tags=tags)

        self.app.synth()

    def get_stage(self) -> Any:
        """Gets the default stage parameter."""
        try:
            return self.app.node.try_get_context("stage")
        except KeyError:
            print("Stage not found")
            exit(1)

    def get_params(self) -> Params:
        """Get the parameters for the stacks."""
        try:
            return Constants.stages[self.stage]()
        except KeyError:
            print("Stage not found")
            exit(1)

    def get_env(self) -> Environment:
        """Gets the Environment for the stacks."""
        stage_context = self.app.node.try_get_context(self.stage)
        return Environment(**stage_context)

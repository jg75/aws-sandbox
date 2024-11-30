import pytest
from dataclasses import dataclass, field
from typing import Dict, Any

from aws_cdk import App, Environment
from aws_cdk.aws_ec2 import IpAddresses, SubnetType

from aws_sandbox.config.params import Params
from aws_sandbox.stacks.aws_sandbox_stack import AwsSandboxStack

@dataclass
class Params:
    pass

@dataclass
class Test(Params):

    vpc: Dict[str, Any] = field(default_factory=lambda: {
        "ip_addresses": IpAddresses.cidr("10.0.0.0/16"),
        "max_azs": 1,
        "subnet_configuration": [
            {
                "cidrMask": 24,
                "name": "sandbox-public",
                "subnetType": SubnetType.PUBLIC,
            },
            {
                "cidrMask": 24,
                "name": "sandbox-private",
                "subnetType": SubnetType.PRIVATE_ISOLATED,
            },
        ],
    })


@pytest.fixture(scope="session")
def app() -> App:
    """Create a fresh CDK app fixture."""
    return App()

@pytest.fixture
def mock_context() -> dict:
    """Fixture to provide mock context values."""
    return {
        "stage": "test",
        "test": {
            "account": "000000000000",
            "region": "us-test-1"
        }
    }

@pytest.fixture
def mock_params():
    """Fixture to provide mock params values."""
    return Test()

@pytest.fixture
def stack(app, mock_context, mock_params):
    """Create a stack fixture."""
    app.node.set_context("stage", mock_context["stage"])
    app.node.set_context("test", mock_context["test"])
    env = Environment(**mock_context["test"])
    return AwsSandboxStack(app, "aws-sandbox", mock_params, env=env)

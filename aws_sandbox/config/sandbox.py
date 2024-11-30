from aws_cdk.aws_ec2 import IpAddresses, SubnetType

from aws_sandbox.config.params import Params


class Sandbox(Params):
    """Parameters for the sandbox stage."""

    vpc: dict = {
        "vpc_name": "Sandbox",
        "ip_addresses": IpAddresses.cidr("172.0.0.0/16"),
        "max_azs": 3,
        "subnet_configuration": [
            {
                "cidrMask": 24,
                "name": "Public",
                "subnetType": SubnetType.PUBLIC,
            },
            {
                "cidrMask": 24,
                "name": "Isolated",
                "subnetType": SubnetType.PRIVATE_ISOLATED,
            },
        ],
    }

    def __init__(self) -> None:
        """Initialize the Params."""
        super().__init__()

    def __repr__(self) -> str:
        """Return a string representation of the Params."""
        return f"{self.__class__.__name__}(vpc={self.vpc})"

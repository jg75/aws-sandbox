from aws_cdk import CfnOutput
from aws_cdk.aws_ec2 import GatewayVpcEndpoint, GatewayVpcEndpointAwsService, Vpc
from constructs import Construct

from aws_sandbox.config.params import Params


class VpcConstruct(Construct):
    """Construct for the VPC."""

    params: Params
    vpc: Vpc

    def __init__(self, scope: Construct, id: str, params: Params) -> None:
        """Creates a new VpcConstruct with the given parameters."""
        super().__init__(scope, id)
        self.params = params
        self.vpc = Vpc(self, "Vpc", **self.params.vpc)

        self.createGatewayVpcEndpoints()
        self.createOutputs()

    def createGatewayVpcEndpoints(self) -> None:
        """Create gateway VPC endpoints for the VPC."""
        GatewayVpcEndpoint(
            self,
            "S3GatewayEndpoint",
            vpc=self.vpc,
            service=GatewayVpcEndpointAwsService.S3,
        )
        GatewayVpcEndpoint(
            self,
            "DynamoDBGatewayEndpoint",
            vpc=self.vpc,
            service=GatewayVpcEndpointAwsService.DYNAMODB,
        )

    def createOutputs(self) -> None:
        """Create outputs for the stack."""
        CfnOutput(self, "VpcId", value=self.vpc.vpc_id)
        CfnOutput(self, "VpcCidr", value=self.vpc.vpc_cidr_block)

        for i, subnet in enumerate(self.vpc.public_subnets):
            CfnOutput(self, f"PublicSubnet{i}Id", value=subnet.subnet_id)
            CfnOutput(self, f"PublicSubnet{i}Cidr", value=subnet.ipv4_cidr_block)

        for i, subnet in enumerate(self.vpc.private_subnets):
            CfnOutput(self, f"PrivateSubnet{i}Id", value=subnet.subnet_id)
            CfnOutput(self, f"PrivateSubnet{i}Cidr", value=subnet.ipv4_cidr_block)

        for i, subnet in enumerate(self.vpc.isolated_subnets):
            CfnOutput(self, f"IsolatedSubnet{i}Id", value=subnet.subnet_id)
            CfnOutput(self, f"IsolatedSubnet{i}Cidr", value=subnet.ipv4_cidr_block)

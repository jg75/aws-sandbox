from aws_cdk.assertions import Template, Match

from aws_sandbox.stacks.aws_sandbox_stack import AwsSandboxStack


def test_vpc(stack) -> None:
    """Test VPC creation with expected properties."""
    template = Template.from_stack(stack)
    
    # Test VPC resource exists with expected properties
    template.has_resource_properties("AWS::EC2::VPC", {
        "CidrBlock": "10.0.0.0/16",
        "EnableDnsHostnames": True,
        "EnableDnsSupport": True,
    })

    # Test that at least one subnet matches our public subnet properties
    template.has_resource_properties("AWS::EC2::Subnet", {
        "CidrBlock": Match.string_like_regexp("10.0.*"),
        "MapPublicIpOnLaunch": True,
    })

    # Test that at least one subnet matches our private subnet properties
    template.has_resource_properties("AWS::EC2::Subnet", {
        "CidrBlock": Match.string_like_regexp("10.0.*"),
        "MapPublicIpOnLaunch": False,
    })

def test_vpc_endpoints(stack) -> None:
    """Test VPC endpoints creation."""
    template = Template.from_stack(stack)
    
    def assert_gateway_endpoint(service: str) -> None:
        """Helper to assert gateway endpoint properties."""
        template.has_resource_properties("AWS::EC2::VPCEndpoint", {
            "ServiceName": {
                "Fn::Join": [
                    "",
                    [
                        "com.amazonaws.",
                        {"Ref": "AWS::Region"},
                        f".{service}"
                    ]
                ]
            },
            "VpcEndpointType": "Gateway",
            "VpcId": Match.any_value()
        })
    
    assert_gateway_endpoint("s3")
    assert_gateway_endpoint("dynamodb")

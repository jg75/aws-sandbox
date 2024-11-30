from aws_cdk.assertions import Template, Match

from aws_sandbox.stacks.aws_sandbox_stack import AwsSandboxStack


def test_vpc_created(stack) -> None:
    """Test VPC creation with expected properties."""
    template = Template.from_stack(stack)
    
    # Test VPC resource exists with expected properties
    template.has_resource_properties("AWS::EC2::VPC", {
        "CidrBlock": "10.0.0.0/16",
        "EnableDnsHostnames": True,
        "EnableDnsSupport": True,
    })
    
    # Find all subnet resources
    subnet_resources = template.find_resources("AWS::EC2::Subnet")
    
    # Test that we have the expected number of subnets
    assert len(subnet_resources) == 2
    
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
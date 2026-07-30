from unittest.mock import MagicMock, patch

from botocore.config import Config
from core.common.models.aws_config import AWSConfig


def test_aws_config_initialization_defaults():
    config = AWSConfig(region_name="us-west-2")
    assert config.region_name == "us-west-2"
    assert config.endpoint_url is None
    assert config.aws_access_key_id is None
    assert config.aws_secret_access_key is None
    assert config.aws_session_token is None
    assert config.boto_config_params == {}


@patch("boto3.resource")
def test_create_resource_passes_arguments_correctly(mock_boto3_resource):
    """Ensure raw fields map directly to boto3 resource factory signatures."""
    mock_resource_instance = MagicMock()
    mock_boto3_resource.return_value = mock_resource_instance

    config = AWSConfig(
        region_name="us-east-1",
        endpoint_url="http://localhost:4566",
        aws_access_key_id="test-key",
        aws_secret_access_key="test-secret",
        aws_session_token="test-token",
        boto_config_params={"max_pool_connections": 25, "read_timeout": 5},
    )

    resource = config.create_resource("dynamodb")

    # Assert factory method outputs correctly
    assert resource == mock_resource_instance

    # Extract the runtime parameters passed to boto3.resource
    mock_boto3_resource.assert_called_once()
    args, kwargs = mock_boto3_resource.call_args

    assert args[0] == "dynamodb"
    assert kwargs["region_name"] == "us-east-1"
    assert kwargs["endpoint_url"] == "http://localhost:4566"
    assert kwargs["aws_access_key_id"] == "test-key"
    assert kwargs["aws_secret_access_key"] == "test-secret"
    assert kwargs["aws_session_token"] == "test-token"

    # Assert botocore Config wrapper was dynamically built
    assert isinstance(kwargs["config"], Config)

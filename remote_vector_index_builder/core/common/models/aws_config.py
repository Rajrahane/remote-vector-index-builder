from dataclasses import dataclass, field
from typing import Optional, Any, Dict
import boto3
from botocore.config import Config


@dataclass
class AWSConfig:
    region_name: str
    endpoint_url: Optional[str] = None

    # AWS Credentials parameters
    # Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_session_token: Optional[str] = None
    boto_config_params: Dict[str, Any] = field(default_factory=dict)

    def create_resource(
        self, service_name: str
    ) -> boto3.resources.base.ServiceResource:

        botocore_config = (
            Config(**self.boto_config_params) if self.boto_config_params else None
        )

        return boto3.resource(
            service_name,
            region_name=self.region_name,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            aws_session_token=self.aws_session_token,
            config=botocore_config,
        )

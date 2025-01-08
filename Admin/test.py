import boto3

bedrock_client = boto3.client("bedrock", region_name="eu-north-1")
response = bedrock_client.list_foundation_models()
print("Available Models:", response)

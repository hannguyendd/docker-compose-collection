# LocalStack

LocalStack is a fully functional local AWS cloud stack for developing and testing cloud & serverless applications offline.

## Quick Start

```bash
docker compose -f localstack/localstack.yaml -p localstack up -d
```

## Environment Variables

Create a `.env` file in the `localstack/` directory with the following variables (all are optional):

```env
# LocalStack Gateway Port
HOST_PORT=4566

# Internal services port range
HOST_PORT_INTERNAL=4510-4559

# AWS Services to start (empty = all services)
# Examples: s3,dynamodb,lambda,sqs,sns,apigateway
SERVICES=

# Debug mode (0 or 1)
DEBUG=0

# AWS Configuration
AWS_DEFAULT_REGION=us-east-1
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
```

## Connection Details

- **Gateway URL**: `http://localhost:4566`
- **Default Credentials**:
  - Access Key ID: `test`
  - Secret Access Key: `test`
  - Region: `us-east-1`

## Using AWS CLI with LocalStack

Configure your AWS CLI to use LocalStack:

```bash
# Set endpoint for all commands
aws --endpoint-url=http://localhost:4566 s3 ls

# Or create a profile
aws configure --profile localstack
# Use endpoint: http://localhost:4566
# Access Key: test
# Secret Key: test
# Region: us-east-1
```

## Common Services

LocalStack supports many AWS services including:

- **S3**: Object storage
- **DynamoDB**: NoSQL database
- **Lambda**: Serverless functions
- **SQS**: Message queuing
- **SNS**: Pub/Sub messaging
- **API Gateway**: API management
- **CloudFormation**: Infrastructure as code
- **CloudWatch**: Monitoring and logging
- **Secrets Manager**: Secret storage
- **And many more...**

## Container Management

```bash
# Start LocalStack
docker compose -f localstack/localstack.yaml -p localstack up -d

# View logs
docker compose -f localstack/localstack.yaml -p localstack logs -f

# Stop LocalStack
docker compose -f localstack/localstack.yaml -p localstack down

# Stop and remove data
docker compose -f localstack/localstack.yaml -p localstack down -v
```

## Examples

### Create S3 Bucket

```bash
aws --endpoint-url=http://localhost:4566 s3 mb s3://my-bucket
aws --endpoint-url=http://localhost:4566 s3 ls
```

### Create DynamoDB Table

```bash
aws --endpoint-url=http://localhost:4566 dynamodb create-table \
    --table-name MyTable \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
```

### List Lambda Functions

```bash
aws --endpoint-url=http://localhost:4566 lambda list-functions
```

## Data Persistence

Data is persisted in the `localstack_data` Docker volume. To completely reset LocalStack, remove the volume:

```bash
docker compose -f localstack/localstack.yaml -p localstack down -v
```

## Resources

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/)
- [Supported Services](https://docs.localstack.cloud/references/coverage/)

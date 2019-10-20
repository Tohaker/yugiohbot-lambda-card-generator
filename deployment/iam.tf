resource "aws_iam_role" "lambda_card_generator" {
  name                = "lambda_card_generator"
  assume_role_policy  = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": "AssumeLambdaRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "lambda_logging" {
  name        = "YuGiOhCardGeneratorLambdaLogging"
  description = "Create and Write to all CloudWatch Logs."

  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "invoke_lambda" {
  name        = "InvokeYuGiOhCardGeneratorLambdaFunction"
  description = "Allows invokation of another Lambda Function."

  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "lambda:InvokeFunction"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "save_generated_images" {
  name        = "SaveGeneratedCardsToS3"
  description = "Allows the Lambda to upload a file to an S3 Bucket"
  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "s3:Put*"
      ],
      "Resource": "arn:aws:s3:::yu-gi-oh-images/generated/*"
    }
  ]
}
EOF
}

resource "aws_iam_policy_attachment" "attach_logging" {
  name       = "lambda-attachment"
  roles      = [
    aws_iam_role.lambda_card_generator.name
  ]
  policy_arn = aws_iam_policy.lambda_logging.arn
}

resource "aws_iam_policy_attachment" "attach_lambda" {
  name       = "lambda-attachment"
  roles      = [
    aws_iam_role.lambda_card_generator.name
  ]
  policy_arn = aws_iam_policy.invoke_lambda.arn
}

resource "aws_iam_policy_attachment" "attach_s3" {
  name       = "lambda-attachment"
  roles      = [
    aws_iam_role.lambda_card_generator.name
  ]
  policy_arn = aws_iam_policy.save_generated_images.arn
}

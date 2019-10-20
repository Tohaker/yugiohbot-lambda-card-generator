resource "aws_lambda_function" "card_generator" {
  s3_bucket         = var.bucket
  s3_key            = var.s3_package
  source_code_hash  = filebase64sha256(var.local_package)
  handler           = var.handler

  function_name     = local.lambda_title_text_name
  role              = aws_iam_role.lambda_card_generator.arn
  
  runtime           = var.runtime
  timeout           = 360

  memory_size       = 512

  environment {
    variables = {
      CHROMIUM = var.headless-chromium
      CHROMEDRIVER = var.chromedriver
    }
  }
}

resource "aws_cloudwatch_log_group" "card_generator" {
  name = "/aws/lambda/${local.lambda_title_text_name}"
}

resource "aws_cloudwatch_event_rule" "every_hour" {
  name                = "every-hour"
  description         = "Triggers every hour"
  schedule_expression = "cron(0 * * * ? *)"
}

resource "aws_cloudwatch_event_target" "every_hour" {
  rule      = aws_cloudwatch_event_rule.every_hour.name
  target_id = "generate_new_card_image"
  arn       = aws_lambda_function.card_generator.arn
}

resource "aws_lambda_permission" "allow_execution_from_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.card_generator.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_hour.arn
}

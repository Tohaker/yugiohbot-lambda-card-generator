set -e

RESULT=$(docker run -e CHROMIUM=/var/task/bin/headless-chromium -e CHROMEDRIVER=/var/task/bin/chromedriver -e AWS_LAMBDA_FUNCTION_MEMORY_SIZE=512 \
 --rm -v "$PWD"/package:/var/task lambci/lambda:python3.7 lambda_function.lambda_handler)

if [[ $RESULT == *"card_file"* ]]; then
  exit 0
else
  exit 1
fi

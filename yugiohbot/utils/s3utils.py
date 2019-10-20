import logging

import boto3

s3 = boto3.client('s3')


def upload_generated_card_to_s3(file):
    success = s3.upload_file(file, 'yu-gi-oh-images', 'generated/' + file)
    logging.debug('Upload ' + file + ' to S3: ' + str(success))


def download_cropped_image_from_s3(file):
    success = s3.download_file('yu-gi-oh-images', 'cropped/' + file, '/tmp/' + file)
    logging.debug("Download " + file + "from S3: " + str(success))

import json
import base64
#from sagemaker.serializers import IdentitySerializer
import boto3


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2021-12-21-21-02-36-527" ## TODO: fill in
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])## TODO: fill in

    # Make a prediction:
    ## TODO: fill in
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)

    # We return the data back to the Step Function   
    inferences = response["Body"].read().decode('utf-8')
    print(inferences)
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['image_data'],
            "s3_bucket": event['s3_bucket'],
            "s3_key": event['s3_key'],
            "inferences": inferences
        }
    }
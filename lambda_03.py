import json


THRESHOLD = .90


def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = json.loads(event['inferences']) ## TODO: fill in

    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = inferences[0] > THRESHOLD or inferences[1] > THRESHOLD ## TODO: fill in
    
    if inferences[0] > inferences[1]:
        label = "bicycle"
        confidence = inferences[0]
    else:
        label = "motorcycle"
        confidence = inferences[1]

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        return {
        'statusCode': 200,
        'body': {
            "prediction": {
                "label": label,
                "confidence": confidence
            } 
        }
    }
    
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
    
    
import json

def lambda_handler(event, context):
    # Extract numbers from the event
    num1 = event.get('num1')
    num2 = event.get('num2')
    
    # Check if the numbers are provided and are valid
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Please provide both num1 and num2.')
        }
    
    try:
        # Convert to float and add the numbers
        result = float(num1) + float(num2)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Invalid input. Please provide valid numbers.')
        }
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }

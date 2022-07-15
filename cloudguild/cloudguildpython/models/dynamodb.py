import boto3
TABLE_NAME="cloudguild"

def set_dynamodb_item(id, user):
    boto3.client("dynamodb").put_item(TableName=TABLE_NAME, Item= {
            "user": {"S": user},
            "id": {"S":id}
        })
    return {"message":"success"}
        
def get_dynamodb_item(id):
    return boto3.client("dynamodb").get_item(TableName=TABLE_NAME,Key = {"id": {"S":id}})
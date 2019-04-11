import os
import boto3


def get_pipeline_id(client, dp_name):
    response = client.list_pipelines()
    pipelines = response['pipelineIdList']

    for pipeline in pipelines:
        if dp_name == pipeline['name']:
            return pipeline['id']

    raise ValueError("Pipeline {0} was not found.".format(dp_name))


def lambda_handler(event, context):
    dp_name = os.environ['PipelineName']
    client = boto3.client('datapipeline')

    dp_id = get_pipeline_id(client, dp_name)

    response = client.activate_pipeline(pipelineId=dp_id)

    print("Execute pipeline response {0}".format(response))


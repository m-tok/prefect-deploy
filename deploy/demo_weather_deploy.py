from demo_weather import my_flow
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=my_flow, 
    name="example_from_deployment", 
    work_queue_name="dev",
    version="1", 
    tags=["demo"]
)

deployment.apply()
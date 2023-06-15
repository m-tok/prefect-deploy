from demo_weather import fetch_weather
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=fetch_weather, 
    name="example_from_deployment", 
    work_queue_name="dev",
    version="1", 
    tags=["demo"]
)

deployment.apply()
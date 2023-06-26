
from prefect.infrastructure import KubernetesJob, KubernetesImagePullPolicy

k8s_job = KubernetesJob(
    namespace="prefect",
    image="prefecthq/prefect:2-python3.9",
    image_pull_policy=KubernetesImagePullPolicy.IF_NOT_PRESENT,
)

k8s_job.save("k8s",overwrite=True )
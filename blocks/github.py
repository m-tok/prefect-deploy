from prefect.filesystems import GitHub

block = GitHub(
    repository=f"https://github.com/m-tok/prefect-deploy.git",
    reference="main",
    access_token="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",
)

block_name = "my-git-repo"
block_id = block.save(block_name, overwrite=True)
print(f"Created block '{block_name}' with ID '{block_id}'")